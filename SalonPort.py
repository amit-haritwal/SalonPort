from flask import request,redirect,url_for,session,render_template,Flask
from flask_wtf import FlaskForm
from otp import *
from databaseconnectivity import *
from wtforms import (SubmitField,TextField,
                    TextAreaField,TimeField,
                    PasswordField,RadioField,
                    FileField,SelectField)
from wtforms.validators import DataRequired,Required,NumberRange, InputRequired
from wtforms.fields.html5 import EmailField,TelField
import random
from elements import *
app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
@app.route('/',methods=['GET','POST'])
def home():
    form1=searchsalonitems()
    if form1.validate_on_submit():
        session['search']=form1.searchitem.data
        return redirect(url_for('searchsalon'))
#first time when user will enter the it will return session['length']=0
#which means that user is not logined
    try:
        print("hi")
        if session['length']>0:
            return render_template("index.html",form1=form1)
        else:
            return render_template("index.html",form1=form1)
    except KeyError:
        session['length']=0
        return render_template("index.html",form1=form1)
@app.route('/login',methods=['GET','POST'])
def login_user():
    form1=login()
    session['password1']=0
    if form1.validate_on_submit():
        session['length']=5
        session['email']=form1.email.data
        session['password']=form1.password.data
        #verify from database and return name and length of name in session['length']
        verify,session['Name']=loginverify(session['password'],session['email'])
        if verify==0:
            return redirect(url_for('home'))
    return render_template("login_user.html",form1=form1)
@app.route('/loginprovider',methods=['GET','POST'])
def loginprovider():
    form1=loginp()
    if form1.validate_on_submit():
        session['length']=5
        session['saloncode']=form1.saloncode.data
        session['password']=form1.password.data
        #verify from database and return name and length of name in session['length']
        if loginverify()==0:
            return redirect(url_for('booking'))
    return render_template("login_provider.html",form1=form1)
@app.route('/register',methods=['GET','POST'])
def register_user():
    register_form=register()
    if register_form.validate_on_submit():
        session['email']=register_form.email.data
        session['password']=register_form.password.data
        session['confirmpassword']=register_form.confirmpassword.data
        session['name']=register_form.name.data
        session['phone']=register_form.phone.data
        session['gender']=register_form.gender.data
        session['user']="user"
        session['length']=len(session['name'])
        print(session['gender'])
        if session['password']==session['confirmpassword']:
            register_userdata(session['name'],session['phone'],session['email'],session['password'],session['gender'])
            import random
            otp_pass=random.randint(100000,999999)
            sendmail(session['email'],otp_pass)
            session['opt_pass']=otp_pass
            return redirect(url_for('otp'))
        return redirect(url_for('register_user'))
    return render_template("register_user.html",register_form=register_form)
@app.route('/register_provider',methods=['GET','POST'])
def register_provider():
    register_form=registersalon()
    if register_form.validate_on_submit():
        session['email']=register_form.email.data
        session['name']=register_form.name.data
        session['phone']=register_form.phone.data
        session['typeofsalon']=register_form.typeofsalon.data
        session['noofemp']=register_form.noofemp.data
        session['owner']=register_form.owner.data
        session['password']=register_form.confirmpassword.data
        session['confirmpassword']=register_form.password.data
        session['user']="provider"
        if session['password']==session['confirmpassword']:
            return redirect(url_for('employer'))
    return render_template("register_provider.html",register_form=register_form)
@app.route('/otp',methods=['GET','POST'])
def otp():
    #creating object for otp
    form1=otpgenerater()
    #otpmsg(session['phone'])
    session['email1']=session['email'][:2]+'XXXXXXXXXXXX'+session['email'][session['email'].find('@'):]
    session['phone1']=session['phone'][:2]+'XXXXXXXX'+session['phone'][8:]
    if form1.validate_on_submit():
        session['otp']=form1.otp.data
        if session['otp']==str(session['opt_pass']):
            session['length']=1
            return redirect(url_for('home'))
    #otp verifcation via otp
    return render_template("otp.html",form1=form1)
@app.route('/logout',methods=['GET','POST'])
def logout():
    #just telling that session has ended
    session['length']=0
    return redirect(url_for("home"))
@app.route('/employer',methods=['GET','POST'])
def employer():
    form1=employerdetails()
    if form1.validate_on_submit():
        if int(session['noofemp'])==1:
            session['name']=form1.name.data
            session['phone']=form1.phone.data
            session['gender']=form1.gender.data
            session['email']=form1.email.data
            #store data in dta base with employer code
            return redirect(url_for('cataloge'))
        else:
            session['name']=form1.name.data
            session['phone']=form1.phone.data
            session['gender']=form1.gender.data
            session['email']=form1.email.data
            #store data in dta base with employer code
            form1.name.data=''
            form1.phone.data=''
            form1.gender.data=''
            form1.email.data=''
            session['noofemp']=int(session['noofemp'])-1
            return render_template("employerdetails.html",form1=form1)
    return render_template("employerdetails.html",form1=form1)
@app.route('/cataloge',methods=['GET','POST'])
def cataloge():
    return render_template("cataloge.html")
@app.route('/uploadimage',methods=['GET','POST'])
def uploadimage():
    form1=uploadimagesalon()
    if form1.validate_on_submit():
        image1=form1.image1.data
        image2=form1.image2.data
        image3=form1.image3.data
        image4=form1.image4.data
        image5=form1.image5.data
        return redirect(url_for('salontimetabel'))
    return render_template("uploadimage.html",form1=form1)
@app.route('/salontimetabel',methods=['GET','POST'])
def salontimetabel():
    form1=timetabelofsalon()
    if form1.validate_on_submit():
        return render_template('thanksprovider.html')
    return render_template("salontimetabel.html",form1=form1)
@app.route('/searchsalon',methods=['GET','POST'])
def searchsalon():
    form1=searchsalonitems()
    form2=bookfirststerp()
    if form1.validate_on_submit():
        session['search']=form1.searchitem.data
        return redirect(url_for('searchsalon'))
    if form2.validate_on_submit():
        return redirect(url_for('bookingtimeandselectemp'))
    return render_template("searchfile.html",form1=form1,form2=form2)
@app.route('/bookingtimeandselectemp',methods=['GET','POST'])
def bookingtimeandselectemp():
    form1=searchsalonitems()
    form3=employerandsalon()
    if form1.validate_on_submit():
        session['search']=form1.searchitem.data
        return redirect(url_for('searchsalon'))
    return render_template("bookemployerandtime.html",form1=form1,form3=form3)
@app.route('/booking',methods=['GET','POST'])
def booking():
    #bookings page will come
    return render_template("bookings_provider.html")
if __name__ == '__main__':
    app.run(debug=True)
