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
\password lab5 will (propmpt for password, keep it simple)
alter database <databasename> owner to <username>;

go to config.py and change the database url to your database url 
database = "postgresql://<username>:<password>@localhost/<databasename>"

Run:
python run.py

Go to :
http://localhost:8080/



Creating a new User to log in with:
$ python
>>> from app import db
>>> from app.models import <Table name>
>>> user = UserProfile(first_name="Your name",
last_name="Your last name", username="someusername",
password="somepassword")
>>> db.session.add(user)
>>> db.session.commit()
>>> quit()
```

