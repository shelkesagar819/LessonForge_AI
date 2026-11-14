
import json
import os
from datetime import datetime


def save_rejection_log(topic, rejection_log):

    os.makedirs("outputs/logs", exist_ok=True)

    file_path = "outputs/logs/rejection_log.json"

    data = []

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

    for log in rejection_log:
        data.append({
            "topic": topic,
            "attempt": log["attempt"],
            "feedback": log["feedback"],
            "timestamp": datetime.now().isoformat()
        })

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
