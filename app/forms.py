from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField,  DecimalField, SubmitField, DateField, SelectMultipleField
from wtforms.validators import InputRequired, DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


#create booking
class BookingForm(FlaskForm):
    clientName = StringField('Client Name', 
                                validators=[DataRequired()])

    contact = StringField('Phone Number', 
                                validators=[DataRequired()])

    eventDate = DateField('Event Date (YYY/MM/DD)', 
                                validators=[DataRequired()])

    address = StringField('Event Address', 
                                validators=[DataRequired()])

    equipment = SelectMultipleField('Equipment for rental', 
                                choices=[('sound', 'Speaker Box sets'), ('light', 'Party Lights'), ('table', 'Tables'), ('chair', 'Chairs')])


    submit = SubmitField("Book Equipment")