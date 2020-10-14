import pymongo
from flask import request,redirect,url_for,session,render_template,Flask
from pymongo import MongoClient
client = MongoClient()
db=client.SalonPort
collection=db.register_user
posts=db.register_user
def loginverify(password,email):
    passwordv=posts.find_one({"password":password})
    session['Name']=""
    try:
        p=passwordv.get("password")
        e=passwordv.get("Email")
        session['Name']=passwordv.get("Name")
        if session['password']==p and session['email']==e:
            session['password1']=0
            #zero = correct and one = wrong
            return session['password1'],session['Name']
        else:
            session['password1']=1
            return session['password1'],session['Name']
    except:
        session['password1']=1
        return session['password1'],session['Name']
def register_userdata(name,phone,email,password,gender):
    post={"Name":name,"Email":email,"Phoneno":phone,"password":password,"Gender":gender}
    post_id=posts.insert_one(post).inserted_id
