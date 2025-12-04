from flask import Flask, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

def get_db_connection():
    max_retries = 5
    retry_count = 0
    while retry_count < max_retries:
        try:
            conn = psycopg2.connect(
                host=os.environ.get('DB_HOST', 'db'),
                database=os.environ.get('DB_NAME', 'mydb'),
                user=os.environ.get('DB_USER', 'myuser'),
                password=os.environ.get('DB_PASSWORD', 'mypassword')
            )
            return conn
        except psycopg2.OperationalError:
            retry_count += 1
            time.sleep(2)
    raise Exception("Could not connect to database")

def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")

@app.route('/')
def home():
    return '''
    <html>
        <body>
            <h1>Hello, DevOps!</h1>
            <p>Ласкаво просимо до веб-застосунку</p>
            <a href="/messages">Переглянути повідомлення</a>
        </body>
    </html>
    '''

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)