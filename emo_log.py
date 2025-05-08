# emo_log.py
# 주요 기능 : 감정 루프 경험 기록 & 오늘의 감정 키워드 기록

import os
import json
from datetime import datetime


class EmotionLogger:
    def __init__(self, log_path="logs/emotion.txt"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def log_loop(self, emotion, cause, resolved, method):
        """감정 루프 경험 기록"""
        data = {
            "type": "loop",
            "datetime": datetime.now().isoformat(timespec="minutes"),
            "emotion": emotion,
            "cause": cause,
            "resolved": resolved,
            "method": method,
        }
        self._write(data)

    def log_keyword(self, keyword):
        """오늘의 감정 키워드 기록"""
        data = {
            "type": "daily",
            "date": datetime.now().date().isoformat(),
            "keyword": keyword,
        }
        self._write(data)

    def _write(self, data):
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

        if data.get("type") == "daily":
            print("[ 감정 키워드 기록 완료 ]")
        if data.get("type") == "loop":
            print("[ 감정 루프 기록 완료 ]")
