# body_log.py
# 주요 기능: 몸의 상태를 기록하는 기능을 제공하는 모듈

import os
import json
from datetime import datetime

class BodyConLogger:
    def __init__(self, log_path="logs/body.txt"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def log_weight(self, weight, time_of_day):
        """몸무게 기록 (공복/자기 전 선택)"""
        if not isinstance(weight, (int, float)):
            raise ValueError("weight는 숫자여야 합니다.")
        if time_of_day not in ["공복", "자기 전"]:
            raise ValueError("time_of_day는 '공복' 또는 '자기 전' 중 하나여야 합니다.")

        data = {
            "type": "weight",
            "date": datetime.now().date().isoformat(),
            "weight": weight,
            "time_of_day": time_of_day
        }
        self._write(data)

    def log_morning_condition(self, swelling, fatigue, sleep_quality):
        """아침 컨디션 기록"""
        for value, name in zip([swelling, fatigue, sleep_quality], ["붓기", "피로도", "수면의 질"]):
            if not isinstance(value, int) or not (1 <= value <= 5):
                raise ValueError(f"{name}는 1~5 사이의 정수여야 합니다.")

        data = {
            "type": "morning_condition",
            "date": datetime.now().date().isoformat(),
            "swelling": swelling,
            "fatigue": fatigue,
            "sleep_quality": sleep_quality,
        }
        self._write(data)

    def _write(self, data):
        """데이터를 파일에 기록"""
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
        print(f"[ {data['type']} 기록 완료 ]")