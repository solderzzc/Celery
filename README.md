

WORKER_TYPE=detect celery worker --loglevel INFO -A proj -E -n detect -c 2 -Q detect 
WORKER_TYPE=embedding celery worker --loglevel INFO -A proj -E -n embedding -c 2 -Q embedding
WORKER_TYPE=nopriority celery worker --loglevel INFO -A proj -E -n nopriority -c 2 -Q nopriority

