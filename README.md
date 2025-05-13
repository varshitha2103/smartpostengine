# 🤖 Local Auto-Repurpose Engine (LangChain + Mistral)

Turn raw content into polished platform-ready formats — all **locally** with no API key required.  
Built using **LangChain**, **Ollama**, and **Mistral**, this app is ideal for solopreneurs, creators, and marketers who want to **repurpose content into:**

- 🟦 LinkedIn carousels  
- 🐦 Tweet threads  
- 📧 Newsletter intros  

---

## ✨ Features

- 🔁 Repurposes podcast scripts, blogs, or outlines into platform-specific formats
- 🧠 Uses **Mistral** via **Ollama** — 100% local LLM inference
- 🧩 Built with **LangChain tools** instead of agents for reliability and speed
- ⚡ Streamlit UI for instant previews
- 🛡️ No external API key required

---

## 📸 Demo

<img width="227" alt="res1" src="https://github.com/user-attachments/assets/e5ac8c35-6c3d-4f6f-aff7-5dfc241d5fcc" />


## 🛠 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/) + [Mistral](https://ollama.com/library/mistral)
- Streamlit
- Python 3.10+

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/auto-repurpose-engine.git
cd auto-repurpose-engine
```

2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run Ollama with Mistral
Make sure Ollama is installed and running:
```bash
ollama run mistral
```
4. Launch the Streamlit app
```bash
streamlit run main.py
```
✏️ Example Input
In today’s episode, I discussed the biggest mistakes solopreneurs make when launching digital products. Most skip the validation phase and build in isolation. I also broke down the “3P Launch Formula”: Problem, People, and Proof...

✅ Output Example
LinkedIn Carousel:
Slide 1: 🚀 Launching Digital Products? Don’t Miss This!
Slide 2: 🤯 Most creators skip validation.
Slide 3: 🧠 Use the “3P Formula”: Problem, People, Proof
...
Tweet Thread:
1/ Most solopreneurs launch and get silence.
2/ Why? No validation. No feedback.
3/ Here's a better way ↓
...
Newsletter Intro:
Hey solopreneur,
If you're about to launch solo, stop and read this first...

🧠 How It Works
Each output format is powered by its own LangChain Tool, using a prompt template tailored for that platform. The app feeds your content through these tools using Mistral running locally via Ollama.

📂 Folder Structure
```bash
auto-repurpose-engine/
│
├── app.py                 # Streamlit UI
├── tools.py               # LangChain Tools (carousel, tweet, newsletter)
├── agent_runner.py        # Optional tool-chain runner
├── requirements.txt       
├── README.md              
└── assets/
    └── demo-screenshot.png
```

💡 Future Ideas
Add Instagram captions and YouTube hook generation
Download outputs as .md or .txt
Add persona-based tone options: Thought Leader, Storyteller, Data-Driven
Deploy to Hugging Face Spaces or Streamlit Cloud

🙌 Author
Made by Varshitha Yanamala
Part of #30DaysOfGenAI Challenge
Follow me on LinkedIn for more GenAI projects!

You can check it out here:
http://localhost:8504/
