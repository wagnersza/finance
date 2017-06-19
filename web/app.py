from flask import Flask
from redis import Redis
from flask import request
from flask import render_template

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/')
# def hello():
#     count = redis.incr('hits')
#     redis.set('foo','20')
#     ap = redis.get('foo')
#     count = int(count)*int(ap)
#     first_name = request.values.get("firstname")
#
#     return 'Hello World! I have been seen {} {} times.\n'.format(count,ap)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
