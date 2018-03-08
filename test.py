# Done once for the whole docs
import requests, json
api_root = 'http://localhost:5555/api'
task_api = '{}/task'.format(api_root)
args = {'args': [1, 2]}
url = '{}/async-apply/deepeye.tasks.detect'.format(task_api)
print(url)
resp = requests.post(url, data=json.dumps(args))
reply = resp.json()
print reply

url = '{}/queues/length'.format(api_root)
print(url)
resp = requests.get(url)
print 'Queues length is {}'.format(resp.json())

## Get list
url = '{}/tasks'.format(api_root)
print(url)
payload = {'state': 'STARTED','taskname':'deepeye.tasks.detect'}
resp = requests.get(url,params=payload)
print 'task running is {}'.format(resp.json())


print 'Test block call'
url = '{}/apply/deepeye.tasks.detect'.format(task_api)
print(url)
resp = requests.post(url, data=json.dumps(args))
reply = resp.json()
print reply


url = '{}/queues/length'.format(api_root)
print(url)
resp = requests.get(url)
print 'Queues length is {}'.format(resp.json())
