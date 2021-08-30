from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from config import Config

app = Flask(__name__)
app.config.from_object(Config.init_app(app=app))
metrics = PrometheusMetrics(app=app)


@app.route('/')
def status():
    return jsonify({'status': 'running'})


def main():
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
