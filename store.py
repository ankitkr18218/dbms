
from flask import Flask, render_template, flash , redirect , url_for , session,request
from wtforms import Form,StringField, TextAreaField, PasswordField, validators
import mysql.connector
from passlib.hash import sha256_crypt

mydb=mysql.connector.connect(host="localhost",user="root",passwd="ankit@123")
mycursor = mydb.cursor();


mycursor.execute("SELECT * FROM `liquor's_castle`.suppliers;")
for i in mycursor:
     print(i)


store = Flask(__name__, template_folder='abc')




@store.route('/')
def home():
    return render_template('home.html')


@store.route('/about')
def about():
    return render_template('about.html')



@store.route('/register', methods=['GET','POST'])

def register():

    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        email = userdetails['email']
        licence = userdetails['licence']
        password = userdetails['password']

        return 'success'


    return render_template('register.html')




if __name__=='__main__':
    store.run(debug=True)
