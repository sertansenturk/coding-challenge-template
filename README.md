# challenge_template

## Prerequisites

- **Docker (suggested):** Please refer to the [documentation](https://docs.docker.com/get-docker/) for installation instructions.
- **Python 3.8:** Required if you want to run the code locally on the terminal. Please follow the [official guideline](https://www.python.org/about/gettingstarted/) for installation instructions.

## How to run

### Running in Docker

For convenience, you could run the whole pipeline by simply executing in the terminal:

```bash
make
```

## Running notebooks

I did exploratory data analysis (EDA) on the data and learning strategies parallel to implementing a solution. The EDA was done in Jupyter notebooks, stored in [./notebooks/](./notebooks/).

If you want to run the notebooks locally, you can start Jupyter Lab by running in the terminal:

```bash
make jupyter
```

Above command builds a docker-compose stack and runs a container with Jupyter installed. Once the Jupyter is up and running, you should see a URL looking like `http://127.0.0.1:8888/lab?token=9f59...` in the terminal screen.

Clicking the URL should take you the Jupyter Lab on your browser of choice.

Note the first build could take around 6-7 minutes, depending on your machine and internet connection.

## Running unittests

Run in the terminal:

```bash
make unit-tests 
```

which runs unit tests using pytest.

The unittests are also run on Github actions after each push: [link](https://github.com/sertansenturk/challenge_template/actions).

## Code formatting

In the terminal run:

```bash
make format
```

which formats the Python code in the repo using [black](https://black.readthedocs.io/en/stable/).

## Code linting

In the terminal run:

```bash
make lint
```

which shows Python code style / linting issues using [flake8](https://flake8.pycqa.org/en/latest/) and [pylint](https://pylint.pycqa.org/en/latest/).
