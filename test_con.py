from flask import Flask,render_template,request
from flask_table import Table,Col
import pymysql
import socket
import os
import sys

app=Flask(__name__)
class VisitTable(Table):
    id=Col('Nr')
    host=Col('Host')
    ip_address=Col('IP')

class db_test:
    def __init__(self):
        self.db=pymysql.connect(host='server',user='docker_test',password='docker_password',db='docker_test')
        self.cur=self.db.cursor()
        self.hostname=socket.gethostname()
        self.ip=socket.gethostbyname(socket.getfqdn())
        sql="INSERT INTO visits (host,ip_address,date_time) VALUES ('{}','{}',NOW());".format(self.hostname,self.ip)
        #print(sql)
        self.cur.execute(sql)
        self.db.commit()
    def list_visits(self):
        sql="SELECT id , host ,ip_address, date_time  FROM visits ORDER BY id DESC"
        print(sql)
        self.cur.execute(sql)
        self.visits=[]
        self.visits=self.cur.fetchall()
        self.db.close()
        return self.visits

@app.route('/')
def hello():
    mytest = db_test()
    visits=mytest.list_visits()
    visit_table=VisitTable(visits)    
    return render_template('visits.html', visits=visits)
@app.route('/env')
def env():
    env=os.environ
    print("env:{}".format(env))
    sys.stdout.flush()
    return render_template('env.html',env=env)
@app.route('/req')
def req():
    req=request.environ
    print("req:{}".format(req))
    sys.stdout.flush()
    return render_template('req.html',req=req)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
