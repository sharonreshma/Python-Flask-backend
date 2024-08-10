from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123sharon'
app.config['MYSQL_DB'] = 'registration_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    full_name = request.form['full_name']
    email = request.form['email']
    gender = request.form['gender']
    country = request.form['country']
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO users (full_name, email, gender, country) VALUES (%s, %s, %s, %s)', (full_name, email, gender, country))
    mysql.connection.commit()
    cursor.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
