# Reusable Flask Login System

A minimal, role-based login system for Flask projects.  
Includes:

- User authentication with **Flask-Login**
- Role support (`admin` / `user`)
- CLI-based user creation (no public registration)
- SQLite (default) or any SQLAlchemy-supported database
- Flash messages with custom CSS
- Fully self-contained HTML/CSS (no external CDN)

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone <repo-url> myproject
cd myproject
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Create `.env`

```bash
cp .env.example .env
```

Edit `.env` and set:

```
SECRET_KEY=<generate with: python -c "import secrets; print(secrets.token_hex(32))">
DATABASE_URL=sqlite:///app.sqlite3
FLASK_ENV=development
```

### 3. Run once to create tables

```bash
python run.py
```

Then `Ctrl+C` to stop.

### 4. Create your first user

```bash
# Create an admin
flask --app run.py create-user --username admin@example.com --role admin
# Create a normal user
flask --app run.py create-user --username user@example.com --role user
```

### 5. Start the server

```bash
python run.py
```

- Visit `/auth/login` to log in.
- Admins go to `/admin/dashboard`.
- Users go to `/dashboard`.

---

## 📂 Project Structure

```
app/
  auth/                # Login/logout routes
  admin/               # Admin-only routes
  main/                # Normal user routes
  models.py            # Database models
  config.py            # App configuration
  templates/           # HTML templates
  static/css/style.css # Custom CSS
```

---

## 🛠 CLI Commands

```bash
# Create user
flask --app run.py create-user --username USERNAME --role [user|admin]

# Delete user
flask --app run.py delete-user --username USERNAME

# List all users
flask --app run.py list-users

# Change a user's role
flask --app run.py set-role --username USERNAME --role [user|admin]

# Reset a user's password
flask --app run.py set-password --username USERNAME
```

---

## ⚙️ Configuration

Environment variables (`.env` or server env):

- `SECRET_KEY` – required for sessions & CSRF
- `DATABASE_URL` – SQLAlchemy DB URI (SQLite default)
- `FLASK_ENV` – `development` or `production`

---

## 🔒 Security Notes

- Keep `.env` out of version control (see `.gitignore`).
- Use HTTPS in production (`REMEMBER_COOKIE_SECURE = True`).
- Change the default DB from SQLite for production use.

---
