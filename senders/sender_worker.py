from celery_app import app


@app.task(name="send_email", acks_late=True)
def send_email(to: any, data: any):
    print("Sended email")
