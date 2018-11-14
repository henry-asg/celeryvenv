from celery import Celery
import time

# app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def add(x, y):
    time.sleep(1)
    return x + y
