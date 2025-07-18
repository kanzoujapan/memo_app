# Memo App 📝

A simple memo application built with Flask and SQLAlchemy.  
You can create, view, and edit memos via a web interface.

---

## 🧰 Technologies Used

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (`instance/memo_edit.sqlite`)

---

## 🚀 Setup Instructions

1. Create and activate a virtual environment:

```bash
python3 -m venv memo_env
source memo_env/bin/activate  # On Windows: memo_env\Scripts\activate
```

2. Install required packages:

```bash
pip install flask sqlalchemy
```

3. Run the Flask application:

```bash
export FLASK_APP=memo_edit_app.py    # macOS / Linux
# or
set FLASK_APP=memo_edit_app.py       # Windows

flask run
```

---

## 📁 Project Structure

```
memo_app/
├── memo_edit_app.py         # Main Flask application
├── templates/
│   ├── base.html            # Base layout template
│   ├── list.html            # Memo list page
│   └── memo.html            # Memo editing page
├── instance/
│   └── memo_edit.sqlite     # SQLite database (ignored by Git)
├── memo_env/                # Virtual environment (ignored by Git)
├── .gitignore
└── README.md
```

---

## 📌 Files/Folders Ignored by Git (`.gitignore`)

The following are excluded from Git tracking:

- `.DS_Store`: macOS system metadata file
- `memo_env/`: Python virtual environment
- `instance/`: Contains the database and app-specific data

---

## 💡 Notes

- `requirements.txt` is not used. Dependencies must be installed manually.
- If the database file is missing, it's recommended to implement automatic creation on first access (ask if you'd like help with this feature).

---

## 📜 License

This project is licensed under the MIT License (add details as needed).

---