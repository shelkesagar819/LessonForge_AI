
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def evaluate_lesson(topic, lesson):

    prompt = f"""
    You are a strict educational content evaluator.

    Evaluate the following lesson.

    TOPIC: {topic}

    LESSON:
    {lesson}

    Evaluate on these 6 criteria:
    1. Accuracy
    2. Beginner Friendliness
    3. Clarity
    4. Examples Quality
    5. Completeness
    6. Coherence

    Give each criterion a score out of 10.

    Passing requirements:
    - Every criterion must score at least 8/10.
    - Total score must be at least 48/60.

    Return your evaluation in this format:

    QUALITY SCORE: X/60

    ACCURACY: X/10
    BEGINNER FRIENDLINESS: X/10
    CLARITY: X/10
    EXAMPLES QUALITY: X/10
    COMPLETENESS: X/10
    COHERENCE: X/10

    STATUS: PASS or FAIL

    FEEDBACK:
    List specific weaknesses and explain how to improve them.

    If all criteria pass, write:
    "The lesson meets all quality requirements."
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text
