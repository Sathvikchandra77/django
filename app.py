from flask import Flask
import subprocess
from datetime import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    top_output = subprocess.getoutput("top -n 1 -b")
    
    response = f"""
    <h1>Name: Thummala Sathvik Chandra</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <h3>TOP Output:</h3>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

