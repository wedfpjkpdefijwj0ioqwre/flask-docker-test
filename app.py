from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f'Hello from Docker!<br>Connected to: {db_version}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
