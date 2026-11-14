
import streamlit as st

import re
from utils.logger import save_rejection_log

from agents.generator import generate_lesson
from agents.supervisor import run_lesson_workflow

st.set_page_config(
    page_title="LessonForge AI",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #15102b);
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3 {
    color: #c4b5fd;
}

div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    height: 45px;
    font-weight: bold;
}

div.stButton > button:hover {
    border: 1px solid #a78bfa;
    color: white;
}

textarea, input {
    background-color: #1e293b !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🤖 LessonForge AI")
    st.caption("Your Intelligent Lesson Workspace")

    st.divider()

    st.subheader("Navigation")
    st.button("🏠 Dashboard", use_container_width=True)
    st.button("📝 Lesson Generator", use_container_width=True)
    st.button("📊 Evaluation Results", use_container_width=True)
    st.button("📜 Rejection Logs", use_container_width=True)

    st.divider()

    st.caption("Powered by Agentic AI")

# Main Dashboard
st.title("✨ LessonForge AI")
st.subheader("Self-Evaluating Lesson Content Generator")

st.markdown("""
Generate high-quality educational lessons with AI.
Our intelligent agents generate, evaluate, and improve
lessons automatically.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📚 Create a New Lesson")

    topic = st.text_input(
        "Enter Lesson Topic",
        placeholder="Example: Introduction to RAG"
    )

    level = st.selectbox(
        "Choose Learning Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    language = st.selectbox(
        "Choose Language",
        ["English", "Hindi", "Marathi"]
    )

    generate_btn = st.button(
        "🚀 Generate Lesson",
        use_container_width=True
    )

with col2:
    st.markdown("### 🤖 Agent Workflow")

    st.info("1️⃣ Generator Agent — Creates lesson")
    st.warning("2️⃣ Evaluator Agent — Checks quality")
    st.success("3️⃣ Supervisor Agent — Approves or regenerates")

    st.metric("Quality Score", "Pending")
    st.metric("Evaluation Attempts", "0")




if generate_btn:
    if topic.strip():

        with st.spinner("🤖 AI Agents are working..."):

            try:
                result = run_lesson_workflow(
                    topic=topic,
                    level=level,
                    language=language
                )
                save_rejection_log(
                    topic,
                    result["rejection_log"]
                )

                st.success("Workflow completed!")

                score_match = re.search(
                    r"QUALITY SCORE:\s*(\d+)\s*/\s*60",
                    result["evaluation"],
                    re.IGNORECASE
                )

                quality_score = (
                    int(score_match.group(1))
                    if score_match else 0
                )

                st.markdown("## 📊 Quality Dashboard")

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Quality Score",
                    f"{quality_score}/60"
                )

                col2.metric(
                    "Evaluation Attempts",
                    result["attempts"]
                )

                col3.metric(
                    "Workflow Status",
                    result["status"]
                )

                st.progress(quality_score / 60)

                st.divider()

                st.markdown("## 📖 Final Lesson")
                st.markdown(result["lesson"])

                st.markdown("## 🧠 Evaluator Analysis")

                with st.expander("Detailed Evaluation"):
                    st.markdown(result["evaluation"])

                st.markdown("## 📜 Rejection History")

                if result["rejection_log"]:
                    for log in result["rejection_log"]:
                        with st.expander(
                            f"Attempt {log['attempt']} - Rejected"
                        ):
                            st.markdown(log["feedback"])
                else:
                    st.success("Lesson passed on first attempt!")

                st.download_button(
                    label="📥 Download Final Lesson",
                    data=result["lesson"],
                    file_name="LessonForge_Final_Lesson.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.error("Please enter a lesson topic.")
