from flask import json, jsonify
from app import app
from app import db
from app.models import Menu

@app.route('/')
def home():
	return jsonify({ "status": "ok" })

@app.route('/menu')
def menu():
    today = Menu.query.all()
    if today:
        body = []
        for obj in today:
            body += [{ "today_special": obj.name, "price":obj.price, "quantity":obj.quantity }]

        status = 200
    else:
        body = { "error": "Sorry, the service is not available today." }
        status = 404
    return jsonify(body), status