from flask import Flask, render_template, Response, request
app = Flask(__name__)


@app.route('/')
def drone_but():
    return render_template('drone_but.html')
@app.route('/drone', methods=['GET'])
def drone_go():
    return open("Drone/Start_Drone.py")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000, threaded=True)