# main.py
# module arrange , combine

from emo_log import EmotionLogger
from datetime import date
import json
import os


def keyword_already_logged(log_path):
    today = date.today().isoformat()
    if not os.path.exists(log_path):
        return False
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
                if entry.get("type") == "daily" and entry.get("date") == today:
                    return True
            except json.JSONDecodeError:
                continue
    return False


def main():
    logger = EmotionLogger()
    log_path = logger.log_path

    while True:
        print("\n=== 디구리 감정 기록 시스템 ===")
        print("1. 오늘의 감정 키워드 기록")
        print("2. 감정 루프 기록")
        print("3. 종료")
        choice = input("선택 (1/2/3): ")

        if choice == "1":
            if keyword_already_logged(log_path):
                print("* 이미 오늘의 감정 키워드 기록이 끝났습니다. *")
                continue
            print("\n=== 오늘의 감정 키워드 기록 ===")
            keyword = input("오늘의 감정을 입력하세요: ")
            logger.log_keyword(keyword)

        elif choice == "2":
            print("\n=== 감정 루프 기록 ===")
            emotion = input("부정적 감정: ")
            cause = input("원인: ")
            resolved_input = input("해결 했나요? (y/n): ").lower()
            resolved = True if resolved_input == "y" else False
            method = input("해결한 방법 (없다면 Enter): ")
            logger.log_loop(
                emotion=emotion,
                cause=cause,
                resolved=resolved,
                method=method if method else None,
            )

        elif choice == "3":
            print("디구리를 종료합니다. 내일 또 만나요 :)")
            break

        else:
            print("유효한 작업 번호를 입력해주세요 (1/2/3).")


if __name__ == "__main__":
    main()
