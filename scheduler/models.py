from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import secrets

db = SQLAlchemy()
ma = Marshmallow()

class Preset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(50))
    Last_Name = db.Column(db.String(50))
    Phone_No = db.Column(db.String(15))
    Email = db.Column(db.String(70))
    Subject = db.Column(db.String(50))
    Date = db.Column(db.String(50))
    StartTime = db.Column(db.String(30))
    EndTime = db.Column(db.String(30))

    def __init__(self, First_Name, Last_Name, Phone_No, Email, Subject, Date, StartTime, EndTime):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Phone_No = Phone_No
        self.Email = Email
        self.Subject = Subject
        self.Date = Date
        self.StartTime = StartTime
        self.EndTime = EndTime

        def set_id(self):
            return (secrets.token_urlsafe())

class PresetSchema(ma.Schema):
    class Meta:
        fields = ['id', 'First_Name', 'Last_Name', 'Phone_No', 'Email', 'Subject', 'Date', 'StartTime', 'EndTime']


preset_schema = PresetSchema()
presets_schema = PresetSchema(many=True)