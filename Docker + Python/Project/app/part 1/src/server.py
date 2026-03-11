from flask import Flask
server = Flask(__name__)

@server.route("/")
 def hello():
    return "Hello world"

if __name__ == "__main__":
    ### server.run(host='0.0.0.0')
    server.run(debug=True, host='0.0.0.0', port=5000)
import ptvsd
ptvsd.enable_attach(address=('0.0.0.0', 5678))