import flask

app = flask.Flask(__name__)


def fib(n):
    """Recursive in order to be slow"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


@app.route('/fib')
def hello_world():
    n = flask.request.args.get('n', 10)
    return flask.jsonify({'fib': fib(int(n))})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

