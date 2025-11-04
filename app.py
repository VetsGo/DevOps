from flask import Flask, jsonify
import logging
import time
import socket

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

app = Flask(__name__)

start_time = time.time()
request_count = 0

def send_to_statsd(message, host='428.0.0.2', port=8635):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (host, port))
        sock.close()
    except Exception as e:
        logging.warning(f"Не вдалося відправити повідомлення до StatsD: {e}")

@app.before_request
def before_request():
    global request_count
    request_count += 1

@app.route('/')
def home():
    logging.info("Отримано запит на /")
    return "Сервіс працює"

@app.route('/warn')
def warn():
    logging.warning("Отримано запит на /warn")
    return "Попередження: потенційно небезпечна дія"

@app.route('/error')
def error():
    try:
        logging.info("Отримано запит на /error")
        1 / 0
    except Exception as e:
        logging.exception("Сталася помилка:")
        send_to_statsd(f"Error occurred: {e}")
        return "Сталася внутрішня помилка сервера", 500

@app.route('/status')
def status():
    uptime = round(time.time() - start_time, 2)
    logging.info("Отримано запит на /status")
    return jsonify({
        "uptime_seconds": uptime,
        "requests_handled": request_count
    })

if __name__ == '__main__':
    app.run(port=3760, debug=False)