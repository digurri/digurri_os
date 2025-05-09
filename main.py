# main.py
# module arrange , combine

from emo_log import EmotionLogger
from body_log import BodyConLogger
from datetime import date
import json
import os


def is_already_logged(log_path, record_type, time_of_day=None):
    today = date.today().isoformat()
    if not os.path.exists(log_path):
        return False
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
                if entry.get("type") == record_type and entry.get("date") == today:
                    if time_of_day is None or entry.get("time_of_day") == time_of_day:
                        return True
            except json.JSONDecodeError:
                continue
    return False


def handle_emotion_logging(emotion_logger):
    emotion_logger = EmotionLogger()
    log_path = emotion_logger.log_path

    while True:
        print("\n=== 디구리 감정 기록 시스템 ===")
        print("1. 오늘의 감정 키워드 기록")
        print("2. 감정 루프 기록")
        print("3. 종료")
        choice = input("선택 (1/2/3): ")

        if choice == "1":
            if is_already_logged(log_path, "daily"):
                print("* 이미 오늘의 감정 키워드 기록이 끝났습니다. *")
                continue
            print("\n=== 오늘의 감정 키워드 기록 ===")
            keyword = input("오늘의 감정을 입력하세요: ")
            emotion_logger.log_keyword(keyword)

        elif choice == "2":
            print("\n=== 감정 루프 기록 ===")
            emotion = input("부정적 감정: ")
            cause = input("원인: ")
            resolved_input = input("해결 했나요? (y/n): ").lower()
            resolved = True if resolved_input == "y" else False
            method = input("해결한 방법 (없다면 Enter): ")
            emotion_logger.log_loop(
                emotion=emotion,
                cause=cause,
                resolved=resolved,
                method=method if method else None,
            )

        elif choice == "3":
            print("감정 기록을 종료합니다.")
            break

        else:
            print("유효한 작업 번호를 입력해주세요 (1/2/3).")

def handle_body_logging(body_logger):
# 몸 상태 기록 시스템
    body_logger = BodyConLogger()
    log_path = body_logger.log_path

    while True:
        print("\n=== 디구리 몸 상태 기록 시스템 ===")
        print("1. 몸무게 기록")
        print("2. 아침 컨디션 기록")
        print("3. 종료")
        choice = input("선택 (1/2/3): ")

        if choice == "1":
            time_of_day = input("공복 또는 자기 전 (공복/자기 전): ")
            if is_already_logged(log_path,"weight", "time_of_day"):
                print("* 이미 오늘의 몸무게 기록이 완료되었습니다. *")
                continue
            print("\n=== 몸무게 기록 ===")
            weight = float(input("몸무게를 입력하세요 (kg): "))
            body_logger.log_weight(weight, time_of_day)

        elif choice == "2":
            if is_already_logged(log_path,"morning_condition"):
                print("* 이미 오늘의 아침 컨디션 기록이 완료되었습니다. *")
                continue
            print("\n=== 아침 컨디션 기록 ===")
            swelling = int(input("붓기 정도 (1~5): "))
            fatigue = int(input("피로도 (1~5): "))
            sleep_quality = int(input("수면의 질 (1~5): "))
            body_logger.log_morning_condition(swelling, fatigue, sleep_quality)

        elif choice == "3":
            print("몸 상태 기록을 종료합니다")
            break

        else:
            print("유효한 작업 번호를 입력해주세요 (1/2/3).")

def main():
    emotion_logger = EmotionLogger()
    body_logger = BodyConLogger()

    while True:
        print("\n=== 디구리 기록 시스템 ===")
        print("1. 감정 기록")
        print("2. 몸 상태 기록")
        print("3. 종료")
        choice = input("선택 (1/2/3): ")

        if choice == "1":
            handle_emotion_logging(emotion_logger)
        elif choice == "2":
            handle_body_logging(body_logger)
        elif choice == "3":
            print("디구리를 종료합니다. 오늘도 좋은 하루 되세요!")
            break
        else:
            print("유효한 작업 번호를 입력해주세요 (1/2/3).")


if __name__ == "__main__":
    main()
