class Shop:
    def __init__(self, dbname: str):
        self.db = MyDB(dbname)
    
    def push_new_buy(self, item, quantity, package):
        record = item + ' ' +  str(quantity) + ' ' + package
        self.db.add(record)
    
    def __str__(self):
        s = ''
        for el in self.db.output():             
            s += el + " <br>"
        return s
from flask import Flask
from flask import redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(shop) + "ссылочка на добавление"
 
@app.route('/hello')
def hello_world2():
    return 'hello'

@app.route('/pushdata',methods = ['POST', 'GET'])
def push_data():
    if request.method == 'POST':
        item = request.form['item']
        quantity = request.form['quantity']
        package = request.form['package']
        shop.push_new_buy(item, quantity, package)
         
        return redirect('/')
    else:
        return html
