# RocheHackathon
Roche Pune Hackathon: Diabetes Care DigiTalent! hosted by Roche India (The Hiring Challenge)
This project is a simple Flask API that provides two endpoints: one for generating numbers based on given parameters and another for retrieving statistics on the most used and most recent requests.
## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/) (version 3.9.18)
- [pip](https://anaconda.org/anaconda/pip) (Python package installer) (version 23.3.2)
- [flask](https://anaconda.org/anaconda/flask) (version 2.2.5)
- [flask-cors](https://anaconda.org/anaconda/flask-cors) (version 3.0.10)
- [flask-testing](https://anaconda.org/conda-forge/flask-testing) (versio 0.8.1)
- [jupyterlab](https://anaconda.org/conda-forge/jupyterlab) (version 4.0.8)

### Installation
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/prashantmane92/RocheHackathon.git
   cd RocheHackathon

2. **Create a Virtual Environment:**

    It's a good practice to use a virtual environment to manage dependencies for our project.
    Create a virtual environment using the following commands:
    ```bash
    conda create --name roche_env --file requirements.txt
3. **Activate the Virtual Environment:**
   Activate the virtual environment:
   ```bash
   # On Windows
    .\venv\Scripts\activate
  Your command prompt or terminal should now show the virtual environment's name.

## Usage

### Running the Application

Start the Flask application:
  ```bash
  python app.py
  ```
The application will be running at http://localhost:5000.

### API Endpoints
1. **Generate Numbers**

* Endpoint: /api/numbers
* Method: POST
* Request Body:
  - int1 (integer): First integer parameter
  - int2 (integer): Second integer parameter
  - limit (integer): Limit for number generation
  - str1 (string): First string parameter
  - str2 (string): Second string parameter
* Example Request:
* Example Request:
    ```bash
    curl -X POST -d "int1=2&int2=3&limit=10&str1=foo&str2=bar" http://localhost:5000/api/numbers
    ```
* Example Response:
    ```bash
    "1,foo,bar,foo,5,foobar,7,foo,bar,foo"
    ```

2. **Get Statistics**
* Endpoint: /api/statistics
* Method: GET
* Example Request:
    ```bash
    curl http://localhost:5000/api/statistics
    ```
* Example Response:
  ```
  "Most used request: {'int1': 2, 'int2': 3, 'limit': 10, 'str1': 'foo', 'str2': 'bar'} with 1 Hits,\nMost recent request: {'int1': 2, 'int2': 3, 'limit': 10, 'str1': 'foo', 'str2': 'bar'} with 1 Hits"
  ```

## Testing
To run unit tests, use the following command:
  ```bash
python -m unittest test_server.py
python -m unittest test_server2.py
  ```


## Project Structure

* app.py: Main application file with Flask routes.
* test_app.py: Unit tests for the application.
* requirements.txt: List of Python dependencies.
* README.md: Project documentation.
