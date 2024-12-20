from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='db',  # This is the service name for MySQL in Docker Compose
        user='app_user',
        password='password',
        database='database'
    )
    return connection

# Route to display the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and insert data into the database
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        # Connect to the database and insert the data
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user_data (name, email) VALUES (%s, %s)', (name, email))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('index'))  # Redirect back to the form

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)