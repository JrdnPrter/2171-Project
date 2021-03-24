"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm
from app.models import EmployeeProfile
from werkzeug.security import check_password_hash
from .forms import BookingForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="TRK Party Rentals")

@app.route('/booking/', methods=['GET', 'POST'])
@login_required
def createBooking():
    myForm = BookingForm()
    
    if request.method == 'POST':
        
        if myForm.validate_on_submit():

            clientName = myForm.clientName.data
            contact = myForm.contact.data
            eventDate = myForm.eventDate.data
            address = myForm.address.data
            equipment = myForm.equipment.data

            

        flash('Booking created Successfully.', 'success')
        return redirect(url_for('home'))    

    return render_template('booking.html', form = myForm)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("User Logged Out")
    return redirect(url_for('home'))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field
        if form.validate_on_submit:
            username = form.username.data
            password = form.password.data

            user = EmployeeProfile.query.filter_by(username=username).first()
            if user is not None and check_password_hash(user.password,password):
            
                login_user(user)
                flash("Logged in sucessfully.", 'success')
                return redirect(url_for("secure_page"))
            else:
                flash("Incorrect username or password", "failure")  # they should be redirected to a secure-page route instead
    return render_template("login.html", form=form)   

@login_manager.user_loader
def load_user(id):
    return EmployeeProfile.query.get(int(id))

@app.route('/secure-page/')
@login_required
def secure_page():
    if current_user.is_authenticated:
        return render_template('secure-page.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
