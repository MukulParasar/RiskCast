# RiskCast: AI-Powered Disaster Forecasting & Planning Engine

Welcome to **RiskCast**, where data meets preparedness. This interactive README invites you to explore, poke around, and build upon a system designed to help communities anticipate and respond to flooding events.

---

## 🎯 What Is RiskCast?

RiskCast is an AI-driven forecasting and planning engine that blends geographical insight, environmental signals, and machine learning into a single decision-support system. It detects flood‑risk zones and recommends practical mitigation strategies.

Think of it as your digital lookout tower that never sleeps.

---

## ✨ Core Features

* **Flood Risk Prediction** using ML models trained on real-world environmental and geographical data.
* **Mitigation Strategy Engine** that generates tailored, data-backed action recommendations.
* **Interactive Angular Frontend** for visualizing maps, heat zones, and suggestions.
* **Robust .NET Core Backend** that ferries data between the UI and ML model.
* **Modular Architecture** enabling future expansion to hurricanes, wildfires, or other hazards.

---

## 🧩 Technology Stack

* **Frontend:** Angular
* **Backend:** .NET Core (C#)
* **Machine Learning:** Python scripts

---

## 🚀 Getting Started

### ✅ Prerequisites

* Node.js v14+
* .NET SDK
* Python 3.x
* npm & pip

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MukulParasar/RiskCast.git
cd RiskCast
```

### 2. Start the Backend

```bash
cd Backend
dotnet restore
dotnet run
```

### 3. Fire Up the Frontend

```bash
cd ../Frontend
npm install
ng serve
```

Your UI awaits at **[http://localhost:4200](http://localhost:4200)**.

### 4. Prep the Machine Learning Model

```bash
cd ../MLModel
pip install -r requirements.txt
python main.py
```

---

## 🏗️ Architecture & Workflow

* **Angular Frontend:** Handles map displays, forms, and user flows.
* **.NET Core Backend:** Acts as the conductor orchestrating calls between UI and ML model.
* **Python ML Engine:** Processes datasets, runs predictions, emits risk scores.

The workflow pirouettes like this:

1. User provides input or navigates the map.
2. Frontend sends the request to backend.
3. Backend forwards it to Python model.
4. Prediction returns and flows back to frontend.
5. User sees risk zones and recommended actions.

---

## 📁 Project Structure

```
RiskCast/
│
├── Frontend/        # Angular application
├── Backend/         # .NET Core API
└── MLModel/        # Python ML scripts
```

---

## 🧭 Usage Guide

* Start the backend first.
* Then run the Angular app.
* Navigate the dashboard to explore risk zones.
* Watch predictions and mitigation insights bloom in real time.

---

## 🤝 Contributing

Pull requests, feature ideas, optimizations... all welcome.

---

## 📜 License

This project is currently not licensed. Please add a license before public distribution.

---

## 📬 Contact

**Your Name**
**[mukulparasharsharma@gmail.com](mailto:mukulparasharsharma@gmail.com)**

Ready to explore? Scroll, click, run, and experiment. RiskCast is your canvas.
