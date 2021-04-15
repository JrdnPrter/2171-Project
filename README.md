# flask_starter

```
Run in terminal 
$ python -m venv venv (you may need to use python3 instead)
$ source venv/bin/activate (or .\venv\Scripts\activate on Windows)
$ pip install -r requirements.txt 
$ python run.py

make sure you have postgresql installed 
https://www.postgresql.org/download/windows/
postgresql will askyou to input a personal password. remember it 


#open the postgresql command line by searching for psql in windows startup 


Run these commands in posrgresql:
create user "<username>";
create database "<databasename>";
\password <username> will (propmpt for password, keep it simple)
alter database <databasename> owner to <username>;

go to config.py and change the database url to your database url 
database = "postgresql://<username>:<password>@localhost/<databasename>"

Run:
python run.py

Go to :
http://localhost:8080/



Create an initial admin user:
$ python
from app import db
from app.models import EmployeeProfile
user = EmployeeProfile(first_name="John",last_name="Brown", password="admin",position="Sup",id=0)
db.session.add(user)
db.session.commit()
quit()

Create an equipment tables:
from app import db
from app.models import Equipment
eq = Equipment(equip_id="Eq_1",equip_name="Sound System")
db.session.add(eq)
do this for each equipment in form
db.session.commit()
quit()
From here can create aditional users in the website as needed
```

