from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, IntegerField, PasswordField, FormField, TextAreaField, SelectField, BooleanField,  DecimalField, SubmitField, DateField
from wtforms.validators import InputRequired, DataRequired

# equipList = ['Sound Systems', 'Party Lights', 'Tables', 'Chairs']


class LoginForm(FlaskForm):
    id = StringField('Employee Id', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

#for use in the create booking form.
#if possible, find a way to iterate this from a list.
class EquipmentForm(FlaskForm):

    
    sound = BooleanField("Sound Systems")
    light = BooleanField("Party Lights")
    table = BooleanField("Tables")
    chair = BooleanField("Chairs")


#create booking
class BookingForm(FlaskForm):
    clientFName = StringField('Client First Name', 
                                validators=[DataRequired()])

    clientLName = StringField('Client Last Name', 
                                validators=[DataRequired()])
                            

    contact = StringField('Phone Number (10-digit)', 
                                validators=[DataRequired()])

    eventDate = DateField('Event Date (YYYY/MM/DD)', 
                                validators=[DataRequired()])

    eventTime = TimeField('Event Start Time (Hour:Minute) ')

    address = StringField('Event Address', 
                                validators=[DataRequired()])

    equipment = FormField(EquipmentForm)
    
    submit = SubmitField("Book Equipment")


#register new employee
class EmployeeForm(FlaskForm):

    employeeFName = StringField('First Name',
                                validators=[DataRequired()])
    employeeLName = StringField('Last Name',
                                validators=[DataRequired()])

    dob = DateField('Date of Birth (YYYY/MM/DD)', 
                                validators=[DataRequired()])

    sex = SelectField('Sex',  
                        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
                        validators=[DataRequired()])
    
    password = StringField('Password',
                                validators=[DataRequired()])
                                
    register = SubmitField("Register new employee")

    position = SelectField('Registered Position',
                                choices=[('Sup', 'Supervisor'), ('Emp', 'Employee')],
                        validators=[DataRequired()])


