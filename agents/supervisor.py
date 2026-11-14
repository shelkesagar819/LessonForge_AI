
from agents.generator import generate_lesson
from agents.evaluator import evaluate_lesson


def run_lesson_workflow(topic, level="Beginner", language="English"):

    rejection_log = []
    max_attempts = 3

    lesson = generate_lesson(topic, level, language)

    for attempt in range(1, max_attempts + 1):

        print(f"\nEvaluation Attempt: {attempt}")

        evaluation = evaluate_lesson(topic, lesson)

        print(evaluation)

        if "STATUS: PASS" in evaluation.upper():

            return {
                "lesson": lesson,
                "evaluation": evaluation,
                "attempts": attempt,
                "status": "PASS",
                "rejection_log": rejection_log
            }

        rejection_log.append({
            "attempt": attempt,
            "feedback": evaluation
        })

        if attempt < max_attempts:

            improvement_prompt = f"""
            Improve the following lesson.

            Topic: {topic}
            Level: {level}
            Language: {language}

            Previous Lesson:
            {lesson}

            Evaluator Feedback:
            {evaluation}

            Fix all identified weaknesses.
            Create a better and more complete lesson.
            """

            from dotenv import load_dotenv
            import os
            from google import genai

            load_dotenv()

            client = genai.Client(
                api_key=os.getenv("GEMINI_API_KEY")
            )

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=improvement_prompt
            )

            lesson = response.text

    return {
        "lesson": lesson,
        "evaluation": evaluation,
        "attempts": max_attempts,
        "status": "FAIL",
        "rejection_log": rejection_log
    }
