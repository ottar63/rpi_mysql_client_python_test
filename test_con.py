from flask import Flask,render_template
from flask_table import Table,Col
import pymysql
import socket

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
        sql="INSERT INTO visits (host,ip_address) VALUES ('{}','{}');".format(self.hostname,self.ip)
        #print(sql)
        self.cur.execute(sql)
        self.db.commit()
    def list_visits(self):
        sql="SELECT id , host ,ip_address  FROM visits ORDER BY id DESC"
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


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
