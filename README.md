# challenge_template

Template repository to kickstart a Python/Docker environment for coding/take-home challenges.

## Technology Stack

- **Language:** Python 3.8
- **Containerization:** [Docker](https://www.docker.com/)
- **Serving:** [flask](https://flask.palletsprojects.com/en/2.1.x/)
- **Continous Integration:** [Github Actions](https://github.com/sertansenturk/coding-challenge-template/actions)

## Prerequisites

- **Docker:** Please refer to the [documentation](https://docs.docker.com/get-docker/) for installation instructions.

## How to run

### Starting the API

To build & start the application, execute in the terminal:

```bash
make api
```

The above command will start a Docker-compose stack. The stack has a single container with the `challenge_template` package installed behind [flask](https://flask.palletsprojects.com/en/2.1.x/).

Once the stack is up and running, the `template` API will be exposed at `localhost:5000/template`.

#### Posting queries

Open a new terminal window and enter a query, e.g.:

```bash
curl -X POST localhost:5000/template -d 'some message'
```

In the above case, the (dummy) template API returns the message back with additional information as the response.

If you are lazy to remember the full curl command, you could run:

```bash
make post QUERY='some message'
# Received POST request: 'some message'
```

### Running the batch app in Docker

For batch use cases, you could run the workflow built on the functionality in `challenge_template` package as:

```bash
make batch
```

Currently, the (dummy) template driver prints out the command line arguments passed to the driver.

### Running notebooks

It is typical to carry out exploratory data analysis (EDA) on the data and test different approaches alongside implementing a solution. Jupyter is a good ecosystem for such work.

If you want to run the notebooks locally, you can start Jupyter Lab by running in the terminal:

```bash
make jupyter
```

Above command builds a docker-compose stack and runs a container with Jupyter installed. Once the Jupyter is up and running, you should see a URL looking like `http://127.0.0.1:8888/lab?token=9f59...` in the terminal screen.

Clicking the URL should take you the Jupyter Lab on your browser of choice.

Note the first build could take around 6-7 minutes, depending on your machine and internet connection.

### Running unittests

Run in the terminal:

```bash
make unit-tests 
```

which runs unit tests using pytest.

The unittests are also run on Github actions after each push: [link](https://github.com/sertansenturk/challenge_template/actions).

### Code formatting

In the terminal run:

```bash
make format
```

which formats the Python code in the repo using [black](https://black.readthedocs.io/en/stable/).

### Code linting

In the terminal run:

```bash
make lint
```

which shows Python code style / linting issues using [flake8](https://flake8.pycqa.org/en/latest/) and [pylint](https://pylint.pycqa.org/en/latest/).
