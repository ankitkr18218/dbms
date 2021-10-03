
from flask import Flask, render_template, flash , redirect , url_for , session,request
from wtforms import Form,StringField, TextAreaField, PasswordField, validators
import mysql.connector
import re
from datetime import date

from passlib.hash import sha256_crypt

mydb=mysql.connector.connect(host="localhost",user="root",passwd="ankit@123",database="liquors_castle4")
mycursor = mydb.cursor()

store = Flask(__name__, template_folder='abc')


@store.route('/')
def home():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM"" `liquors_castle4`.item;")
    result = mycursor.fetchall()

    if session.get('logged_in'):
        return render_template('home.html', result=result,username=session['user'])
    else:
        return render_template('home.html', result=result,username="no user")

@store.route('/supplierhome/')
def supplierhome():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()



    if session.get('supplier_logged_in'):
        mycursor.execute("SELECT * FROM"" `liquors_castle4`.item where  Supplier_ID ='" + session['supplier'] + "';")
        result = mycursor.fetchall()
        print(session['supplier'])
        return render_template('supplierhome.html', result=result,username=session['supplier'])
    else:
        return "login fisrt"



@store.route('/', methods=['GET', 'POST'])
def results():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()
    if request.method == "POST":
        query = request.form['query_by_user']
        # search by author or book
        mycursor.execute("SELECT * from item WHERE Name LIKE %s OR Item_type LIKE %s;", (query, query))

        result = mycursor.fetchall()
        # all in the search box will return all the tuples
        if len(result) == 0 and query == 'all':
            mycursor.execute("SELECT * from item;")
            # mydb.commit()
            result = mycursor.fetchall()
            for i in result:
                print(i)
        return render_template('home.html', result=result)
    return render_template('home.html')


@store.route('/about')
def about():
    return render_template('about.html')

@store.route('/contact')
def contact():
    return render_template('contact.html')

@store.route('/product_detail/<det>')
def product_detail(det):
    det = str(det)
    command = "Select * From item where item_id="

    command += "'"+det+ "';"
    print(command)
    mycursor.execute(command)
    result = mycursor.fetchone()

    itemid = result[0]
    itemname = result[1]
    itemtype = result[2]
    supplier=result[3]
    avalble = result[4]
    place = result[5]
    price = result[6]

    link = result[7]
    discount = "NO DISCOUNT AVAILABLE :("
    command = "select Deal_ID from deals where item_id = "+ "'"+det+ "';"
    mycursor.execute(command)
    deals = []
    deals = mycursor.fetchone()
    if len(deals) >=1:
        discount = "DISCOUNT AVAILABLE, COUPON CODE IS " + deals[0] + " (AUTO APPLICABLE)"

    if session.get('logged_in'):
        mycursor.execute("select Customer_id from customer where Customer_name = %s and pass_word = %s;",
                         (session['user'], session['pass_word']))
        result1 = mycursor.fetchone()
        return render_template('product_detail.html', itemid=itemid, itemname=itemname, itemtype=itemtype,supplier=supplier,discount=discount,
                               avalble=avalble, place=place, price=price,  link = link,username=session['user'],password=session['pass_word'],userid=result1[0])

    else:
        return render_template('product_detail.html', itemid=itemid, itemname=itemname, itemtype=itemtype,supplier=supplier,discount=discount,
                               avalble=avalble, place=place, price=price,  link = link,username="No user",password='no',userid='no')



@store.route('/supplierchange/<det>/<username>/', methods=['GET','POST'])
def supplierchange(det,username):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
        mycursor = mydb.cursor()

        det = str(det)
        command = "Select * From item where item_id="

        command += "'"+det+ "';"
        print(command)
        mycursor.execute(command)
        result = mycursor.fetchone()

        itemid = result[0]
        itemname = result[1]
        itemtype = result[2]
        supplier=result[3]
        avalble = result[4]
        place = result[5]
        price = result[6]
        link = result[7]
        try:
            if request.method == 'POST':
                userdetails = request.form
                name = userdetails['name']
                itemtype = userdetails['itemtype']
                itemplace = userdetails['place']
                price = userdetails['price']
                place = userdetails['place']
                aval = userdetails['aval']
                link  = userdetails['link']

                #mycursor.execute("Delete from item where item_id = ""'"+det+ "';")
                #mydb.commit()
                comm = "update item set " "Name = " + "'"+str(name)+"'" + ", Item_type=" + "'"+str(itemtype)+"'"+  ", Item_available_status=" \
                + "'"+str(aval) +"'"+ ", Places_item_available=" +"'"+ str(itemplace)+"'" + ", Price=" +"'"+ str(price) + "'" + ", Image=" +"'"+ str(link)+"' where item_id=""'"+det+ "';"
                print(comm)
                mycursor.execute(comm)
                mydb.commit()
                return 'success'
        except:
            return render_template('supplierchange.html', itemid=itemid, itemname=itemname, itemtype=itemtype,
                                   avalble=avalble, place=place, price=price, link=link,username=username)

        return render_template('supplierchange.html', itemid=itemid, itemname=itemname, itemtype=itemtype,
                               avalble=avalble, place=place, price=price, link=link,username=username)



@store.route('/supplieradd/<username>/', methods=['GET','POST'])
def supplieradd(username):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()

    try:
        if request.method == 'POST':
                userdetails = request.form
                name = userdetails['name']
                itemid = userdetails['itemid']
                itemtype = userdetails['itemtype']
                itemplace = userdetails['place']
                price = userdetails['price']
                place = userdetails['place']
                aval = userdetails['aval']
                link  = userdetails['link']

                comm = "insert into Item (item_id, Name, Item_type, Supplier_id, Item_available_status, Places_item_available, Price ,Image) values "
                com = []
                com.append(itemid)
                com.append(name)
                com.append(itemtype)
                com.append(username)
                com.append(aval)
                com.append(itemplace)
                com.append(price)
                com.append(link)
                com = tuple(com)
                comm += str(com)
                comm += ";"
                if session.get('supplier_logged_in'):
                    mycursor.execute(comm)
                    mydb.commit()
                    flash("succesfully added")
                else:
                    flash("please login first")
        render_template('supplieradd.html', username=session['supplier'])
    except:
        return render_template('supplieradd.html',username=session['supplier'])
    return render_template('supplieradd.html',username=session['supplier'])




@store.route('/addtocart/<id>/<user>/<password>/<price>/<name>')
def add_to_cart(id,user,password,price,name):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()

    if session.get('logged_in'):

        user1="'" +user+ "'"
        password1="'" +password+ "'"
        command = "select Customer_id from customer where Customer_name = {0} and pass_word = {1};".format(user1,password1)

        mycursor.execute(command)

        result=mycursor.fetchone()

        result1="'" +result[0]+ "'"
        command="select * from add_to_cart where Customer_id = '{0}' and item_id ='{1}';".format(result[0],id)

        mycursor.execute(command)
        result2 = mycursor.fetchone()

        name1="'" +name+ "'"
        if result2 is not None and result2[1]==result[0] and result2[0]==id:
            flash("ITEM ALREADY IN CART")
        else:

            command="insert into add_to_cart (item_id,Customer_id) values ('{0}' , '{1}');".format(id,result[0])
            mycursor.execute(command)
            mydb.commit()
        mycursor.execute("select * from add_to_cart where Customer_id ='"+result[0]+"';")
        result1=mycursor.fetchall()


        return render_template('addtocart.html',result1=result1)
    else:
        return 'no user currently logined'

@store.route('/remove/<itemid>')
def deltecart(itemid):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM add_to_cart WHERE item_id='"+itemid+"';")
    mydb.commit()
    return redirect('/')



@store.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

@store.route('/registersupplier', methods=['GET','POST'])
def registersupplier():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    cursor = mydb.cursor()
    command = "select * from suppliers ORDER BY Supplier_ID DESC LIMIT 1"
    cursor.execute(command)
    result = cursor.fetchone()
    new_suppid = int(result[0]) + 1
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        surname = userdetails['surname']
        email = userdetails['email']
        licnumber = userdetails['licnumber']
        adharnumber = userdetails['adharnumber']
        owneraddress = userdetails['owneraddress']
        number  = userdetails['number']
        shopaddress = userdetails['shopaddress']
        cityserve = userdetails['cityserve']
        password = userdetails['password']

        com = []
        com.append(str(new_suppid))
        com.append(name)
        com.append(surname)
        com.append(adharnumber)
        com.append(licnumber)
        com.append(owneraddress)
        com.append(shopaddress)
        com.append(number)
        com.append(email)
        com.append(cityserve)
        com.append(password)
        com = tuple(com)
        if password == "" or password == None:
            return render_template('registersupplier.html', new_suppid=new_suppid)

        command1 = "insert into suppliers (Supplier_ID, Name, Surname, Aadhar_No, Licence_No, Owner_address, Shop_address, Contact_No, email, City_Serveable, password) values "
        command1 += str(com)
        command1 += ";"
        try:
            cursor.execute(command1)
            mydb.commit()
            return 'success'
        except:
            pass

    return render_template('registersupplier.html',new_suppid = new_suppid)



@store.route('/registercustomer', methods=['GET','POST'])
def registercustomer():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    cursor = mydb.cursor()
    command = "select * from customer ORDER BY customer_id DESC LIMIT 1"
    cursor.execute(command)
    result = cursor.fetchone()
    new_suppid = int(result[0]) + 1
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        surname = userdetails['surname']
        email = userdetails['email']
        dob = userdetails['dob']
        adharnumber = userdetails['adharnumber']
        state = userdetails['state']
        number  = userdetails['number']
        address = userdetails['address']
        city = userdetails['city']
        password = userdetails['password']

        com = []
        com.append(str(new_suppid))
        com.append(name)
        com.append(surname)
        com.append(email)
        com.append(dob)
        com.append(state)
        com.append(city)
        com.append(address)
        com.append(number)
        com.append(password)
        com.append(adharnumber)
        com = tuple(com)
        if password == "" or password == None:
            return render_template('registersupplier.html', new_suppid=new_suppid)

        command1 = "insert into Customer (Customer_id, Customer_name, Surname, email, DOB, state, city, address, delivery_Phone_no, pass_word, aadhar_no) values "
        command1 += str(com)
        command1 += ";"
        try:
            cursor.execute(command1)
            mydb.commit()
            return 'success'
        except:
            pass

    return render_template('registercustomer.html',new_suppid = new_suppid)



@store.route('/login/')
def login():
    return render_template('login.html')

@store.route('/logincustomer', methods=['GET','POST'])
def logincustomer():

    if request.method == 'POST':
        userdetails = request.form
        cusid = userdetails['cusid']
        password = userdetails['password']
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
        cursor = mydb.cursor()

        useranemdata = cursor.execute("SELECT Customer_ID FROM customer WHERE Customer_ID ='"+cusid+"'")
        user=cursor.fetchone()
        passworddata = cursor.execute("SELECT pass_word FROM customer WHERE Customer_ID ='"+cusid+"'")
        passw = cursor.fetchone()
        cursor.execute("SELECT Customer_name FROM customer WHERE Customer_ID ='"+cusid+"'")
        username = cursor.fetchone()
        if user is None:
            flash("No customer_ID please try again ....")
        else:
            for passwd in passw:
                if (password==passwd):

                    session['logged_in'] = True
                    session['user'] = username[0]
                    session['pass_word']=userdetails['password']

                    return redirect('/')
            if not session.get('logged_in'):
                flash("wrong username")

    return render_template('logincustomer.html')


@store.route('/loginsupplier', methods=['GET','POST'])
def loginsupplier():

    if request.method == 'POST':
        userdetails = request.form
        supid = userdetails['supid']
        password = userdetails['password']
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
        cursor = mydb.cursor()
        supiddata = cursor.execute("SELECT Supplier_ID FROM suppliers WHERE Supplier_ID ='" + supid + "'")
        user = cursor.fetchone()
        passworddata = cursor.execute("SELECT password FROM suppliers WHERE Supplier_ID ='" + supid + "'")
        passw = cursor.fetchone()
        cursor.execute("SELECT Name FROM suppliers WHERE Supplier_ID ='"+supid+"'")
        username = cursor.fetchone()
        if user is None:
            flash("No Supplier_ID please try again ....")
        else:
            for passwd in passw:
                if (password==passwd):

                    session['supplier_logged_in'] = True
                    session['supplier'] = supid

                    return redirect('/supplierhome/')
            if not session.get('supplier_logged_in'):
                flash("wrong username")

    return render_template('loginsupplier.html')



@store.route('/logout')
def logout():
    # Remove session data, this will log the user out
    if session.get('logged_in') or session.get('supplier_logged_in') :
        session.pop('logged_in', None)
        session.pop('username', None)
        session.pop('supplier_logged_in', None)
        session.pop('supplier', None)
        flash("LOgOuT DoNe")
        return redirect('/login/')
   # Redirect to login page
    else:
        return redirect('/')


@store.route('/order/<itemid>/<userid>/',methods=['GET','POST'])
def order(itemid,userid):
    if session.get('logged_in'):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
        mycursor = mydb.cursor()
        mycursor.execute("select Name,Price,Image from item where item_id ='" + itemid + "'")
        result = mycursor.fetchone()

        command = "select * from Order1 ORDER BY Order_id DESC LIMIT 1"
        mycursor.execute(command)
        result1 = mycursor.fetchone()
        new_orderid = int(result1[0]) + 1

        try:
            if request.method == 'POST':
                userdetails = request.form
                address = userdetails['address']
                phone = userdetails['phone']
                quantity = userdetails['quantity']

                com = []
                com.append(str(new_orderid))
                com.append(itemid)
                com.append(userid)
                com.append(quantity)
                com.append(phone)
                com.append(str(date.today()))
                com.append(address)
                com = tuple(com)

                command1 = "insert into Order1 (Order_id,item_id,Customer_id,Quantity,Contact_No,Order_date, Delivery_address) values "
                command1 += str(com)
                command1 += ";"


                mycursor.execute(command1)

                return render_template('orderform.html', name=result[0], link=result[2], price=result[1], user=userid,item=itemid,order=new_orderid)




            return render_template('orderform.html', name=result[0], link=result[2], price=result[1], user=userid,item=itemid,order=new_orderid)


        except Exception:
            mydb.rollback()
        finally:
            mydb.commit()
    else:
        flash("please login first to order")
        return redirect('/login/')


@store.route('/tranaction/<item>/<user>/<price>/<order>/',methods=['GET','POST'])
def tranaction(item,user,price,order):

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()
    command = "select * from transaction ORDER BY transaction_id DESC LIMIT 1"
    mycursor.execute(command)
    result = mycursor.fetchone()
    new_id = int(result[0]) + 1
    #command5 = "select Quantity from order1 where Order_id= '{0}'; ".format(Order_id)
    #print(command5)
    #mycursor.execute(command5)
    #quantity = mycursor.fetchone()
    #print(price,quantity[0])
    total_price=int(int(price)* 3)
    print(total_price)

    try:
        command2= "select * from deals where item_id='{0}'".format(item)
        print(command2)
        mycursor.execute(command2)
        e = mycursor.fetchall()
        command3 = "select * from discounttypes where Discounttype='{0}' ORDER BY Discount DESC LIMIT 1".format(
            str(e[1]))

        print(command3)

        mycursor.execute(command3)
        y = mycursor.fetchone()
        total_price=int(totalprice)-(int(total_price)*int(y[0])/100)
        print(total_price)

    finally:
        if request.method == 'POST':

            userdetails = request.form
            accountno = userdetails['account']
            pay_mode = userdetails['mode']
            command2="insert into transaction (transaction_id,Customer_id,account_id,item_id,transacted_money,transaction_time,transaction_date,payment_mode) values ('{0}','{1}','{2}','{3}','{4}','9:30','{5}','{6}')".format(new_id,str(user),str(accountno),str(item),str(total_price),str(date.today()),str(pay_mode))
            print(command2)
            mycursor.execute(command2)
            mydb.commit()


        ##sab kuch insert karna ha abb bas into table
            return render_template('tranaction.html',totalprice=total_price)
        return render_template('tranaction.html',totalprice=total_price)


@store.route('/rejectedorder/<orderid>/<itemid>/<userid>/')
def rejectedorder(orderid,itemid,userid):

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()

    if session.get('logged_in'):

        if request.method == 'POST':
            userdetails = request.form
            reason = userdetails['reason']

            com = []
            com.append(orderid)
            com.append(itemid)
            com.append(userid)
            com.append(reason)

            com = tuple(com)

            command1 = "insert into rejected_order (Order_id,Item_ID,Customer_id,reason) values "
            command1 += str(com)
            command1 += ";"

            mycursor.execute(command1)
            mydb.commit()
            return render_template('reject.html', name=itemid, customer=userid)



        return render_template('reject.html',name=itemid,customer=userid)
    else:
        return "login first"


@store.route('/orderplaced')
def orderplaced():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="ankit@123", database="liquors_castle4")
    mycursor = mydb.cursor()

    if session.get('logged_in'):

        user1 = "'" + session['user'] + "'"
        password1 = "'" + session['pass_word'] + "'"
        command = "select Customer_id from customer where Customer_name = {0} and pass_word = {1};".format(user1,
                                                                                                           password1)

        mycursor.execute(command)

        result = mycursor.fetchone()

        result1 = "'" + result[0] + "'"
        command = "select * from order1 where Customer_id = '{0}';".format(result[0])

        mycursor.execute(command)
        result2 = mycursor.fetchall()

        return render_template('ordersplaced.html', result=result2)
    else:
        return 'NO USER LOGINED PLEASE LOGIN FIRST'


if __name__=='__main__':
    store.secret_key="1223445hi"
    store.run(debug=True)
