from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
log_path = f"/home/digurri/digurri_dev/logs/{today}.txt"

emotion = input("What's the emotion of today? ")

with open(log_path, "a") as file:
	file.write(emotion + "\n")

print(f"Save Completed : {log_path}")
