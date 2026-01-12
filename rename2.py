import os
import requests
import time

ROOT_DIR = r"D:\Leetcode"

API_URL = "https://leetcode.com/api/problems/all/"

def fetch_problem_map():
    print("Fetching LeetCode problem list...")
    r = requests.get(API_URL, timeout=20)
    r.raise_for_status()
    data = r.json()
    mp = {}
    for q in data["stat_status_pairs"]:
        mp[str(q["stat"]["frontend_question_id"])] = q["stat"]["question__title"]
    return mp

def clean_title(title):
    return (
        title.replace(" ", "-")
        .replace("'", "")
        .replace(",", "")
        .replace(":", "")
        .replace("(", "")
        .replace(")", "")
    )

problem_map = fetch_problem_map()

renamed = 0
skipped = 0
failed = 0

for name in os.listdir(ROOT_DIR):
    folder_path = os.path.join(ROOT_DIR, name)

    if not os.path.isdir(folder_path):
        continue

    # already renamed folders will not be pure numbers
    if not name.isdigit():
        skipped += 1
        continue

    title = problem_map.get(name)

    if not title:
        print(f"❌ Title not found for {name}")
        failed += 1
        continue

    new_name = f"{int(name):04d}-{clean_title(title)}"
    new_path = os.path.join(ROOT_DIR, new_name)

    try:
        if not os.path.exists(new_path):
            os.rename(folder_path, new_path)
            print(f"✅ {name} → {new_name}")
            renamed += 1
        else:
            skipped += 1
    except Exception as e:
        print(f"⚠️ Failed for {name}: {e}")
        failed += 1

    time.sleep(0.05)  # small delay

print("\n===== DONE =====")
print("Renamed :", renamed)
print("Skipped :", skipped)
print("Failed  :", failed)
