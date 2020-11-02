import os
from flask import jsonify, Blueprint
from . import api
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required,
    get_jwt_identity, get_raw_jwt
)


prefix = '/'+str(os.path.basename(__file__)).replace('.py','')

@api.route(prefix+'/list', methods=['GET'])
@jwt_required
def estimate_g():
  return jsonify({
    'logs': [
      {
        'id': 1,
        'data':"test"
      },
      {
        'id': 2,
        'data':"test2"
      }
    ]
    })

@api.route(prefix+'/new', methods=['POST'])
@jwt_required
def master_n():
  return jsonify({'test':"test"})

@api.route(prefix+'/edit', methods=['POST'])
@jwt_required
def master_p():
  return jsonify({'test':"test"})

@api.route(prefix+'/delete', methods=['DELETE'])
@jwt_required
def master_d():
  return jsonify({'test':"test"})

# @app.route('/incomes')
# def get_incomes():
#   schema = IncomeSchema(many=True)
#   incomes = schema.dump(
#     filter(lambda t: t.type == TransactionType.INCOME, transactions)
#   )
#   return jsonify(incomes.data)


# @app.route('/incomes', methods=['POST'])
# def add_income():
#   income = IncomeSchema().load(request.get_json())
#   transactions.append(income.data)
#   return "", 204


# @app.route('/expenses')
# def get_expenses():
#   schema = ExpenseSchema(many=True)
#   expenses = schema.dump(
#       filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
#   )
#   return jsonify(expenses.data)


# @app.route('/expenses', methods=['POST'])
# def add_expense():
#   expense = ExpenseSchema().load(request.get_json())
#   transactions.append(expense.data)
#   return "", 204