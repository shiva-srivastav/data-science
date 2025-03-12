**Section 1: File Handling in Python**

## Topic 1: File Operations in Python

### Introduction
File handling in Python allows users to create, read, write, and manipulate files easily. Python provides built-in functions to handle file operations using the `open()` function.

### File Operations
The major operations that can be performed on a file include:
1. **Opening a File** - `open(filename, mode)`
2. **Reading a File** - `read()`, `readline()`, `readlines()`
3. **Writing to a File** - `write()`, `writelines()`
4. **Appending to a File** - `append()`
5. **Closing a File** - `close()`

### File Modes
| Mode | Description |
|------|-------------|
| `'r'` | Read mode (default) |
| `'w'` | Write mode (overwrites existing content) |
| `'a'` | Append mode (adds content to existing file) |
| `'x'` | Exclusive creation mode (fails if file exists) |
| `'b'` | Binary mode |
| `'t'` | Text mode (default) |

### Example: Reading and Writing to a File
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python File Handling!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Mermaid Diagram
```mermaid
graph TD;
    A[Open File] -->|Read| B[Read Operations];
    A -->|Write| C[Write Operations];
    A -->|Append| D[Append Operations];
    A -->|Close| E[Close File];
```
