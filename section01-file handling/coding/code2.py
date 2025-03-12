from pathlib import Path

file_path =Path("example.txt")

if file_path.exists():
    print("file exists")

print(file_path.resolve())