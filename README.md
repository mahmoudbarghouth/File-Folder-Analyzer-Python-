# File-Folder-Analyzer-Python-
This Python script scans a given directory and prints a detailed report of:

- ✅ All files and their sizes
- ✅ All folders
- ✅ Total number of files and folders
- ✅ Data stored in lists of dictionaries for further use

---

##  Features

- Detects files and folders in a given path
- Measures file sizes (in KB)
- Stores results in dictionaries for easy export
- Clearly separates files and folders
- Handles both relative and absolute paths

---

##  How it works

1. You provide a path (configured in the `path` variable)
2. It lists all items in that directory
3. It checks each item:
   - If file → gets size using `os.path.getsize()`
   - If folder → counts it (size is symbolic)
4. Results are printed and saved in lists:
   - `files = [{filename: size}, ...]`
   - `folders = [{foldername: size}, ...]`
