from flask import Flask, render_template

app = Flask(__name__)

# Flag to control data streaming
streaming = False

# Example live data
live_data = "Initial data"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_stream')
def start_stream():
    global streaming
    streaming = True
    return "Streaming started"

@app.route('/stop_stream')
def stop_stream():
    global streaming
    streaming = False
    return "Streaming stopped"

@app.route('/get_data')
def get_data():
    global live_data
    if streaming:
        # Replace this with your code to fetch live data from the server
        live_data = "Live data from server"  # Example live data
        return live_data
    else:
        return "Streaming not started"

if __name__ == "__main__":
    app.run(debug=True)
