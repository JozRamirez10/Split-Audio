# Split Audio API

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PM2](https://img.shields.io/badge/PM2-Process_Manager-2B037A?style=for-the-badge&logo=pm2&logoColor=white)

An advanced, AI-powered audio processing microservice designed to isolate and separate specific musical stems from mixed audio files. This API combines robust on-premise machine learning models for processing vocals, drums, winds, and standard tracks, while seamlessly integrating with the **Music.ai API** for specialized, high-fidelity guitar separation (by role and type). Its fully decoupled architecture makes it an ideal engine for any ecosystem requiring professional-grade audio manipulation.

## 🏗️ Architecture & Tech Stack

-   **Framework:** FastAPI (Python)
-   **AI & Audio Processing:** PyTorch, ONNX Runtime, Audio-Separator, SciPy
-   **Cloud Integrations:** Music.ai SDK
-   **Process Management:** PM2 (Configured for high-memory AI workloads)
-   **Infrastructure:** Docker & Docker Compose (with OS-level audio decoders)
-   **Data Validation:** Pydantic

### 🚀 Key Features
-   **Local AI Stem Separation:** High-quality extraction of vocals, drums, winds, and custom tracks using local PyTorch models.
-   **Music.ai Cloud Processing:** Offloads complex guitar isolation (Guitar Role and Guitar Type) to the Music.ai cloud infrastructure via seamless API integration.
-   **Automated Cleanup Engine:** Dedicated endpoints designed to safely and efficiently delete temporary processed audio files, preventing storage bloat.
-   **Dynamic Docker Builds:** Includes configurable build arguments (`PYTORCH_INSTALL_ARGS`) to let developers choose between lightweight CPU-only images or full GPU-accelerated environments.

---

## 📂 Repository Structure

~~~text
split_audio_api/
├── app/
│   ├── controllers/          # Route handlers (tracks, drums, vocals, guitars, cleanup)
│   ├── core/                 # Configuration, environment variables, and constants
│   ├── enums/                # Enumerations for supported instruments and models
│   ├── models/               # Pydantic schemas for separation payloads
│   ├── services/             # Audio separation logic and Music.ai integrations
│   ├── utils/                # Global error handlers and utilities
│   └── main.py               # FastAPI application entry point
├── logs/                     # Persistent PM2 application logs directory
├── docker-compose.yml        # Multi-container orchestration (with model volumes)
├── Dockerfile                # Multi-stage image build with ffmpeg/libsndfile1
├── ecosystem.config.js       # PM2 configuration (4GB memory limit for AI)
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md
~~~

---

## 🚀 Getting Started

### Prerequisites
-   Python 3.10+
-   **System Packages:** `ffmpeg` and `libsndfile1` (Required for bare-metal executions)
-   Docker & Docker Compose *(For containerized execution)*
-   Node.js & PM2 *(For bare-metal production execution)*
-   **Music.ai API Key:** Required for guitar processing endpoints.

### Environment Setup
This project uses a `.env` file for configuration. Before starting the application, you must create your local environment file:

1. Copy the example file:
   ~~~bash
   cp .env.example .env
   ~~~
2. Open `.env` and configure your directories (`DIR_MODELS`, `TMP_DIR`) and your `MUSIC_AI_API_KEY`.

---

### Installation & Execution

**Option A: Running with Docker (Recommended)**
~~~bash
git clone https://github.com/JozRamirez10/Split-Audio.git
cd Split-Audio

# 1. Create your local environment file
cp .env.example .env

# STOP 🛑: Open the .env file in your editor and configure your Music.ai Key & directories!

# 2. Build and run the container in detached mode
# Note: The docker-compose.yml contains an argument to install the CPU-only version of PyTorch to save space.
docker compose up -d --build
~~~

**Option B: Running in Production with PM2**
~~~bash
git clone https://github.com/JozRamirez10/Split-Audio.git
cd Split-Audio

# 1. Create your local environment file and fill it out
cp .env.example .env

# 2. Create the virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate

# 3. Install PyTorch (Choose CPU or GPU version based on your server)
pip install torch torchvision torchaudio
pip install -r requirements.txt

# 4. Start the application using PM2 (Handles the 4GB RAM limit automatically)
pm2 start ecosystem.config.js
pm2 save
~~~

**Option C: Running locally for Development**
~~~bash
git clone https://github.com/JozRamirez10/Split-Audio.git
cd Split-Audio

# 1. Create your local environment file and fill it out
cp .env.example .env

# 2. Create the virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install torch torchvision torchaudio
pip install -r requirements.txt

# 3. Run the development server with live reload
uvicorn app.main:app --host 0.0.0.0 --port 7002 --reload
~~~

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request.