# 🤖 AutoStream AI Agent

## 🎥 Demo

Example Interaction:

User: What does the pro plan include?
Agent: Pro plan costs $79/month with features Unlimited videos, 4K resolution, AI captions

User: I want to try the pro plan
Agent: Awesome! Let's get you started 🚀


## 🚀 Overview

This project is a conversational AI agent designed to automate social media interactions. It uses intent detection, retrieval-augmented generation (RAG), and a graph-based workflow to simulate real-world AI agent systems.

---

## 🧠 Features

* 🔍 Intent Detection (Greeting, Pricing, High Intent)
* 📚 RAG (FAISS-based vector retrieval)
* 🧭 LangGraph Agent Workflow
* 🧠 Context-aware Responses
* 📥 Lead Capture System

---

## 🏗️ Architecture

User Input → Intent Detection →
→ Greeting / RAG / Lead Capture → Response

---

## 📂 Project Structure

* `main.py` → Entry point
* `agent_graph.py` → LangGraph workflow
* `rag.py` → Vector search system
* `intent.py` → Intent classification
* `tools.py` → Lead capture
* `knowledge_base.json` → Data

---

## ⚙️ Tech Stack

* Python
* LangGraph
* FAISS
* Sentence Transformers

---

## 💡 Note

LLM integration was designed but responses are mocked during testing due to API quota limits. The system is fully compatible with real LLM APIs like Gemini or GPT.

---

## 🎯 Outcome

Built a modular AI agent capable of:

* Multi-turn conversations
* Knowledge retrieval
* Lead conversion

---
