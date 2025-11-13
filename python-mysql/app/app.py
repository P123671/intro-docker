import mysql.connector
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='testdb'
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, msg VARCHAR(255))")
    cursor.execute("INSERT INTO visits (msg) VALUES ('Hello from Docker Compose!')")
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM visits")
    count = cursor.fetchone()[0]
    conn.close()
    return f"Visits count: {count}"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)