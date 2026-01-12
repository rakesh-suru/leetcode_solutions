import os
import requests
import time

ROOT_DIR = r"D:\Learning\Leetcode"

LEETCODE_API = "https://leetcode.com/graphql"

QUERY = """
query getQuestionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
  }
}
"""

# get title by problem number using list API
def get_title_by_number(num):
    url = "https://leetcode.com/api/problems/all/"
    data = requests.get(url).json()

    for q in data["stat_status_pairs"]:
        if str(q["stat"]["frontend_question_id"]) == str(num):
            title = q["stat"]["question__title"]
            return title
    return None


def clean_title(title):
    return title.replace(" ", "-").replace("'", "").replace(",", "").replace(":", "")


renamed = 0
skipped = 0

for name in os.listdir(ROOT_DIR):
    folder_path = os.path.join(ROOT_DIR, name)

    if not os.path.isdir(folder_path):
        continue

    if not name.isdigit():
        skipped += 1
        continue

    qno = int(name)
    title = get_title_by_number(qno)

    if not title:
        print(f"❌ Title not found for {name}")
        skipped += 1
        continue

    new_name = f"{qno:04d}-{clean_title(title)}"
    new_path = os.path.join(ROOT_DIR, new_name)

    if not os.path.exists(new_path):
        os.rename(folder_path, new_path)
        print(f"✅ {name} → {new_name}")
        renamed += 1
    else:
        print(f"⚠️ Already exists: {new_name}")
        skipped += 1

    time.sleep(0.2)  # be gentle to API

print("\nDONE")
print("Renamed:", renamed)
print("Skipped:", skipped)
