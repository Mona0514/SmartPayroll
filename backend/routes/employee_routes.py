from flask import Blueprint, request, jsonify
from db import employee_collection

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/add", methods=["POST"])
def add_employee():
    data = request.json
    employee_collection.insert_one(data)
    return jsonify({"message": "Employee added successfully"})

@employee_bp.route("/view", methods=["GET"])
def view_employees():
    employees = list(employee_collection.find({}, {'_id': 0}))
    return jsonify(employees)
