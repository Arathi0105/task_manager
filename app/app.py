#importing flask , render_template is used to open the html file, request is used to get the input from the user

from flask import Flask, render_template,request

#create a Flask Instance
app = Flask(__name__, static_folder='static')

task= []  #to store the inputs

#create a route decorator
@app.route('/',methods=['GET'])
def home():
    return render_template("home.html")
    

@app.route('/add-task')
def add_task():
    return render_template("add_task.html")

@app.route('/tasks', methods=['POST'])
def tasks():
    # Get data from the form
    task_name = request.form.get('task_name')  # Get task name
    status = request.form.get('status')        # Get status (radio button value)
    task_date = request.form.get('task_date')  # Get date (selected by user)

    # Append the task to the list
    task.append({'name': task_name, 'date': task_date, 'status': status})

    # Redirect to the task list or render a success page
    return render_template('task.html', task=task)




if __name__ == '__main__':
    app.run(debug=True)