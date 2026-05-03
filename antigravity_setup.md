# Antigravity IDE Setup Guide

Welcome to **Antigravity**, your advanced agentic AI coding assistant! Antigravity is designed to seamlessly integrate into your development workflow, acting as an autonomous pair programmer capable of writing code, debugging, and managing entire projects.

This guide covers how to install the Antigravity application and configure it within your IDE environment.

---

## 🛠️ Prerequisites

Before installing Antigravity, ensure you have the following:
- **Operating System:** Windows 10/11, macOS 12+, or Linux.
- **Compatible IDE:** A modern editor environment (e.g., VS Code, Cursor, or the standalone Antigravity IDE client).
- **Network Connection:** A stable internet connection for real-time model inference and synchronization.
- **Authentication:** An active developer account or API token provided by your administrator.

---

## 📥 Installation

### Option 1: Standalone Application
1. **Download:** Navigate to the Antigravity developer portal and download the latest installer for your OS.
2. **Run Installer:** Execute the downloaded file and follow the on-screen instructions.
3. **Launch:** Open the Antigravity Application from your applications folder/Start menu.

### Option 2: IDE Extension (Recommended)
1. Open your IDE (e.g., VS Code).
2. Navigate to the **Extensions Marketplace**.
3. Search for **"Antigravity Agentic Assistant"**.
4. Click **Install**.
5. Once installed, restart your IDE to initialize the background services.

---

## ⚙️ Configuration & Setup

### 1. Authentication
Upon launching the extension or app for the first time, you will be prompted to authenticate:
- Click the **Login to Antigravity** button in the sidebar.
- Enter your credentials or paste your secure developer token.

### 2. Workspace Integration
To allow Antigravity to fully understand your project context:
- Open your target project directory in the IDE.
- Antigravity will automatically index the workspace (respecting `.gitignore`).
- Go to the **Antigravity Settings** gear icon to adjust indexing limits or exclude specific directories.

### 3. Model Selection
Antigravity supports various underlying models based on your task complexity:
- Open the **Model Selection** dropdown at the top of the chat interface.
- Select your preferred model (e.g., *Gemini 3.1 Pro (High)* for complex architectural tasks, or faster models for quick inline edits).

---

## 🚀 Getting Started

Once configured, you can start leveraging Antigravity:

- **Chat & Commands:** Open the Antigravity panel (`Ctrl+Shift+A` or `Cmd+Shift+A`) and describe your task in natural language.
- **Agentic Actions:** Give high-level instructions (e.g., *"Build a new login page with React and connect it to my backend"*), and watch Antigravity plan, execute, and verify the changes.
- **Inline Editing:** Highlight code, press the inline-edit shortcut (`Ctrl+K` / `Cmd+K`), and ask for refactoring or bug fixes.
- **Terminal Integration:** Antigravity can securely run tests, install dependencies, and manage version control directly from your terminal when authorized.

---

## 🛑 Troubleshooting

- **Connection Issues:** Ensure your firewall allows outbound connections on port 443.
- **Index Sync Failed:** Try clearing the local cache from `Settings > Advanced > Clear Workspace Cache` and reload the window.

For advanced settings, refer to the [official documentation portal](#).
