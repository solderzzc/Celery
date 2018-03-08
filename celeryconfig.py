
imports = ('deepeye.tasks',)

broker_url = 'amqp://10.5.52.110'
result_backend = 'rpc://'
worker_pool_restarts = True

task_routes = {
    'deepeye.tasks.detect': {'queue': 'detect'},
    'deepeye.tasks.extract': {'queue': 'embedding'},
    'deepeye.tasks.fullimage': {'queue': 'nopriority'}
}
