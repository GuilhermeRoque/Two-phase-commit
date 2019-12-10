from flask import Flask, jsonify
from flask import abort
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
import requests
import random

auth = HTTPBasicAuth()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

trans = {}

mode = 'replica'

class Replica(db.Model):
    __tablename__ = "Replica"
    id = db.Column(db.String(40), primary_key=True)
    endpoint = db.Column(db.String(40), index=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.pop('id')
        self.endpoint = kwargs.pop('endpoint')

    def __repr__(self):
        return '<Replica {}>'.format(self.id)

    def to_json(self):
        return {'id': self.id, 'endpoint': self.endpoint}


class Account(db.Model):
    # __tablename__ = "Account"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, index=True)
    transactions = db.relationship('Transaction', backref='account', lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.balance = kwargs.pop('balance')

    def __repr__(self):
        return '<Account {}>'.format(self.id)

    def to_json(self):
        return {'id': self.id, 'balance': self.balance}


class Transaction(db.Model):
    # __tablename__ = "Transaction"
    id = db.Column(db.String(40), primary_key=True)
    operation = db.Column(db.String(40), index=True)
    value = db.Column(db.Integer, index=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.operation = kwargs.pop('operation')
        self.value = kwargs.pop('value')
        self.account_id = kwargs.pop('account_id')

    def __repr__(self):
        return '<Transaction {}>'.format(self.id)

    def to_json(self):
        return {'id': self.id, 'operation': self.operation, 'value': self.value, 'account_id': self.account_id}



@app.route('/accounts', methods=['GET'])
def account():
    accounts = Account.query.all()
    accounts_list = []
    for account in accounts:
        accounts_list.append(account.to_json())
    return jsonify({'accounts': accounts_list})


@app.route('/replicas', methods=['GET', 'POST', 'DELETE'])
def replica():
    if request.method == 'GET':
        replicas = Replica.query.all()
        replicas_list = []
        for replica in replicas:
            replicas_list.append(replica.to_json())
        return jsonify({'replicas': replicas_list})
    elif request.method == 'POST':
        if not request.json:
            abort(400)
        replicas = request.json.get("replicas")
        for replica in replicas:
            r = Replica(id=replica.get('id'), endpoint=replica.get('endpoint'))
            db.session.add(r)
        mode = "coordinator"
        db.session.commit()
        return jsonify({'replicas': replicas}), 201
    else:
        Replica.query.delete()
        mode = "replica"
        db.session.commit()
        return '', 200


@app.route('/transaction', methods=['PUT','GET'])
def transaction():
    if request.method == 'PUT':
        if not request.json:
            abort(400)
        transaction = request.json
        replicas = Replica.query.all()
        replicas_len = len(Replica.query.all())
        for replica in replicas:
            url = replica.endpoint + '/action'
            r = requests.post(url=url, json=transaction)
            if r.status_code == 200:
                replicas_len -= 1
        if replicas_len == 0:
            for replica in replicas:
                url = replica.endpoint + '/decision'
                requests.put(url=url, json={'id': transaction.get('id')})
                t1 = Transaction(id=transaction.get('id'), operation=transaction.get('operation'),
                                 value=transaction.get('value'), account_id=transaction.get('account'))
            a = Account.query.filter(Account.id == t1.account_id);
            if t1.operation == "withdrawal":
                a.balance -= t1.value
            elif t1.operation == "deposit":
                a.balance += t1.value
            db.session.add(t1)
            try:
                db.session.commit()
            except:
                pass
            return '', 201
        else:
            for replica in replicas:
                url = replica.endpoint + '/decision'
                requests.delete(url=url, json={'id': transaction.get('id')})
            return '', 403
    if request.method == 'GET':
        t = Transaction.query.all()
        j = []
        for t1 in t:
            j.append({'id': t1.id, 'status': 'success'})

        for t1 in trans:
            j.append({'id': t1, 'status': 'fail'})
        return jsonify({'actions': j})

@app.route('/action', methods=['POST'])
def action():
    if request.method == 'POST':
        if not request.json:
            abort(400)

        t = request.json
        if not t.get('id') in trans:
            trans[t.get('id')] = t

        l = [True, True, True, True, True, True, True, False, False, False]
        choice = random.choice(l)
        if choice:
            return '', 200
        else:
            return '', 403
    return '', 200


@app.route('/decision', methods=['PUT', 'DELETE'])
def decision():
    if mode == "coordinator":
        return '', 400
    if request.method == 'PUT':
        if not request.json:
            abort(400)

        transaction = None
        if (request.json.get('id') in trans):
            transaction = trans.get(request.json.get('id'))
            trans.pop(request.json.get('id'))
        else:
            return '', 200


        t1 = Transaction(id=transaction.get('id'), operation=transaction.get('operation'),
                         value=transaction.get('value'), account_id=transaction.get('account'))
        db.session.add(t1)
        try:
            db.session.commit()
        except:
            pass
        return '', 200

    if request.method == 'DELETE':
        if not request.json or 'id' not in request.json:
            abort(404)

        return '', 200




@app.route('/seed', methods=['POST'])
def seed():
    if not request.json or not 'seed' in request.json:
        abort(400)
    seed = request.json.get('seed')
    random.seed(seed)
    return '', 200

def create_db():
    db.create_all()
    acc1 = Account(balance=500)
    acc2 = Account(balance=1500)
    db.session.add(acc1)
    db.session.add(acc2)
    db.session.commit()

if __name__ == '__main__':
    create_db()
    print("Running as ", mode)
    app.run(host='0.0.0.0',debug=True, port=5500)
