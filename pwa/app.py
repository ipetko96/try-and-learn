from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/manifest.json")
def serve_manifest():
    return send_file("manifest.json", mimetype="application/manifest+json")


@app.route('/service-worker.js')
def serve_sw():
    return send_file('service-worker.js', mimetype='application/javascript')
