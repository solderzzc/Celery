
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

### Result on Dashboard

http://localhost:5555/dashboard

![screen shot 2018-03-06 at 7 28 49 pm](https://user-images.githubusercontent.com/3085564/37072135-b93e680c-2174-11e8-954f-632570f1757c.png)
![screen shot 2018-03-06 at 7 28 38 pm](https://user-images.githubusercontent.com/3085564/37072138-baca5032-2174-11e8-90d6-57c7ce29fe27.png)
