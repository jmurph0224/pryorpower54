from flask import Flask, Request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return open('static\index.html').read()

@app.route('/schedule', methods=['POST'])
def schedule():
    data = Request.json
    date = data['date']
    time_slot = data['timeSlot']

    # Database interaction
    conn = sqlite3.connect('appointments.db')
    c = conn.cursor()
    c.execute("INSERT INTO appointments (date, time_slot) VALUES (?, ?)", (date, time_slot))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Appointment scheduled'})

if __name__ == '__main__':
    app.run()
