# RocheHackathon
Roche Pune Hackathon: Diabetes Care DigiTalent! hosted by Roche India (The Hiring Challenge)
This project is a simple Flask API that provides two endpoints: one for generating numbers based on given parameters and another for retrieving statistics on the most used and most recent requests.

Note: This project is configured for Windows 10. If you are using a different operating system, some commands may need to be adjusted accordingly.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Interactive HTML Page](#interactive-html-page)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Use app on Interactive HTML Page](#Use-app-on-interactive-html-page)
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

Please refer to requirements.txt

### Installation
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/prashantmane92/RocheHackathonPhase1.git
   cd RocheHackathonPhase1
   ```

2. **Create a Virtual Environment:**

    It's a good practice to use a virtual environment to manage dependencies for our project.
    Create a virtual environment using the following commands:
    ```bash
    conda create --name roche_env --file requirements.txt
    ```
3. **Activate the Virtual Environment:**
   Activate the virtual environment:
   ```bash
    conda activate roche_env
   ```
  Your command prompt or terminal should now show the virtual environment's name.

## Interactive HTML Page

To facilitate easy interaction with the APIs, we have provided an interactive HTML page. You can access it by opening `page.html` in your web browser.

This HTML page allows you to:

- Hit the APIs with various parameters.
- View the responses from the application.

## Usage

### Running the Application

Start the Flask application:
  ```bash
  python App.py
  ```
The application will be running at http://localhost:5000.

### Use app on Interactive HTML Page

To make it easy for developers to interact with the APIs and visualize the responses, we've provided an interactive HTML page. Follow these steps to use it:

1. Open `page.html` in your web browser.
2. Follow the on-screen instructions to input parameters and interact with the APIs.
3. View the output and responses directly in your browser.

Please note that this HTML page is specifically designed for Windows 10.

...


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
    curl -X POST -d "int1=3&int2=5&limit=20&str1=fizz&str2=buzz" http://localhost:5000/api/numbers
    ```
* Example Response:
    ```bash
    "1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,17,fizz,19,buzz"
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
  "Most used request: {'int1': 3, 'int2': 5, 'limit': 20, 'str1': 'fizz', 'str2': 'buzz'} with 1 Hits,\nMost recent request: {'int1': 3, 'int2': 5, 'limit': 20, 'str1': 'fizz', 'str2': 'buzz'} with 1 Hits"
  ```

## Testing
To run unit tests, use the following command:
  ```bash
python -m unittest test_server.py
python -m unittest test_server2.py
  ```


## Project Structure

* App.py: Main application file with Flask routes.
* test_server.py: Unit tests for the Statistics API.
* test_server2.py: Unit tests for the Numbers API.
* requirements.txt: List of Python dependencies.
* README.md: Project documentation.
* page.html: HTML page to hit the API and get responces
