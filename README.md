
### Run RabbitMQ

```
docker run -d --net=host arm64v8/rabbitmq:3
```

### Modify IP

https://github.com/solderzzc/Celery/blob/master/tasks.py#L6

### Install flower Celery

```
pip install flower celery
```

### Run Test

```
celery worker --loglevel INFO -A tasks -E -c 5
```
Open New terminal

```
celery flower -A tasks
```

```
python test.py
```
