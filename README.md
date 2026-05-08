# 📂 Smart File Launcher (Python Productivity Tool)

A Python-based productivity tool that allows you to quickly **search and open files** from your desktop using simple text commands.

Instead of manually browsing folders, you can instantly launch files by typing part of the file name.

---

# 🚀 Features

✔ Search files using partial names
✔ Automatically opens matching files
✔ Fast desktop file access
✔ Beginner-friendly automation script
✔ Lightweight and simple to use

---

# 🛠 Technologies Used

* Python
* OS module

---

# 📂 Project Structure

```id="op1"
smart-file-launcher
│
├── main.py
└── README.md
```

👉 Rename your file to **main.py** for a clean structure.

---

# ⚙️ Setup

1️⃣ Install Python 3.x

2️⃣ Update desktop path in code:

```python id="op2"
desktop_path = "C:/Users/ravir/OneDrive/Desktop"
```

Set this to the folder where your files are stored.

---

# ▶️ How to Run

```bash id="op3"
git clone https://github.com/ravigautam7739/smart-file-launcher.git
cd smart-file-launcher
python main.py
```

---

# 🧠 How It Works

1. User enters file name or keyword
2. Program scans files inside selected folder
3. Checks if keyword matches any file name

### 📌 Logic:

* Match found → File opens automatically
* No match → "File not found" message shown

4. Program runs continuously until:

```id="op4"
exit
```

is entered.

---

# 💻 Example Output

```id="op5"
Enter file name: resume

Opening → resume.pdf
```

OR

```id="op6"
Enter file name: project

Opening → python_project.docx
```

---

# 🎯 Use Cases

* Fast file access
* Productivity automation
* Quick desktop launcher
* Office workflow improvement
* Beginner Python project

---

# ⚠️ Notes

* Works on Windows (`os.startfile`)
* Searches only inside selected folder
* Partial matching may open first matching file only

---

# 🔮 Future Improvements

* Voice-based file opening
* Search multiple folders
* GUI interface
* Open apps and folders
* Fuzzy search support

---

# ⭐ Support

If you found this project useful, give it a **star ⭐**.

---

# 📱 Follow for More Projects

I regularly share **Python, AI, and automation projects**.

Stay tuned 🚀
