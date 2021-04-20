from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://myuser:2003@localhost/iot-test-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Insurance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    duration_in_months = db.Column(db.Integer, unique=True)
    min_insurance_sum = db.Column(db.Integer, unique=True)
    risk_level = db.Column(db.Integer, unique=True)

    def __init__(self, name: str, duration_in_months: int, min_insurance_sum: float, risk_level: int):
        self.name = name
        self.duration_in_months = duration_in_months
        self.min_insurance_sum = min_insurance_sum
        self.risk_level = risk_level


class InsuranceSchema(ma.Schema):
    name = fields.String()
    duration_in_months = fields.Integer()
    min_insurance_sum = fields.Integer()
    risk_level = fields.Integer()


insurance_schema = InsuranceSchema()
insurances_schema = InsuranceSchema(many=True)


@app.route('/insurance', methods=["POST"])
def add_insurance():
    name = request.json['name']
    duration_in_months = request.json['duration_in_months']
    min_insurance_sum = request.json['min_insurance_sum']
    risk_level = request.json['risk_level']

    new_insurance = Insurance(name, duration_in_months, min_insurance_sum, risk_level)

    db.session.add(new_insurance)
    db.session.commit()

    return jsonify(new_insurance)


@app.route("/insurance", methods=["GET"])
def get_insurance():
    all_insurances = Insurance.query.all()
    result = insurances_schema.dump(all_insurances)
    return jsonify(result)


@app.route("/insurance/<id>", methods=["GET"])
def insurance_detail(id):
    insurance = Insurance.query.get(id)
    return insurance_schema.jsonify(insurance)


@app.route("/insurance/<id>", methods=["PUT"])
def insurance_update(id):
    insurance = Insurance.query.get(id)
    name = request.json['name']
    duration_in_months = request.json['duration_in_months']
    min_insurance_sum = request.json['min_insurance_sum']
    risk_level = request.json['risk_level']

    insurance.name = name
    insurance.duration_in_months = duration_in_months
    insurance.min_insurance_sum = min_insurance_sum
    insurance.risk_level = risk_level

    db.session.commit()
    return insurance_schema.jsonify(insurance)


@app.route("/insurance/<id>", methods=["DELETE"])
def insurance_delete(id):
    insurance = Insurance.query.get(id)
    db.session.delete(insurance)
    db.session.commit()

    return insurance_schema.jsonify(insurance)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
