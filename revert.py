import os
import re

ROOT_DIR = r"D:\Learning\Leetcode"   # change only if needed

reverted = 0
skipped = 0

for name in os.listdir(ROOT_DIR):
    old_path = os.path.join(ROOT_DIR, name)

    if not os.path.isdir(old_path):
        continue

    # match: 0001-Title-Here
    match = re.match(r"^(\d+)-", name)

    if not match:
        skipped += 1
        continue

    number = match.group(1).lstrip("0") or "0"
    new_path = os.path.join(ROOT_DIR, number)

    if not os.path.exists(new_path):
        os.rename(old_path, new_path)
        print(f"✅ {name} → {number}")
        reverted += 1
    else:
        print(f"⚠️ Folder exists, skipping: {number}")
        skipped += 1

print("\nDONE")
print("Reverted:", reverted)
print("Skipped :", skipped)
