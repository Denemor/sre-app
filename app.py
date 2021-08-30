from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def status():
    return jsonify({'status': 'running'})


def main():
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
