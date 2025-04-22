# 🧠 Terminal AI Assistant – Powered by Cohere

A fast, simple, and dev-friendly CLI chatbot powered by [Cohere's](https://cohere.com) API. Built for developers, sysadmins, and IT pros who love their terminal.

---

## 🚀 Features

- Interactive CLI-based chat interface
- Context-aware threading using Cohere Chat
- Simple `.env`-based API key management
- Customizable system prompt & developer credits
- Smooth and snappy UX with a dev-friendly tone

---

## 📦 Requirements

- Python 3.8+
- [Cohere API key](https://dashboard.cohere.com/api-keys)
- `pip install` the following:

```bash
pip install cohere python-dotenv
```

---

## ⚙️ Setup

1. Clone the repo:

```bash
git clone https://github.com/DevMohammad-SA/cli-cohere-chatbot.git
cd cli-cohere-chatbot
```

2. Create a `.env` file:

```env
API_KEY=your_cohere_api_key_here
```

3. Run it:

```bash
python cohere_chat.py
```

---

## 💬 Usage

```bash
🧠 Welcome to your Terminal AI Assistant!
Type your prompts below and get instant answers powered by Cohere.

💡 Pro tips:
 - Type '.quit' anytime to exit
 - Designed for developers, sysadmins, and curious tinkerers

────────────────────────────────────────────
🗨️  Chat Prompt > How do I restart systemd services?
🤖 Response:
You can restart a service using: `sudo systemctl restart <service-name>`
```

---

## 👨‍💻 Developer

Made with ❤️ by **Mohammad Albuainain**  
Twitter: [@DevMohammad_SA]


---

## 🛡️ License

MIT License. Use it, fork it, mod it.

---

## 📌 Notes

- This is a minimalist wrapper and a fun side project. Not production-hardened.
- You can tweak the `system_message` or add more logic to filter/format replies.

---

Pull requests are welcome. Drop a star if you liked it 🌟

