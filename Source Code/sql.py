import sqlite3
def check(usertype,username,password):
    mycon=sqlite3.connect('db.db')
    c=mycon.cursor()
    if usertype=="admin":
        c.execute("select * from admin where username='{}' and password='{}'".format(username,password))
    else:
        c.execute("select * from entries where reg_no='{}' and uid='{}'".format(username,password))
        pass
    r=c.fetchall()
    return r
def aadhar_data(uid):
    mycon=sqlite3.connect('db.db')
    c=mycon.cursor()
    c.execute("""SELECT UID,first_name||" "||middle_name||" "||last_name,father_firstname||" "||father_middlename||
    " "||father_lastname,mother_firstname||" "||mother_middlename||" "||mother_lastname,address_house||" "||
    address_street||" "||address_city||" "||address_state||" "||address_pin,gender,mobile,DOB FROM AADHAR  where uid='{}'""".format(uid))
    r=c.fetchall()
    return r
def find_summary(column):
    mycon=sqlite3.connect('db.db')
    c=mycon.cursor()
    c.execute("select {},count({}) from aadhar join entries on aadhar.uid=entries.uid group by {}".format(column,column,column))
    r=c.fetchall()
    return r
def reg():
    mycon=sqlite3.connect('db.db')
    c=mycon.cursor()
    c.execute("select max(reg_no) from entries")
    r=c.fetchall()
    if r[0][0] is None:
        return 1
    else:
        return (r[0][0]+1)
def check_entries(uid):
    mycon=sqlite3.connect('db.db')
    c=mycon.cursor()
    c.execute("select uid from entries where uid={}".format(uid))
    r=c.fetchall()
    return len(r)
def insert(values):
    mycon=sqlite3.connect('db.db')
    c=mycon.cursor()
    r="insert into entries values ({},'{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},{})".format(values[0],
    values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],
    values[16],values[17],values[1])
    c.execute(r)
    mycon.commit()