from flask import Flask, request
import json
import redis
from rq import Queue
from worker.worker import dbCreate,addUser


app = Flask(__name__)

# connect redis container and run rq lib
queue = Queue(connection=redis.Redis(host='redis-service',port=6379))

@app.route('/')
def checkProcess():
    return {
        "code": "success",
        "msg": "process active"
        }

@app.route('/api/user',methods=['POST'])
def saveUser():
    data = request.data.decode("utf-8")
    data = json.loads(data)
    queue.enqueue(addUser,data)
    return {
        "code": "success",
        "msg": "task queued"
        }

if __name__ == "__main__":
    dbCreate() # for first start
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True) # for development server
