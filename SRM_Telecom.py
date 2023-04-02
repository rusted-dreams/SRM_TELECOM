myfile = open("link.txt", "r")
usr=myfile.readline()
usr=usr.strip("\n")
passwd=myfile.readline()
passwd=passwd.strip("\n")
databse=myfile.readline()
databse=databse.strip("\n")

import mysql.connector

print("This is the Fresh starting of program so you need to select the desired enteries")
entry=input("Do you want to continue with the previous database\n (Recommended:If you are running it first time then you must create new)?\n Y or N: ")
if entry.lower()=="n":
    myfile=open("link.txt",'w')
    usr=input("Enter the user name of MySql: ")

    passwd=input("Enter the password of MySql: ")

    databse=input("Enter the name of new database to create: ")
    list=[usr,passwd,databse]
    for i in list:
        myfile.write(i)
        myfile.write("\n")
    myfile.close()

    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd)

    mycur = mydb.cursor()
    mycur.execute("create database {}".format(databse))
    mycur.execute("use {}".format(databse))
    str="create table SRM_Telecom (cno int(11) primary key not null,cname varchar(30) not null,mobile int(11) not null,address char(25),email varchar(30),no_calls int(8),status char(5))"
    mycur.execute(str)
    mydb.commit()
else:
    pass
def add():  # working fine

    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)

    mycur = mydb.cursor()

    ch = 'y'

    while ch.lower()=="y":
        print("enter the values: ")
        print(50*"=")
        cno = int(input("Customer no: "))
        cname = input("Customer Name: ")
        mobile = int(input("Phone no.: "))
        address = input("address: ")
        email = input("Email id.: ")
        no_calls = int(input("No. of calls: "))
        status = input("paid / due: ")
        str = "INSERT INTO SRM_Telecom VALUES ('{}','{}','{}','{}','{}','{}','{}')"
        query =str.format(cno, cname, mobile, address, email, no_calls, status)
        mycur.execute(query)
        mydb.commit()
        print("record inserted")
        print("="*50)
        ch = input("want to add more record (y/n): ")
        print("="*50)


def search():  # working fine

    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur = mydb.cursor()

    cno = int(input("Enter The Customer no.: "))
    str = "select*from SRM_Telecom where cno={}"
    query = str.format(cno)
    print("=" * 50)
    mycur.execute(query)
    myrec = mycur.fetchall()
    for x in myrec:
        cno = x[0]
        cname = x[1]
        mobile = x[2]
        address = x[3]
        email = x[4]
        no_calls = x[5]
        status = x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)


def display():  # working fine

    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur = mydb.cursor()

    mycur.execute("select * from SRM_Telecom")
    print("=" * 50)
    myrec = mycur.fetchall()
    for x in myrec:
        cno = x[0]
        cname = x[1]
        mobile = x[2]
        address = x[3]
        email = x[4]
        no_calls = x[5]
        status = x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)
        

def edit():         #working fine
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur=mydb.cursor()
    mycur.execute("select*from SRM_Telecom")
    print("="*99)
    print("available records\n")
    myrec=mycur.fetchall()
    for x in myrec:
        cno=x[0]
        cname=x[1]
        mobile=x[2]
        address=x[3]
        email=x[4]
        no_calls=x[5]
        status = x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)
        

    print("="*99)
    
    print("1:Update cname")
    print("2:Update mobile")
    print("3:Update address")
    print("4:Update email")
    print("5:Update no_call")
    print("6:Update status")
    print("7:Update all")
    print("="*99)
    chs=int(input("Enter your choice:"))
    if chs==1:
        edit_name()
    elif chs==2:
        edit_mobile()
    elif chs==3:
        edit_address()
    elif chs==4:
        edit_email()
    elif chs==5:
        edit_no_calls()
    elif chs==6:
        edit_status()
    elif chs==7:
        edit_all()
    elif ch==8:
        return
    
    else:
        print("INVATID CHOISE TRY AGAIN!")

def edit_name():
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur=mydb.cursor()
    cno=int(input("Customer no: "))
    cname=input("Customer Name: ")
    st="update SRM_Telecom set cname='%s'where cno='%s'"%(cname,cno)
    mycur.execute(st)
    mydb.commit()
    print(" Succesfully updated")
    print("="*99)

    print("after Updation\n")
    mycur.execute("select * from SRM_Telecom")

    myrec=mycur.fetchall()
    for x in myrec:
        cno=x[0]
        cname=x[1]
        mobile=x[2]
        address=x[3]
        email=x[4]
        no_calls=x[5]
        status=x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)


def edit_mobile():
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur=mydb.cursor()
    cno=int(input("Customer no: "))
    mobile=input("Enter phone no. : ")
    st="update SRM_Telecom set mobile='%s'where cno='%s'"%(mobile,cno)
    mycur.execute(st)
    mydb.commit()
    print("Succesfully updated")
    print("="*99)

    
    print("after Updation\n")
    mycur.execute("select * from SRM_Telecom")

    myrec=mycur.fetchall()
    for x in myrec:
        cno=x[0]
        cname=x[1]
        mobile=x[2]
        address=x[3]
        email=x[4]
        no_calls=x[5]
        status=x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)


def edit_address():
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur=mydb.cursor()
    cno=int(input("Customer no: "))
    address=input("Enter new Address :")
    st="update SRM_Telecom set address='%s'where cno='%s'"%(address,cno)
    mycur.execute(st)
    mydb.commit()
    print("Succesfully updated")
    print("="*99)

    print("after Updation\n")
    mycur.execute("select * from SRM_Telecom")

    myrec=mycur.fetchall()
    for x in myrec:
        cno=x[0]
        cname=x[1]
        mobile=x[2]
        address=x[3]
        email=x[4]
        no_calls=x[5]
        status=x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)


def edit_email():
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur=mydb.cursor()
    cno=int(input("Customer no: "))
    email=input("Enter new Email")
    st="update SRM_Telecom set email='%s'where cno='%s'"%(email,cno)
    mycur.execute(st)
    mydb.commit()
    print(" Succesfully updated")
    print("="*99)

    print("after Updation\n")
    mycur.execute("select * from SRM_Telecom")

    myrec=mycur.fetchall()
    for x in myrec:
        cno=x[0]
        cname=x[1]
        mobile=x[2]
        address=x[3]
        email=x[4]
        no_calls=x[5]
        status=x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)


def edit_no_calls():
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur=mydb.cursor()
    cno=int(input("Customer no: "))
    no_calls=int(input("Enter no of calls:"))
    st="update SRM_Telecom set no_calls='%s'where cno='%s'"%(no_calls,cno)
    mycur.execute(st)
    mydb.commit()
    print(" Succesfully updated")       

    
        
    print("="*99)

    
    print("after Updation\n")
    mycur.execute("select * from SRM_Telecom")

    myrec=mycur.fetchall()
    for x in myrec:
        cno=x[0]
        cname=x[1]
        mobile=x[2]
        address=x[3]
        email=x[4]
        no_calls=x[5]
        status=x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)


def edit_status():

    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur=mydb.cursor()
    cno=int(input("Customer no: "))
    status=(input("paid \ due :"))
    st="update SRM_Telecom set status='%s'where cno='%s'"%(status,cno)
    mycur.execute(st)
    mydb.commit()
    print(" Succesfully updated")

    print("="*99)

    
    
    print("after Updation\n")
    mycur.execute("select * from SRM_Telecom")

    myrec=mycur.fetchall()
    for x in myrec:
        cno=x[0]
        cname=x[1]
        mobile=x[2]
        address=x[3]
        email=x[4]
        no_calls=x[5]
        status=x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)


def edit_all():
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur = mydb.cursor()
    mycur.execute("select*from SRM_Telecom")
    print("=" * 50)
    print("Availble records\n")
    myrec = mycur.fetchall()
    for x in myrec:
        cno = x[0]
        cname = x[1]
        mobile = x[2]
        address = x[3]
        email = x[4]
        no_calls = x[5]
        status = x[6]
        print(cno, " | ", cname, " | ", mobile, " | ", address, " | ", email, " | ", no_calls, " | ", status)

    print("=" * 50)
    cno = int(input("Enter The Customer no You want to update: "))
    print("Enter The Changes You Want\n")
    cname = input("Enter The Customer Name: ")
    mobile = int(input("Enter The Phone no.: "))
    address = input("Enter The address: ")
    email = input("Enter The Email id.: ")
    no_calls = int(input("Enter The No. of calls: "))
    status= input("paid \ due :")

    str = "Update SRM_Telecom set cname='{}',mobile='{}',address='{}',email='{}',no_calls='{}', status='{}' where cno='{}'"
    query = str.format(cname, mobile, address, email, no_calls, status, cno)
    mycur.execute(query)
    mydb.commit()
    mycur.execute("select * from SRM_Telecom")
    print("=" * 50)

    print("After Updation\n\n")

    myrec = mycur.fetchall()
    for x in myrec:
        cno = x[0]
        cname = x[1]
        mobile = x[2]
        address = x[3]
        email = x[4]
        no_calls = x[5]
        status = x[6]
        print(cno, " | ", cname, " | ", mobile, " | ", address, " | ", email, " | ", no_calls, " | ", status)




def delete():# working fine
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur = mydb.cursor()
    mycur.execute("select * from SRM_Telecom")
    print("=" * 50)
    print("Before Deletion")
    print("=" * 50)

    myrec = mycur.fetchall()
    for x in myrec:
        cno = x[0]
        cname = x[1]
        mobile = x[2]
        address = x[3]
        email = x[4]
        no_calls = x[5]
        status=x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)

    cno = int(input("Enter The Customer no.: "))
    str = "Delete from SRM_Telecom where cno={}"
    query = str.format(cno)
    mycur.execute(query)
    mydb.commit()

    print("Record deleted")
    mycur.execute("select * from SRM_Telecom")
    print("=" * 50)
    print("After Deletion: ")
    print("="*50)

    myrec = mycur.fetchall()
    for x in myrec:
        cno = x[0]
        cname = x[1]
        mobile = x[2]
        address = x[3]
        email = x[4]
        no_calls = x[5]
        status=x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)


def generate():# working fine
    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd, database=databse)
    mycur = mydb.cursor()
    mycur.execute("select * from SRM_Telecom")

    myrec = mycur.fetchall()
    for x in myrec:
        cno = x[0]
        cname = x[1]
        mobile = x[2]
        address = x[3]
        email = x[4]
        no_calls = x[5]
        status = x[6]
        print(cno," | ",cname," | ",mobile," | ",address," | ",email," | ",no_calls," | ", status)

    cno = int(input("Enter The Customer no.: "))
    str = "select cno, cname, mobile, address, email, no_calls from SRM_Telecom where cno={}"
    query = str.format(cno)
    mycur.execute(query)

    myrec = mycur.fetchall()
    for x in myrec:
        cno = x[0]
        cname = x[1]
        mobile = x[2]
        address = x[3]
        email = x[4]
        no_calls = x[5]

        a = x[5]

        if a <= 100:
            amt = 200
        elif a <= 150:
            amt = 200 + 0.60 * (a - 100)
        elif a <= 200:
            amt = 200 + 0.60 * 50 + 50 * (a - 150)
        elif a > 200:
            amt = 200 + 0.60 * 50 + 0.50 * 50 + 0.40 * (a - 200)

        tax = round(amt * 0.10, 2)
        net = round(amt + tax, 2)
        print("="*50)
        print("\n","\n","\n")
        print("="*50)
        print("<===\t\tS.R.M Telecom\t\t====>")
        print("=" * 50)
        print("M:- 011563287\t\tBranch:- Jarhi")
        print("="*50)
        print("Customer no. :- ", cno)
        print("Customer name: ", cname)
        print("=" * 50)
        print("Phone no.: ", mobile)
        print("Address: ", address)
        print("=" * 50)
        print("Email id: ", email)
        print("No. of Calls: ", no_calls)
        print("=" * 50)
        print("Your bill is Rs. ", amt)
        print("Gst: Rs. ", tax)
        print("=" * 50)
        print("net amount: Rs. ", net)

def datab():
    myfile = open("D:\\link.txt", 'w')
    usr = input("Enter the user name of MySql")

    passwd = input("Enter the password of MySql")

    databse = input("Enter the name of new database to create")
    list = [usr, passwd, databse]
    for i in list:
        myfile.write(i)
        myfile.write("\n")
    myfile.close()

    mydb = mysql.connector.connect(host="localhost", user=usr, password=passwd)

    mycur = mydb.cursor()
    mycur.execute("create database {}".format(databse))
    table = input("Enter the name of table")
    mycur.execute("use {}".format(databse))
    str = "create table {} (cno int(11) primary key not null,cname varchar(30) not null,mobile int(11) not null,address char(25),email varchar(30),no_calls int(8), status char(5))"
    mycur.execute(str.format(table))

ch = 'y'
while ch.lower()=="y":
    print("==================================================")
    print("<====             S.R.M Telecom              ====>")
    print("==================================================")
    print("Currently using",databse)
    print("CHOICES")
    print("1. To Add New Record")
    print("2. To Search a Record")
    print("3. To Update the Record")
    print("4. To Delete a Record")
    print("5. To View all Records")
    print("6. To Generate The Bill")
    print("7. To Change Database")
    print("==================================================")

    ch = int(input("Enter The Choice: "))

    if ch == 1:
        add()
    elif ch == 2:
        search()
    elif ch == 3:
        edit()
        a= input("want to edit more? y/n :")
        while a=="y":
            edit()
            a= input("want to edit more? y/n :")
    elif ch == 4:
        delete()
    elif ch == 5:
        display()
    elif ch == 6:
        generate()
    elif ch==7:
        datab()
    print("\n\n-------------------------------")
    ch = input("Want to See Main Menu? (y/n):  ")
