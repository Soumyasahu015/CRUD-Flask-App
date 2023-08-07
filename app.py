# app.py
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Set the MongoDB URI and database name in the Flask application configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
client = MongoClient(app.config['MONGO_URI'])
db = client.get_database()

# Create the necessary routes and functions for the REST API endpoints

# GET /users - Returns a list of all users.
@app.route('/')
def home():
    return "Welcome to the Flask MongoDB API!"

@app.route('/users', methods=['GET'])
def get_users():
    users = db.users.find()
    result = []
    for user in users:
        result.append({'id': str(user['_id']), 'name': user['name'], 'email': user['email']})
    return jsonify(result)

# GET /users/<id> - Returns the user with the specified ID.
@app.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    user = db.users.find_one({'_id': ObjectId(id)})
    if user is None:
        return jsonify({'message': 'User not found.'}), 404

    return jsonify({'id': str(user['_id']), 'name': user['name'], 'email': user['email']})


# POST /users - Creates a new user with the specified data.
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }
    user_id = db.users.insert_one(new_user).inserted_id
    return jsonify({'id': str(user_id), 'message': 'User created successfully.'})

# PUT /users/<id> - Updates the user with the specified ID with the new data.
@app.route('/users/<string:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    updated_user = {
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }
    db.users.update_one({'_id': ObjectId(id)}, {'$set': updated_user})
    return jsonify({'message': 'User updated successfully.'})

# DELETE /users/<id> - Deletes the user with the specified ID.
@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    db.users.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User deleted successfully.'})

if __name__ == '__main__':
    app.run(debug=True)
