# Quokka Deployment Guide

This document outlines the steps required to deploy the **Quokka** application (frontend and backend) to a production environment.

## 1. Environment Variables

We have created an `.env.example` file in the root directory. You must set these environment variables in your deployment environment (e.g., Render, Vercel, Heroku, or AWS).

**Required Variables for Backend:**
- `PINECONE_API_KEY`: Pinecone API key
- `PINECONE_INDEX_NAME`: Pinecone index name (e.g., `rag-materials`)
- `GROQ_API_KEY`: Groq API key
- `HF_TOKEN`: HuggingFace token
- `MONGODB_URI`: MongoDB connection string
- `JWT_SECRET`: Secret key for JWT signing
- `GOOGLE_CLIENT_ID`: Google OAuth client ID

**Required Variables for Frontend:**
- `VITE_API_URL`: The URL of your deployed backend API (e.g., `https://quokka-backend.onrender.com`). The frontend is pre-configured to use this environment variable.

## 2. Backend Deployment (e.g., Render.com)

1. Create a **Web Service** on your chosen platform.
2. Point it to your repository.
3. **Build Command:** `npm install`
4. **Start Command:** `npm start`
5. **Root Directory:** `backend`
6. Add the environment variables listed in `.env.example`.

## 3. Frontend Deployment (e.g., Vercel or Netlify)

1. Create a new **Project** and link it to your repository.
2. **Framework Preset:** Vite
3. **Root Directory:** `frontend`
4. **Build Command:** `npm run build`
5. **Output Directory:** `dist`
6. **Environment Variables:** Set `VITE_API_URL` to the live URL of your deployed backend.

## Summary of Changes Made for Deployment Readiness:

1. **Frontend API References:** Replaced all hardcoded `http://localhost:8000` URLs with `import.meta.env.VITE_API_URL` in `App.jsx`, `AdminPage.jsx`, and `AuthModal.jsx`. This ensures the React app can dynamically connect to any production API.
2. **Backend Scripts:** Added a `"start": "node server.js"` script to `backend/package.json` for easy starting by cloud services.
3. **Configuration:** Created a `.env.example` file to document the required environment variables.
