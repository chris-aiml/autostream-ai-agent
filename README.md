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

## 🏗️ Architecture Explanation

This project uses LangGraph to design a modular and state-driven conversational AI agent. LangGraph was chosen over simple pipelines because it enables structured workflows using nodes and conditional routing, which closely resembles real-world agent systems. Each component of the agent is implemented as a node—intent detection, knowledge retrieval (RAG), and lead capture—while a router dynamically directs the flow based on user intent.

State management is handled through a shared state object passed across all nodes in the graph. This state stores key information such as user input, detected intent, generated response, and lead details (name, email, platform). By maintaining this state across multiple steps, the agent is able to support multi-turn conversations and ensure that actions such as lead capture are only triggered when all required information is collected.

The system also integrates a Retrieval-Augmented Generation (RAG) pipeline using FAISS and sentence-transformer embeddings. This allows the agent to retrieve relevant information from a local knowledge base instead of relying solely on predefined responses.

Overall, the architecture is modular, scalable, and designed to easily integrate with real LLM APIs and external services in production environments.


---

## 📱 WhatsApp Integration (Concept)

To integrate this agent with WhatsApp:

1. Use WhatsApp Business API (via providers like Twilio or Meta Cloud API)
2. Set up a webhook endpoint (Flask/FastAPI)
3. Incoming messages are sent to the webhook
4. Pass message into the agent (`app.invoke`)
5. Return agent response back to WhatsApp API
6. Maintain session state per user (using user ID)

This enables real-time conversational automation on WhatsApp.
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
