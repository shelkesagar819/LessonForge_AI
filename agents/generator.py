
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing in .env file")

client = genai.Client(api_key=api_key)


def generate_lesson(topic, level="Beginner", language="English"):

    prompt = f"""
    You are an expert educational lesson generator.

    Create a high-quality educational lesson.

    Topic: {topic}
    Learning Level: {level}
    Language: {language}

    Follow this structure:

    1. Lesson Title
    2. Learning Objectives
    3. Introduction
    4. Detailed Explanation
    5. Important Concepts
    6. Real-World Examples
    7. Simple Practical Example
    8. Summary
    9. Quiz with 5 Questions
    10. Quiz Answers

    Requirements:
    - Use simple and clear language.
    - Make the lesson beginner-friendly.
    - Include accurate technical information.
    - Explain difficult concepts with examples.
    - Avoid unnecessary information.
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text
