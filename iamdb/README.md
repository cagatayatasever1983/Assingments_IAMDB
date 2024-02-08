# I am Db

I am Db is a Python based REST API that provides information on movies and the people that work on them. Although currently somewhat lacking in features and database entries, we plan to ramp up development soon!

## Requirements
- Python 3.
- Pip.
- Pipenv.

## Introduction
I am Db is designed to run on Linux or Mac. If you are using a Windows machine, we recommend using Git Bash or a similar Linux terminal emulator. 

Feel free to browse through the application's source code, but assume that the application will quickly become far more complex as development progresses. The test suite should be able to guarantee the application's functioning even if the underlying code changes and becomes less predictable. 

A full description of all API calls currently supported by the application can be found in `apidocs.md`.

## Getting started
Navigate to the project's home directory in a terminal. 

`sh resetdb.sh`
Populates the database with some basic (test) values. Can also be used to reset the database to these same values.

`pipenv install`
Install the project's required dependencies. 

`pipenv run python src/app.py` 
Start the API service.

`pipenv run pytest` 
Trigger the test suite. 

If all goes well, the result of the test suite should be a single passing test. 
