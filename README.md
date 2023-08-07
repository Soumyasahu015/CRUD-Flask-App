# Flask MongoDB API

This repository contains a simple Flask API that interacts with a MongoDB database. The API provides endpoints to manage users (CRUD operations: Create, Read, Update, Delete).

## Getting Started

Follow the instructions below to set up and run the application on your local machine.

### Prerequisites

Before running the application, you need to have the following installed:

1. Docker Desktop: Ensure you have Docker Desktop installed and running on your machine.

### Installation

1. Clone the repository to your local machine:
   git clone https://github.com/your-username/your-repo.git
   
Navigate to the project directory:
cd your-repo


### Configuration
In the docker-compose.yml file, make sure the MONGO_URI environment variable points to your MongoDB instance. By default, it is set to mongodb://mongodb:27017/mydatabase, assuming you have a MongoDB instance running in a Docker container.
### Build and Run
1. Build the Docker containers:
docker-compose build
2. Start the application:
docker-compose up -d
The API will be available at http://localhost:5000.

3. To stop the application, run:
docker-compose down

### API Endpoints
-GET /users: Get a list of all users.

-GET /users/<id>: Get a user by their ID.

-POST /users: Create a new user. (JSON data with name, email, and password required)

-PUT /users/<id>: Update an existing user by their ID. (JSON data with name, email, and password required)

-DELETE /users/<id>: Delete a user by their ID.

