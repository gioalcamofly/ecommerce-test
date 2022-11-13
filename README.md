# ecommerce

## Requirements

- Python 3.8

## Basic usage

1. Clone this repo
2. Enter the repository folder and create a virtual environment: `python3 -m venv venv`
3. Activate the newly created environment: `source venv/bin/activate`
4. Install the needed packages: `pip install -r requirements`
5. Copy the `.env.example` file into `.env` and fill it with your database credentials
6. Run the migrations: `python3 manage.py migrate`
7. Execute it with `python3 manage.py runserver`

Note: You can use ecommerce.postman_collection.json file to test the endpoints on Postman. If you need the data files, they are stored under `data` folder.

## ToDo

- Refactor
- Test endpoints
- Dockerize