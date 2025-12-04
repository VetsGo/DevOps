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

@app.route('/messages')
def messages():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("INSERT INTO messages (content) VALUES (%s) RETURNING id", 
                   (f"Запит виконано",))
        new_id = cur.fetchone()[0]
        conn.commit()
        
        cur.execute("SELECT id, content, created_at FROM messages ORDER BY created_at DESC LIMIT 10")
        rows = cur.fetchall()
        
        cur.close()
        conn.close()
        
        messages_list = []
        for row in rows:
            messages_list.append({
                'id': row[0],
                'content': row[1],
                'created_at': str(row[2])
            })
        
        html = '<html><body><h1>Список повідомлень</h1><ul>'
        for msg in messages_list:
            html += f'<li>ID: {msg["id"]}, Текст: {msg["content"]}, Час: {msg["created_at"]}</li>'
        html += '</ul><a href="/">На головну</a></body></html>'
        
        return html
    except Exception as e:
        return f'<html><body><h1>Помилка</h1><p>{str(e)}</p><a href="/">На головну</a></body></html>'

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)