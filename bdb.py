import pymysql

def insert_data(email, pw):
    db = pymysql.connect(host='lycan0512.mysql.pythonanywhere-services.com',
                    user='lycan0512', password='1234',
                    db='lycan0512$20181055_webapp', charset='utf8')
    c = db.cursor()
    setdata = (email, pw)
    c.execute("INSERT INTO user_tb VALUES (%s, %s)", setdata)
    db.commit()

def get_emailpw(email, pw):
    print(email, pw)
    db = pymysql.connect(host='lycan0512.mysql.pythonanywhere-services.com',
                    user='lycan0512', password='1234',
                    db='lycan0512$20181055_webapp', charset='utf8')
    c = db.cursor()
    setdata = (email, pw)
    c.execute("SELECT * FROM user_tb WHERE email = %s AND pw = %s", setdata)
    ret = c.fetchone()
    print(ret)

# insert_data('d@a.com', '4')
# get_emailpw('d@a.com', '41')