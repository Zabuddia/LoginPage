import os
from dotenv import load_dotenv

# Load .env early so env vars exist before Config is evaluated
load_dotenv()

class Config:
    # Secrets/settings pulled from environment
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///app.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False