## DOCTALK
<p>Web chat application aimed at enhacing communication between healthcare proffessionals and patients.
This is the backend side</p>

### STARTING THE PROJECT
- Clone the repository to your local environment `git clone repo`
- Install the dependencies, run `pip install -r requirements.txt`
- Navigate to the backend branch `git checkout backend`
- Navigate to the Backend folder `cd Backend`
- Select the environment you're working with before starting the application. On the terminal, run `export FLASK_ENV=development` or `export FLASK_ENV=production`. The default environment is testing. 
- Each environment creates its own database, make sure you're on the correct environment. The test runs clears the database when a new run is made.
- Run `main.py`
- To run the test modules, navigate to the Backend folder and run `python -m unittest discover` for all test modules or `python -m unittest tests/test_file.py` for a specific module

### AUTHORS
1.[Robert Ndung'u](https://github.com/doni-robert) - Backend Developer

2.[Rehema Owino](https://github.com/R-Owino) - Backend Developer


### FRAMEWORK AND LIBRARIES
- Flask Framework
- MongoEngine for the database
- SocketIO for real time communication
- Jason Web Tokens (JWT) for user authentication and authorization
- Unittest for testing the modules

### PROJECT LINK
*wip*
