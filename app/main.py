# main.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Ticket
from config import Config
import requests

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)

@app.route('/buy/<int:ticket_id>')
def buy_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if ticket and not ticket.purchased:
        ticket.purchased = True
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/draw')
def draw():
    api_url = 'https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new'
    response = requests.get(api_url)
    if response.status_code == 200:
        winning_number = int(response.text.strip())
        winner = Ticket.query.filter_by(number=winning_number).first()
        return render_template('result.html', winner=winner)
    return 'Error drawing winner', 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if Ticket.query.count() == 0:
            for i in range(1, 101):
                ticket = Ticket(number=i)
                db.session.add(ticket)