# Done once for the whole docs
import requests, json
api_root = 'http://localhost:5555/api'
task_api = '{}/task'.format(api_root)
args = {'args': [1, 2]}
url = '{}/async-apply/tasks.add'.format(task_api)
print(url)
resp = requests.post(url, data=json.dumps(args))
reply = resp.json()
print reply
