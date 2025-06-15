<!-- Banner Section -->
<p align="center">
  <img src="https://img.freepik.com/free-vector/emotional-intelligence-concept-illustration_114360-7063.jpg?w=826" width="500"/>
</p>

<h1 align="center">🌈 Mood Tracker App</h1>
<p align="center">
  A beautifully simple mood-tracking app built with Streamlit. Track emotions, explore trends, and receive AI-powered insights.
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Anamicca23/mood-tracker-app-streamlit?style=flat-square&color=brightgreen" />
  <img src="https://img.shields.io/github/forks/Anamicca23/mood-tracker-app-streamlit?style=flat-square&color=blue" />
  <img src="https://img.shields.io/github/license/Anamicca23/mood-tracker-app-streamlit?style=flat-square&color=orange" />
</p>


<p align="center">
  <p align="center">
    Built with tech-stack like:</br>
    </br>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-ff4b4b?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-SQLite-lightblue?logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Visualization-Matplotlib%20%7C%20Plotly-orange?logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI-Integrated-green?logo=openai" />
</p></p>


## ✨ Features

- ✅ **Log Daily Mood**: Use intuitive sliders for mood, sleep, energy, and productivity levels
- 📊 **Trend Visualization**: View line charts, radar plots, and compare metrics over time
- 🧠 **AI Insights (Optional)**: GPT-powered emotional summaries and well-being suggestions
- 🗂 **History Log**: Browse, delete, or review past entries stored locally in SQLite
- 💻 **Modern UI**: Clean, interactive frontend with fast reactivity using Streamlit
- 🔒 **Privacy Focused**: All data is stored locally (no cloud by default)

---

## 📁 Project Structure

```bash
📦 mood-tracker-app-streamlit/
├── main.py                  # App Entry Point
├── requirements.txt         # Dependencies
├── modules/
│   ├── db.py                # Database Operations (Insert, Read, Delete)
│   ├── visualization.py     # Charts (Line, Radar, Bar)
│   └── guidances.py         # OpenAI Feedback Integration
├── databases/
│   └── mental_health.db     # SQLite Database File
├── assets/                  # Optional: Store screenshots, logos, etc.
└── .github/workflows/
    └── deploy.yml           # CI/CD for deployment
````

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Anamicca23/mood-tracker-app-streamlit.git
cd mood-tracker-app-streamlit
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Launch the App

```bash
streamlit run main.py
```

📌 *Note: Make sure your Python version is 3.9 or above for compatibility.*

---

## 🌐 Web UI Preview

<p align="center">
  <img src="https://user-images.githubusercontent.com/placeholder/mood-ui-preview.png" width="80%" alt="Mood Tracker UI"/>
  <br />
  <i>Minimal, clean, and accessible interface designed for everyday use.</i>
</p>

---

## ☁️ Deployment

This app is **production-ready** and easy to deploy.

* 📦 **Docker** support with pre-configured `Dockerfile`
* 🔄 **GitHub Actions** (`deploy.yml`) for automatic cloud deployment
* ☁️ **Suggested Platforms**:

  * Google Cloud Run
  * Streamlit Community Cloud
  * Heroku

---

## 🧠 Powered by AI 

Leverage **OpenAI GPT** to generate personalized feedback based on your mood history.

### How to Enable:

1. Get your API key: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Add it to a `.env` file or directly inside `guidances.py`

   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```
3. Enable "Guidance" in the sidebar and enjoy actionable insights.

🔐 *Your key is never shared and used only for this session.*

---

## 📅 Upcoming Features

| Feature                                           | Status                 |
| ------------------------------------------------- | ---------------------- |
| 🧑‍🤝‍🧑 Multi-user support                       | 🛠 In Progress         |
| 📲 Mobile-responsive UI                           | ✅ Done (via Streamlit) |
| 📄 Mood export (PDF/CSV)                          | Planned                |
| ⏰ Daily email reminders                           | Planned                |
| 🧘‍♀️ Integrate with wellness APIs (e.g., Fitbit) | Researching            |

---

## 📚 Use Cases

* 📝 **Self-reflection**: Log your emotions daily and look for patterns
* 🧪 **Mental Health Research**: Analyze trends for personal insights or academic study
* 👨‍⚕️ **Therapy Support Tool**: Share visual history with your counselor
* 🧘‍♀️ **Mindfulness Companion**: Combine mood logs with meditation journals

---

## 🤝 Contributing

Contributions are welcome! Here’s how:

1. 🌱 Fork the repo
2. 🚧 Create a feature branch
3. 💬 Submit a Pull Request

```bash
git checkout -b feature/yourFeature
git commit -m "Add your awesome feature"
git push origin feature/yourFeature
```

---

## 👩‍💻 Author

**Anamika Kumari**
📬 [GitHub](https://github.com/Anamicca23) 
• ✨ Passionate about mental wellness + open source

---

<p align="center">
  💚 Made with mindfulness to help you track, reflect, and thrive 💚
</p>

<p align="center">
  <a href="#-mood-tracker-app">
    <img src="https://img.shields.io/badge/⬆️%20Back%20to%20Top-blue?style=for-the-badge" alt="Back to Top" />
  </a>
</p>
