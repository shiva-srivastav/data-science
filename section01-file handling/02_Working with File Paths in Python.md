## Topic 2: Working with File Paths in Python

### Introduction
Handling file paths correctly is essential for managing files across different operating systems. Python provides the `os` and `pathlib` modules for working with file paths effectively.

### Using `os` Module
- `os.path.exists(path)`: Check if a file exists
- `os.path.join(path1, path2)`: Join paths in a cross-platform way
- `os.path.dirname(path)`: Get the directory name from a path
- `os.path.abspath(path)`: Get the absolute path

### Using `pathlib` Module (Recommended)
Python 3.4+ introduced `pathlib` for an object-oriented approach to file paths.
```python
from pathlib import Path

# Defining a file path
file_path = Path("example.txt")

# Checking if the file exists
if file_path.exists():
    print("File exists")

# Getting absolute path
print(file_path.resolve())
```

### Mermaid Diagram
```mermaid
graph TD;
    A[File Path] -->|Check Exists| B[File Exists?];
    A -->|Get Absolute Path| C[Absolute Path];
    A -->|Join Paths| D[Combined Path];
```

This section provides a comprehensive guide to file handling and file paths in Python.

