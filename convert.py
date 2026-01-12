import os

ROOT_DIR = r"D:\Leetcode"   # change only if your path is different

count = 0

for foldername, subfolders, filenames in os.walk(ROOT_DIR):
    for filename in filenames:
        if filename.lower().endswith(".txt"):
            old_path = os.path.join(foldername, filename)
            new_name = filename[:-4] + ".py"
            new_path = os.path.join(foldername, new_name)

            if not os.path.exists(new_path):  # safety check
                os.rename(old_path, new_path)
                count += 1

print(f"✅ Done! Converted {count} files from .txt to .py")
