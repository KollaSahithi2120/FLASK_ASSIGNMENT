from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db, bcrypt
from app.models import User, Role
from flask_login import login_user, current_user, logout_user, login_required

# Blueprint registration
main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role_name = request.form.get('role')

        # Check if the email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already registered. Please use a different email.', 'danger')
            return redirect(url_for('main.register'))

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        role = Role.query.filter_by(name=role_name).first()
        
        if not role:
            flash('Role not found.', 'danger')
            return redirect(url_for('main.register'))

        # Create and add the new user
        user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(user)
        db.session.commit()

        flash('User registered successfully!', 'success')
        return redirect(url_for('main.login'))

    roles = Role.query.all()
    users = User.query.all()  # Get all users to display in the table
    return render_template('register.html', roles=roles, users=users)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login unsuccessful. Check email and password.', 'danger')

    users = User.query.all()  # Get all users to display in the table
    return render_template('login.html', users=users)

@main.route('/dashboard')
@login_required
def dashboard():
    # Log the role for debugging
    print(f"Logged in user: {current_user.username}, Role: {current_user.role.name}")
    
    # Redirect only admins to the admin dashboard; all other roles go to user dashboard
    if current_user.role.name.lower() == 'admin':
        return redirect(url_for('main.admin_dashboard'))
    else:
        return redirect(url_for('main.user_dashboard'))

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/admin-dashboard')
@login_required
def admin_dashboard():
    # Ensure only admin has access to this route
    if current_user.role.name.lower() != 'admin':
        flash('You do not have permission to access the admin dashboard.', 'danger')
        return render_template('user_dashboard.html')
    return render_template('admin_dashboard.html')  # Render the admin dashboard with the iframe

@main.route('/user-dashboard')
@login_required
def user_dashboard():
    # Render the user dashboard for non-admin roles
    return render_template('user_dashboard.html')

@main.route('/view-users')
@login_required
def view_users():
    # Ensure only admin can view users
    if current_user.role.name.lower() != 'admin':
        flash('You do not have permission to view users.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    users = User.query.all()
    return render_template('view_users.html', users=users)
