from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Materials Science Chatbot API")

import os

# Configuration - Relative to this script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "..", "models", "final_qwen_model")
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading model from {model_path} on {device}...")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto" if torch.cuda.is_available() else {"": "cpu"}
)

class ChatRequest(BaseModel):
    message: str
    max_tokens: int = 512
    temperature: float = 0.7

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Construct ChatML format
        system_prompt = "You are a BRILLIANT and SUPER FRIENDLY Materials Science Expert! 🧠✨ Your goal is to provide helpful, detailed, and encouraging scientific answers. CRITICAL: You MUST use many relevant emojis (like 🔬, 🧪, 🚀, 👉, 🌟, 🧠) throughout your response. Structure your answers with BOLD headers and bullet points! 💎"
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": request.message}
        ]
        
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        model_inputs = tokenizer([text], return_tensors="pt").to(device)

        with torch.no_grad():
            generated_ids = model.generate(
                model_inputs.input_ids,
                max_new_tokens=request.max_tokens,
                temperature=request.temperature,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Remove input tokens from output
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return ChatResponse(response=response_text.strip())
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"status": "online", "model": "Qwen2.5-0.5B-Materials-Science"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
