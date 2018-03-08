from __future__ import absolute_import
from celery import Celery
from celery import Task
from billiard import current_process

from time import sleep
from celery.signals import worker_process_init
from celery.signals import celeryd_after_setup
from celery.concurrency import asynpool

import os

asynpool.PROC_ALIVE_TIMEOUT = 60.0 #set this long enough

workai = Celery()
workai.config_from_object({
    'name':'workai',
    'BROKER_URL': 'amqp://10.5.52.110',
    'CELERY_RESULT_BACKEND': 'rpc://',
    'CELERYD_POOL_RESTARTS': True,  # Required for /worker/pool/restart API
})
workai.count = 1
def getQueueName():
    return os.environ['WORKER_TYPE']
@worker_process_init.connect()
def setup(sender=None, **kwargs):
    print('initializing {}'.format(getQueueName()))
    sleep(20)
    # setup
    print('done initializing <<< ==== be called Per Fork/Process')


class FaceDetectorTask(Task):
    def __init__(self):
        print('initializing face detector, load module <<< ==== be called Per Worker')
        self._model = 'testing'
    def detector(self):
        return self._model

@workai.task(base=FaceDetectorTask)
def add(x, y):
    return x + y

@workai.task
def sub(x, y):
    sleep(30)  # Simulate work
    return x -  y
