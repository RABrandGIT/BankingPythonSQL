from pymysql import connect
import os

connection = connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utf8mb4')

try:
    with connection.cursor() as cursor:
        query = 'SELECT * FROM user'
        cursor.execute(query)
    connection.commit()

    with connection.cursor() as cursor:
        query = 'SELECT * FROM accounts;'
        cursor.execute(query)
        result = cursor.fetchall()
finally:
        connection.close()
    

connection = connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utf8mb4')


def AccountCreation():
    first_name = str(input("Enter your first name: ",))
    last_name = str(input("Enter your last name: ",))
    check = False
    while check == False:
        password = str(input("Enter your password: ",))
        password2 = str(input("Reenter your password: ",))
        if password == password2:
            check = True
    address = str(input("Enter your email address: ",))

    query = "INSERT INTO user (firstname,lastname,password,email) VALUES(%s,%s,%s,%s)"
    query2 = (first_name,last_name,password,address)
    query3 = "INSERT INTO accounts (balance) VALUES(%s)"
    query4 = (0.00)
    with connection.cursor() as cursor:
        cursor.execute(query,query2)
        cursor.execute(query3,query4)
    connection.commit()

    print("Account has been created") 
    

def Deposit():
    amount = input("How much would you like to deposit?: ",)

def Withdraw():
    amount = input("How much would you like to withdraw?: ",)

def Login():
    Success = False
    while Success == False:
        email = str(input("Enter your email: ",))
        password = str(input("Enter your password: ",))
        with connection.cursor() as cursor:
            cursor.execute("SELECT password FROM user WHERE email = '%s'" % email)
            pulled_pass = cursor.fetchall()
        pulled_pass = pulled_pass[0]
        pulled_pass = pulled_pass[0]
        if pulled_pass == password:
            print("Login successful")
            Success = True
            with connection.cursor() as cursor:
                cursor.execute("SELECT accountnumber FROM user WHERE email = '%s'" % email)
                account_ID = cursor.fetchall()
                account_ID = account_ID[0]
                account_ID = account_ID[0]
             
        else:
            print("Login unsuccessful")
    return Success, account_ID

def Details(ID):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM accounts WHERE accountnumber = '%s'" % ID)
        details = cursor.fetchall()
        print(details)
        
    
    
                   
    
    
    

action = int(input("Press 1 to:Create Account\nPress 2 to:Login\n"))

if action == 1:
    AccountCreation()
if action == 2:
    result = Login()
    if result[0] == True:
        account = result[1]
        action = int(input("Press 1 to: View Account Details\nPress 2 to: Deposit\nPress 3 to: Withdraw\nPress 4 to: exit "))
        if action == 1:
            Details(account)
        elif action == 2:
            Deposit()
        elif action == 3:
            Withdraw()
        elif action == 4:
            exit()

            
    

        
    
    



