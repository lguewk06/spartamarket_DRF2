## Project name
Sparta Market Implemented with DRF

## Introduction
Let's implement **Sparta Market** using **Django REST Framework (DRF)**!

## Development Period
- **Start Date**: 2024.09.05
- **End Date**: 2024.09.10

## Full Technology Stack Overview
- **Programming Language**: Python 3.10
- **Web Framework**: Django 4.2
- **Database**: SQLite
- **IDE**: VSCode
- **Version Control**: Git, GitHub
- **API Development and Testing**: Postman
- **Technical Stack**:
  - **Backend**: Python, Django REST Framework
  - **Database**: Django ORM, SQLite

<br>

## Key Features

### **Accounts**

#### User Signup:
- **Endpoint**: `/api/accounts`
- **Method**: `POST`
- **Conditions**: Username, password, email, name, nickname, and birthday are required fields; gender and bio are optional.
- **Validation**: Username and email must be unique. Email duplication check is optional.
- **Implementation**: Validates the data and saves it to the database.
![User Signup Example](https://github.com/user-attachments/assets/a2bd195b-df49-43ad-8c54-49f648d7b99d)

#### Login
- **Endpoint**: `/api/accounts/login`
- **Method**: `POST`
- **Conditions**: Username and password are required.
- **Validation**: Username and password must match the records in the database.
- **Implementation**: Issues a token upon successful login and returns an appropriate error message upon failure.
![Login Example](https://github.com/user-attachments/assets/09c7fdd5-ed39-4552-8915-a17ff4a3b8ed)
![Refresh Token Example](https://github.com/user-attachments/assets/a208c2c5-92b8-4565-898b-7ebba485d11d)

#### User Profiles
- **Endpoint**: `/api/accounts/<str:username>`
- **Method**: `GET`
- **Conditions**: Requires user to be logged in.
- **Validation**: Only the logged-in user can view their profile.
- **Implementation**: Returns the logged-in user's profile information in JSON format.
![Profile Example](https://github.com/user-attachments/assets/5c2cbcdc-07c8-4f23-b36f-b3a1b52dd6f3)

### **Products**

#### Product Create
- **Endpoint**: `/api/products`
- **Method**: `POST`
- **Conditions**: User must be logged in, and the product's title, description, and image must be provided.
- **Implementation**: Validates the data and creates a new product in the database.
![Product Create Example](https://github.com/user-attachments/assets/eea74dba-1ec7-4c31-b133-d036e0aa41bf)

#### Product List
- **Endpoint**: `/api/products`
- **Method**: `GET`
- **Conditions**: No login required.
- **Implementation**: Returns a paginated list of all products.
![Product List Example](https://github.com/user-attachments/assets/6c1807ee-959f-470f-b455-6054fb6f7bb0)

#### Product Update
- **Endpoint**: `/api/products/<int:productId>`
- **Method**: `PUT`
- **Conditions**: User must be logged in, and only the user who created the product can update it.
- **Validation**: Checks if the requestor is the creator of the product.
- **Implementation**: Updates the product with the provided information.
![Product Update Example](https://github.com/user-attachments/assets/4a47bf55-a8ae-45ca-a7fe-1872545f431b)

#### Product Delete
- **Endpoint**: `/api/products/<int:productId>`
- **Method**: `DELETE`
- **Conditions**: User must be logged in, and only the user who created the product can delete it.
- **Validation**: Checks if the requestor is the creator of the product.
- **Implementation**: Deletes the product from the database.
![Product Delete Example](https://github.com/user-attachments/assets/7b5fdccd-8558-478a-9898-e79e82b35288)
![Product Deleted Confirmation](https://github.com/user-attachments/assets/ce4e0c20-937c-4068-a998-b40b0f085b87)

### ERD Diagram
![ERD Diagram](https://github.com/user-attachments/assets/ced2a298-bf97-47da-81b3-0f86f89e47f7)

## Folder Structure
```bash
SPARTAMARKET_DRF/
│
├── accounts/           # App handling user authentication and permissions
├── products/           # App managing product-related features
├── spartamarket_DRF/   # Project configuration files (settings.py, etc.)
├── db.sqlite3          # SQLite database file
├── .gitignore          # Files and directories to be ignored by Git
├── manage.py           # Django management command file
├── requirements.txt    # List of dependencies for the project