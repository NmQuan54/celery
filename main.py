from flask import Flask, request, jsonify
from celery_app import make_celery
from tasks import add, multiply, subtract, divide, send_email

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://redis:6379/0',
    CELERY_RESULT_BACKEND='redis://redis:6379/0'
)

celery = make_celery(app)

@app.route('/send_email', methods=['POST'])
def send_email_api():
    data = request.get_json()
    task = send_email.delay(data['to_email'], data['subject'], data['message'])
    return jsonify({"task_id": task.id}), 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)