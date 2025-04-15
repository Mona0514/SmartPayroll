from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://batchumonasahasra22csm:sara0514@cluster0.lmldqog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["smart_payroll"]
employees_col = db["employees"]
users_col = db["users"]
print("Connected to MongoDB:", db.list_collection_names())


@app.route('/')
def home():
    return render_template('signup.html')
@app.route('/home')
def homee():
    return render_template('index.html')

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']
        employees_col.insert_one({
            'name': name,
            'position': position,
            'salary': salary
        })
        return redirect(url_for('view_employees'))
    return render_template('add_employee.html')

@app.route('/view_employees')
def view_employees():
    employees = list(employees_col.find())
    return render_template('view_employees.html', employees=employees)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = employees_col.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']
        employees_col.update_one({'_id': ObjectId(id)}, {'$set': {
            'name': name,
            'position': position,
            'salary': salary
        }})
        return redirect(url_for('view_employees'))
    return render_template('edit.html', employee=employee)

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_employee(id):
    employee = employees_col.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        employees_col.delete_one({'_id': ObjectId(id)})
        return redirect(url_for('view_employees'))
    return render_template('delete.html', employee=employee)

@app.route('/calculate_salary', methods=['GET', 'POST'])
def calculate_salary():
    employees = list(employees_col.find())
    selected_employee = None
    if request.method == 'POST':
        emp_id = request.form['employee_id']
        selected_employee = employees_col.find_one({'_id': ObjectId(emp_id)})
    return render_template('calculate_salary.html', employees=employees, selected_employee=selected_employee, salary=selected_employee['salary'] if selected_employee else None)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users_col.insert_one({'username': username, 'password': password})
        return render_template('index.html')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_col.find_one({'username': username, 'password': password})
        if user:
            return render_template('index.html')
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
