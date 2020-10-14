from flask import request,redirect,url_for,session,render_template,Flask
from flask_wtf import FlaskForm
from wtforms import (SubmitField,TextField,SelectField,
                    TextAreaField,TimeField,
                    PasswordField,RadioField,
                    FileField,SelectField,DateField,DateTimeField)
from wtforms.validators import DataRequired,Required,NumberRange, InputRequired
from wtforms.fields.html5 import EmailField,TelField
class employerandsalon(FlaskForm):
    employer=SelectField("checked")
    cataloge=SelectField("checked")
class bookfirststerp(FlaskForm):
    book=SubmitField('Book')
class timetabelofsalon(FlaskForm):
    otime=DateTimeField('Salon Opening Time',validators=[DataRequired()])
    ctime=DateTimeField('Salon Closing Time',validators=[DataRequired()])
    dayofweek=SelectField('Day of week when you are absent',
    choices=[('mo','Monday'),('tu','Tuesday'),
    ('we','Wednesday'),('th','ThursDay'),('fr','Friday'),
    ('sa','Saturday'),('su','Sunday')])
    Submit=SubmitField('Confirm')
class uploadimagesalon(FlaskForm):
    image1=FileField('Image 1',validators=[Required()])
    image2=FileField('Image 2',validators=[Required()])
    image3=FileField('Image 3',validators=[Required()])
    image4=FileField('Image 4',validators=[Required()])
    image5=FileField('Image 5',validators=[Required()])
    submit=SubmitField('submit')
class employerdetails(FlaskForm):
    name=TextField('Employer Name',validators=[Required()])
    phone=TelField('Employer Phone',validators=[Required()])
    email=EmailField('Employer Gmail',validators=[Required()])
    submit=SubmitField('Submit',validators=[Required()])
    gender=RadioField(label='Gender',choices=[('m','MALE'),('f','FEMALE')],validators=[InputRequired()])
class registersalon(FlaskForm):
    name=TextField('Salon Name',validators=[Required()])
    phone=TelField('Salon Phone',validators=[Required()])
    email=EmailField('Salon Gmail',validators=[Required()])
    owner=TextField('Owner Name',validators=[Required()])
    password=PasswordField('Password',validators=[Required()])
    confirmpassword=PasswordField('Confirm Password',validators=[Required()])
    noofemp=TelField('Number of Employer',validators=[Required()])
    typeofsalon=RadioField(label='Type of Salon',choices=[('m','GENTS'),('f','LADIDES'),('o','UNISEX')],validators=[InputRequired()])
    submit=SubmitField('Submit')
class otpgenerater(FlaskForm):
    otp=TelField('OTP')
    submit=SubmitField('Submit')
#booking elements
'''class booking(FlaskForm):
    name=TextField('Customer Name')
    services=TextField('Services')
    timerequired=TimeField('Time Required')
    timebooking=TimeField('Booking Time')
    employername=TextField('Employer Name')
    Submit=SubmitField('Done')'''
#login user elements
class login(FlaskForm):
    email=EmailField('Email',validators=[Required()])
    password=PasswordField('Password',validators=[Required()])
    submit=SubmitField('Submit')
#login provider elements
class loginp(FlaskForm):
    saloncode=TelField('Salon Code',validators=[Required()])
    email=EmailField('Email',validators=[Required()])
    password=PasswordField('Password',validators=[Required()])
    submit=SubmitField('Submit')
#registration details
class register(FlaskForm):
    email=EmailField('Email',validators=[InputRequired()])
    name=TextField('Name',validators=[Required()])
    phone=TelField('Phone',validators=[Required()])
    gender=RadioField(label='Gender',choices=[('m','MALE'),('f','FEMALE')],validators=[InputRequired()])
    submit=SubmitField('Submit',validators=[Required()])
    password=PasswordField('Password',validators=[Required()])
    confirmpassword=PasswordField('Confirm Password',validators=[Required()])
class searchsalonitems(FlaskForm):
    submit=SubmitField('')
    searchitem=TextField('Name',validators=[Required()])
