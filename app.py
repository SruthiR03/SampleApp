from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.config['MYSQL_USER'] = 'sql3354572'
app.config['MYSQL_PASSWORD'] = 'mRAU99xW7h'
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql3354572'

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO SampleTable (name,email) VALUES(%s,%s)",(name,email))

        mysql.connection.commit()


        cur.close()
        return 'Done!'
    return render_template('index.html')

@app.route('/list',methods=['GET','POST'])
def data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM SampleTable''')
    results = cur.fetchall()
    print(results)

    return jsonify(results)

@app.route('/<name>')
def intro(name):
    return '<h1>Hello {}!</h1>'.format(name)

@app.route('/about')
def about():
    return '<h1>About Page</h1> \n I am a person who is interested in coding'

if __name__ == "main":
    app.run(debug=True)