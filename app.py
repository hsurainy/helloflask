from flask import Flask
import pymongo,click
app = Flask(__name__)
app.config['show'] = '用户如下:'

@app.route('/')
def index():
    return '<h1>Hello, Flask, First LOOK</h1>'

@app.route('/showusers')
def showusers():
    dbs = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = dbs['flaskdemo']
    col = db['user']
    datas = col.find({})
    res = '<h1>{}</h1>\n'.format(app.config['show'])
    for i,data in enumerate(datas):
        res += "<h2>{}:{}</h2>\n".format(i+1,data['name'])

    return res


#cli command 实现命令行操作
@app.cli.command()
def hello():
    click.echo('Hello')

@app.cli.command()
@click.option('--id')
@click.option('--username')
def add(id,username):
    dbs = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = dbs['flaskdemo']
    col = db['user']
    col.insert_one({"id":int(id),"name":username})
    click.echo('Done!')
