# Memo App

This is a simple Flask-based memo application that allows users to view, create, and edit a single memo. It uses SQLite as the database via SQLAlchemy, and Bulma CSS for basic styling.

## Features

- View all memos sorted by title
- Create a new memo (with default title/body)
- Edit existing memos
- Persistent storage via SQLite and SQLAlchemy ORM

## Tech Stack

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Bulma CSS (via CDN)

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/memo_app.git
cd memo_app
```

2. **Create virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python memo_edit_app.py
```

5. **Access in browser**

Open `http://localhost:5000` in your browser.

## Directory Structure

```
memo_app/
├── memo_edit_app.py         # Main Flask application
├── templates/
│   ├── base.html            # Base layout
│   ├── list.html            # Memo list page
│   └── memo.html            # Memo editing page
└── requirements.txt         # Python dependencies
```

## 📌 Notes

- Memos are stored in a SQLite database (`sqlite:///memo.db`).
- The app always shows one "CREATE" item to simulate new memo creation.

## 🔐 What to exclude from GitHub?

- **Virtual environment directory** (`venv/`): Add this to `.gitignore`.
- **`.env` files or secrets** (not used here, but if you add any secret key or DB credentials later, hide them).
- **Database files** (`*.db`) if you want a clean repo without local data.

```
venv/
__pycache__/
*.pyc
*.db
.env
```

## 💡 To Do

- Add user authentication
- Enable memo deletion
- Improve UI with better styles or different framework (e.g., Tailwind, Bootstrap)

## License

MIT
