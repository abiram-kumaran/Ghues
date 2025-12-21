from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        GA = request.form.get("GA")
        password = request.form.get("password")

        # Ensure GA exists and password is correct
        user = User.query.filter_by(GA=GA).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Please try again.', category='error')
        else:
            flash('GA number not found. Please check your details.', category='error')

    return render_template("login.html", user=current_user)

@auth.route("/register", methods=['GET', 'POST'])  # Updated route to `/register`
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        GA = request.form.get("GA")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # Predefined valid GA numbers and emails
        GA_list = [
            "18GA112", "21GA106", "23GA129", "20GA106", "11GA118", "23GA013",
            "23GA169", "23GA144", "15GA117", "12GA085", "23GA171", "21GA129",
            "24GA168", "23GA217", "11GA173", "23GA104", "17GA141", "13GA035",
            "12GA248", "11GA047", "11GA303", "18GA056", "19GA036", "11GA010",
            "11GA063", "20GA078", "19GA112", "23GA121", "23GA128", "11GA200",
            "23GA125", "11GA294", "21GA168", "12GA246", "18GA062", "17GA200",
            "23GA024", "18GA040", "11GA012"
        ]
        email_list = [
            "flamesraft@gmail.com", "abhidhyasri5@gmail.com", "abiram.kumaran@gmail.com",
            "amareshgamer2203@gmail.com", "chaarya.rangasamy@gmail.com", "darshxx2007@gmail.com",
            "dhakshindhakshin.v@gmail.com", "dheshnaashri@gmail.com", "yeoh7155@gmail.com",
            "gvkabiylesh@gmail.com", "harikumaran1106@gmail.com", "harshyamaha@gmail.com",
            "hashwittha2007@gmail.com", "ishaklathif840@gmail.com", "ishwaryaaravikumar2007@gmail.com",
            "jeshnasree08@gmail.com", "jovithajo30@gmail.com", "jeffymn07@gmail.com",
            "midhuna338@gmail.com", "sksnehusasi@gmail.com", "vithyasuka@gmail.com",
            "keshavonnet@gmail.com", "srividhyaprakash21@gmail.com", "praneshnirmala@gmail.com",
            "jarvis62393@gmail.com", "priyankapoongodi1010@gmail.com", "raghavi3004@gmail.com",
            "rila2625@gmail.com", "rithanya0128@gmail.com", "rithikbalaji7@gmail.com",
            "kabilesh85852@gmail.com", "shabhariraam2@gmail.com", "dharshanvidhya1@gmail.com",
            "varshanss5707@gmail.com", "sivaguru.n888@gmail.com", "thevyasgbtunique@gmail.com",
            "uvashrirsivakumar@gmail.com", "visahanvenkat07@gmail.com", "yogesh2468@gmail.com"
        ]

        # Validation checks
        email_exists = User.query.filter_by(email=email).first()
        GA_exists = User.query.filter_by(GA=GA).first()

        if GA not in GA_list:
            flash('GA number is not authorized to create an account.', category='error')
        elif email_exists:
            flash('This email is already registered.', category='error')
        elif email not in email_list:
            flash('This email cannot be used to create an account.', category='error')
        elif GA_exists:
            flash('This GA number is already registered.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash('Invalid email address.', category='error')
        else:
            # Create new user
            new_user = User(
                email=email,
                GA=GA,
                username=username,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully! Welcome!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for("views.home"))
