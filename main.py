from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'smashhhh,, BIG SLAYYY'

app.run(host='0.0.0.0', port=81)