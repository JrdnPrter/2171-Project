from . import db
from werkzeug.security import generate_password_hash


class EmployeeProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'employee_profiles'

    empid = db.Column(db.String(10), primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    password = db.Column(db.String(255))
    position = db.Column(db.String(3))


    def __init__(self,first_name,last_name,id,password,position):
        self.first_name = first_name
        self.last_name = last_name
        self.password = generate_password_hash(password,method="pbkdf2:sha256")
        self.position = position
        self.empid='Emp-' + str(id)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_supervisor(self):
        if self.position == "Sup":
            return True
        else:
            return False

    def get_id(self):
        try:
            return unicode(self.empid)  # python 2 support
        except NameError:
            return self.empid  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.empid)


class Booking(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cfname = db.Column(db.String(40))
    clname=db.Column(db.String(40))
    contact = db.Column(db.String(11))
    event_date = db.Column(db.Date)
    address = db.Column(db.String(225))
    

    def __init__(self,cfname,clname,contact,event_date,address):
        self.cfname=cfname
        self.clname=clname
        self.contact=contact
        self.event_date=event_date
        self.address=address
class Equipment(db.Model):
    __tablename__ = 'equipment'
    equip_id = db.Column(db.String(10),primary_key = True)
    equip_name = db.Column(db.String(30))


    def __init__(self, equip_id, equip_name,):
        self.equip_id=  equip_id
        self.equip_name=equip_name


class EquipmentAssignments(db.Model):
    __tablename__ = 'equipment_assignments'
    bookingid = db.Column(db.Integer,db.ForeignKey(Booking.id),primary_key=True)
    eqipmentid = db.Column(db.String(10),db.ForeignKey(Equipment.equip_id),primary_key=True)

