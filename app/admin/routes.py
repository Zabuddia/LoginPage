from flask import render_template, abort
from flask_login import login_required, current_user
from . import admin_bp

def admin_required(view_func):
    @login_required
    def wrapper(*args, **kwargs):
        if not current_user.is_admin():
            abort(403)
        return view_func(*args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper

@admin_bp.route("/dashboard")
@admin_required
def dashboard():
    # Put admin tools here (manage users, view logs, etc.)
    return render_template("admin_dashboard.html")