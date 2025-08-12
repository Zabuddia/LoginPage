from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from . import main_bp

@main_bp.route("/")
def index():
    if current_user.is_authenticated:
        # Route to appropriate dashboard based on role
        return redirect(url_for("admin.dashboard" if current_user.is_admin() else "main.dashboard"))
    return redirect(url_for("auth.login"))

@main_bp.route("/dashboard")
@login_required
def dashboard():
    # Normal user dashboard
    return render_template("dashboard.html")