# User and User Group Management API

This project provides a REST API with Python and Django to manage users and user groups, allowing clients to perform CRUD operations on users and groups, and associate users with groups.

## Features
- **User Management**: Create, update, delete and select users.
- **Group Management**: Create, update, delete and select groups.
- **Association**: Add or remove users from groups.

## Prerequisites
Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Setup

### 1. Clone the Repository
```bash
git clone <https://github.com/majroit/usergroup>
cd <usergroup>

```bash
docker-compose up --build

run project: 
```bash
http://localhost:8000/api

you can migrate for default data:
```bash
docker-compose exec web python manage.py migrate

## API Endpoints

The following are the key API endpoints available in this project:

### Users
- **GET /api/users/**: Retrieve a list of all users.
- **POST /api/users/**: Create a new user.
- **GET /api/users/{id}/**: Retrieve a specific user by ID.
- **PUT /api/users/{id}/**: Update a user.
- **DELETE /api/users/{id}/**: Delete a user.

### Groups
- **GET /api/groups/**: Retrieve a list of all groups.
- **POST /api/groups/**: Create a new group.
- **GET /api/groups/{id}/**: Retrieve a specific group by ID.
- **PUT /api/groups/{id}/**: Update a group.
- **DELETE /api/groups/{id}/**: Delete a group.

### User-Group Management
- **POST /api/groups/{group_id}/add_user/**: Add a user to a group.
- **POST /api/groups/{group_id}/remove_user/**: Remove a user from a group.

### Swagger API Documentation
Swagger API documentation is available for easy reference. Visit the following URL to explore the API via the Swagger UI:
```bash
http://localhost:8000/swagger/


