from flask import Flask,redirect,url_for,render_template,request, jsonify
from connect import todos

app=Flask(__name__)

# Some useful functions 
def get_next_id():
    if todos.count_documents({}) != 0:
        max_id = todos.find().sort([("_id", -1)]).limit(1)
        id = max_id[0]['_id']
        return id + 1
    else:
        return 1

def get_todo(id):
    todo_exist = todos.count_documents({'_id' : id})
    if todo_exist != 0:
        return todos.find({'_id' : id}).limit(1)[0]
    return False

# flask routes

# get all todos in the list 
@app.route('/all',methods=['GET'])
def all():
    todos_list = todos.find()
    todos_list = [todo for todo in todos_list]
    return jsonify(todo=todos_list), 200

# get any todo through its id
@app.route('/<int:id>',methods=['GET'])
def get_todo_with_id(id):
    todo = get_todo(id)
    if todo:
        return jsonify(todo=todo), 200
    return jsonify(error = "No TODO with this id"), 404

# add a new todo in the list 
@app.route('/add', methods=['POST'])
def add_todo():
    todo_name = request.form.get("todo_name")
    todo_desc = request.form.get("todo_desc")
    new_todo = {
        "_id" : get_next_id(),
        "name" : todo_name,
        "desc" : todo_desc
    }
    todos.insert_one(new_todo)
    return jsonify(success = "TODO has been added")

# delete a todo using id
@app.route("/delete/<int:id>", methods=["delete"])
def delete_todo(id):
    if get_todo(id):
        todos.delete_one({"_id" : id})
        return jsonify(success="TODO succesfully deleted")
    return jsonify(error = "No TODO with this id"), 404

# edit a todo
@app.route("/edit/<int:id>", methods=["PUT", "GET"])
def edit_todo(id):
    todo = get_todo(id)
    if todo:
        if request.method == "GET":
            return jsonify(todo=todo)
        else:
            new_todo = {
                "_id" : id,
                "name" : request.form.get("todo_name"),
                "desc" : request.form.get("todo_desc")
            }
            todos.update_one({"_id" : id},{"$set" : new_todo})
            return jsonify(success="TODO succesfully updated")
    else:
        return jsonify(error = "No TODO with this id"), 404


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)