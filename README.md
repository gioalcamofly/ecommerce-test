# ecommerce

## Requirements

- Python 3.8
- Docker

## Basic usage

1. Clone this repo
2. Enter the repository folder and create a virtual environment: `python3 -m venv venv`
3. Activate the newly created environment: `source venv/bin/activate`
4. Install the needed packages: `pip install -r requirements`
5. Copy the `.env.example` file into `.env` and fill it with your database credentials. Note that you can specify a different database for testing purposes
6. Run the migrations: `python3 manage.py migrate`
7. Execute it with `python3 manage.py runserver`

Now, you can access the application through `localhost:8000` (api is under `localhost:8000/api/v1`)

Note: You can use ecommerce.postman_collection.json file to test the endpoints on Postman. If you need the data files, they are stored under `data` folder.

### With Docker

1. Build the docker image using the Dockerfile: `docker build . -t [TAG_NAME]`
2. Run the docker container: `sudo docker run -d -p 8080:8000 -v src:/app [TAG_NAME]`

Now, the app will be available through `localhost:8000` 

### Run the tests

1. To run the tests, execute the following command: `python3 manage.py test`


## Development choices I made

### Project configuration

For the project configuration, I think it's better if I have different configuration files for different environments. That is why I splited the configuration between base file (configuration needed for all environments) and development and production configuration files.

At the beginning I thought it would be useful too to have a testing configuration I could use with the command `manage.py test --settings=testing`. However, in the end I found it better to control that on base configuration with `if sys.argv == 'test'`. The reason for that is that I only wanted to change the database, so I found the implemented way more secure: With the first approach, if someone executes the tests without changing settings, the tests will run on main database, which is not preferable.

### CRUD

Although it was not mandatory, I decided to create CRUD endpoints for the different models, just to deliver a more complete project.

### Input Data

I was having problems with the original data, which had 0 indexes, so I decided to assign to every 0 index a new index, so the database could handle it properly.

## Improvements

These are some features that could be implemented, but not necessarily required for the scope of this assignment, so I just focused on other areas.

1. Testing could be better. The returned files can be tested to see if the content is alright (not just the headers), and the uploaded files test can also test if the data is actually uploaded.

2. Uploaders. In `reports_service`, there are some uploaders methods. These method could be implemented using classes and inheritance. That way, the uploading phase could be even more complete in case it was needed

3. Upload Product. In this method, I was having problems with `get_or_create` from `django.models`. It was returning an error for duplicate key, which is contrary to the meaning of the method: if it exists, return it; if not, create it. I couldn't solve it so followed another approach. Anyways, it will be nice to solve this.

4. Validate input file columns. Validate that the columns are the required ones.