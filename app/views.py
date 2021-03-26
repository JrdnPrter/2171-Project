"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, BookingForm, EmployeeForm
from app.models import EmployeeProfile, Booking,EquipmentAssignments
from werkzeug.security import check_password_hash


EMP_TRACK=0
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
    bookForm = BookingForm()
    if request.method == 'POST':
        
        if bookForm.validate_on_submit():
            equipmentList=[]
            clientFName = bookForm.clientFName.data
            clientLName = bookForm.clientLName.data
            contact = bookForm.contact.data
            eventDate = bookForm.eventDate.data
            address = bookForm.address.data
            equipment = bookForm.equipment.data
            for key,value in equipment.items():
                if value == True:
                    equipmentList.append(key)
            booking = Booking(clientFName,clientLName,contact,eventDate,address)
            db.session.add(booking)
            db.session.commit()
            id = db.session.query(Booking).order_by(Booking.id.desc()).first()

            
            for item in equipmentList:
                equip = EquipmentAssignments(bookingid=id.id,eqipmentid =item)
                db.session.add(equip)
            db.session.commit()
            flash('Booking created Successfully.', 'success')

            

        
        return redirect(url_for('home'))    

    return render_template('booking.html', form = bookForm)

@app.route('/newEmployee/', methods=['GET', 'POST'])
@login_required
def newEmployee():
    empForm = EmployeeForm()
    
    if request.method == 'POST':
        
        if empForm.validate_on_submit():

            employeeFName = empForm.employeeFName.data
            employeLName = empForm.employeeLName.data
            dob = empForm.dob.data
            sex = empForm.sex.data   
            pos = empForm.position.data       
            password=empForm.password.data  
            id = trackEmployee()
            employee = EmployeeProfile(employeeFName,employeLName,id,password,pos)
            db.session.add(employee)
            db.session.commit()
        flash('Employee registered successfully. Employee ID is Emp-' + str(id), 'success')
        return redirect(url_for('home'))    

    return render_template('employee.html', form = empForm)

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

@app.route('/viewBooking')
def viewBooking():
    bookings = Booking.query.all()
    return render_template('viewBooking.html',bookings=bookings)

@app.route('/viewBooking/<bookingid>',methods=['GET','POST'])
def editBooking(bookingid):
    bookForm = BookingForm()
    requestedBooking = Booking.query.get(bookingid)
    if request.method =='POST':
            clientFName = bookForm.clientFName.data
            clientLName = bookForm.clientLName.data
            contact = bookForm.contact.data
            eventDate = bookForm.eventDate.data
            address = bookForm.address.data

            requestedBooking.cfname=clientFName
            requestedBooking.clname=clientLName
            requestedBooking.contact=contact
            requestedBooking.event_date=eventDate
            requestedBooking.address=address
            db.session.commit()

            flash("Booking Updated")
            return redirect(url_for('viewBooking'))
    


    bookForm.clientFName.data=requestedBooking.cfname
    bookForm.clientLName.data=requestedBooking.clname
    bookForm.contact.data=requestedBooking.contact
    bookForm.eventDate.data=requestedBooking.event_date
    bookForm.address.data=requestedBooking.address
    return render_template('editBooking.html',bookingid=bookingid,form=bookForm)

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
        if form.validate_on_submit:
            Id = form.id.data
            password = form.password.data

            user = EmployeeProfile.query.filter_by(empid=Id).first()
            if user is not None and check_password_hash(user.password,password):
            
                login_user(user)
                return redirect(url_for("secure_page"))
            else:
                flash("Incorrect Id or password", "failure")
    return render_template("login.html", form=form)   

@login_manager.user_loader
def load_user(empid):
    return EmployeeProfile.query.get(empid)

@app.route('/secure-page/')
@login_required
def secure_page():
    if current_user.is_authenticated:
        return render_template('secure-page.html')
    else:
        return redirect(url_for('login'))

def trackEmployee():
    global EMP_TRACK
    EMP_TRACK +=1
    return EMP_TRACK
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
