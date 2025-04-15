from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["smart_payroll"]
employee_collection = db["employees"]
