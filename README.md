### Run RabbitMQ

```
docker run -d --net=host arm64v8/rabbitmq:3
```
### Enable RabbitMQ Plugin in rabbitmy runtime (in docker for such case)
```
rabbitmq-plugins enable rabbitmq_management
service rabbitmq-server restart
```

### Modify IP

https://github.com/solderzzc/Celery/blob/master/celeryconfig.py

### Install flower Celery

```
pip install flower celery
```

### Run Test

```
WORKER_TYPE=detect celery worker --loglevel INFO -E -n detect -c 2 -Q detect

WORKER_TYPE=embedding celery worker --loglevel INFO -E -n embedding -c 2 -Q embedding

WORKER_TYPE=nopriority celery worker --loglevel INFO -E -n nopriority -c 2 -Q nopriority

```
Open New terminal

```
celery flower
```

```
python test.py
```

### Result on Dashboard

http://localhost:5555/dashboard

![screen shot 2018-03-06 at 7 28 49 pm](https://user-images.githubusercontent.com/3085564/37072135-b93e680c-2174-11e8-954f-632570f1757c.png)
![screen shot 2018-03-06 at 7 28 38 pm](https://user-images.githubusercontent.com/3085564/37072138-baca5032-2174-11e8-90d6-57c7ce29fe27.png)
