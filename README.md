# Flask MongoDB API

This repository contains a simple Flask API that interacts with a MongoDB database. The API provides endpoints to manage users (CRUD operations: Create, Read, Update, Delete).
### Key Features:
User Management: The application allows users to be created, updated, retrieved, and deleted through API endpoints. Users are stored in a MongoDB database, providing a scalable and flexible storage solution.

RESTful API: The application follows the principles of a RESTful API, making it easy for developers to interact with and integrate the API into their applications. Endpoints are designed to handle various HTTP methods, such as GET, POST, PUT, and DELETE, for managing user data.

Data Persistence: User data is stored in a MongoDB database, ensuring data persistence and durability. MongoDB's NoSQL nature allows for easy schema changes and adaptability to evolving data requirements.

Secure User Data: Passwords are securely stored in the database using best practices, such as hashing and salting, to protect user information from unauthorized access.

Dockerized Deployment: The application can be easily deployed using Docker, ensuring consistent and reproducible environments across different systems. Docker containers encapsulate the application and its dependencies, making deployment hassle-free.

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

-GET /users/(id): Get a user by their ID.

-POST /users: Create a new user. (JSON data with name, email, and password required)

-PUT /users/(id): Update an existing user by their ID. (JSON data with name, email, and password required)

-DELETE /users/(id): Delete a user by their ID.

