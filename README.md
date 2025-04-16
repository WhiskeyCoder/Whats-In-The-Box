# Whats-In-The-Box

A script with the sole purpose of listing every file in a directory and saving those names to a `file_list.txt` file. Why? Because sometimes you just need a list. No questions asked.

---

## 🤔 What It Does

- Checks if a directory exists.
- If it exists, writes all file names from that directory into `file_list.txt`.
- That's it. Seriously.

---

## 📂 Example Use Case

You’ve got a giant folder of files and you want to remember what’s inside without actually opening it. Perfect time for this pointless lil’ script.

---

## 🧠 Requirements

- Python 3
- A folder full of stuff you want to list

---

## 🔧 Usage

Update the `directory` variable to the path you want to scan:

```python
directory = "C:\\YOUR_FOLDER"
```

Then run:

```bash
python whats_in_the_box.py
```

You’ll get a `file_list.txt` in the same folder as the script, containing one filename per line.

---

## 📜 Script

```python
import os
import sys

directory = "C:\\YOU_FOLDER"
if not os.path.exists(directory):
    print("Directory does not exist")
    sys.exit(1)

file_list = open("file_list.txt", "w")
for file in os.listdir(directory):
    file_list.write(file + "\n")

file_list.close()
```

---

## 🧃 Why This Exists

Because you once needed it at 3am, probably with a slice of cold pizza in your hand and no patience left. And now you have it. You're welcome. 🍕

---

## 🪪 License

MIT. Do with it what you will — list things responsibly.


