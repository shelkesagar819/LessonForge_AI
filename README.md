# 📚 LessonForge AI
### Self-Evaluating Lesson Content Generator

LessonForge AI is an AI-powered application that generates educational lesson content and evaluates its quality using a predefined rubric. It improves lessons through an iterative feedback loop to produce clear, accurate, and beginner-friendly learning material.

## 🚀 Features

- AI-powered lesson generation
- Multiple difficulty levels: Beginner, Intermediate, Advanced
- Multi-language support: English, Hindi, Marathi
- Automated lesson evaluation using a 6-criteria rubric
- Quality scoring dashboard
- Iterative lesson improvement workflow
- Rejection and feedback logging
- Download generated lesson content
- Interactive Streamlit user interface

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- JSON
- python-dotenv

## 📂 Project Structure

```text
LessonForge_AI/
│
├── agents/
│   ├── generator.py
│   ├── evaluator.py
│   └── supervisor.py
│
├── utils/
│   └── logger.py
│
├── outputs/
│   ├── lessons/
│   └── logs/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shelkesagar819/LessonForge_AI.git
cd LessonForge_AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Gemini API key.

**Note:** Never upload your API key to GitHub.

## ▶️ Usage

Run the application:

```bash
streamlit run app.py
```

1. Enter a lesson topic.
2. Select the difficulty level.
3. Choose the output language.
4. Click **Generate Lesson**.
5. Review the generated lesson and evaluation score.
6. Explore the feedback and rejection history.
7. Download the final lesson.

## 🧠 Evaluation Criteria

The generated lesson is evaluated based on:

- Accuracy
- Beginner Friendliness
- Clarity
- Examples
- Completeness
- Coherence

The workflow evaluates the generated lesson and attempts to improve it based on feedback, up to a maximum of three evaluation attempts.

## 🎯 Project Objective

The objective of LessonForge AI is to automate educational content generation while maintaining quality through AI-based evaluation and feedback-driven improvement.

## 👨‍💻 Author

**Sagar Shelke**

- [GitHub](https://github.com/shelkesagar819)
- [LessonForge AI Repository](https://github.com/shelkesagar819/LessonForge_AI)
