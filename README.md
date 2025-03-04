<h1>FastAPI template</h1>

Template for a FastAPI app.

<h2>Table of contents</h2>

- [Technical stack](#technical-stack)
- [Installation](#installation)
- [Usage](#usage)
  - [Environment variables](#environment-variables)
  - [Running the server](#running-the-server)
  - [Running the tests](#running-the-tests)
- [License](#license)

## Technical stack

- [FastAPI](https://fastapi.tiangolo.com/): Web framework.
- [SQLModel](https://sqlmodel.tiangolo.com/): ORM.  

## Installation

Run the following commands to install the project:

```bash
you@machine:~$ python -m venv venv
you@machine:~$ source venv/bin/activate # venv\Scripts\activate on Windows
(venv) you@machine:~$ pip install . # -e .[dev] for development
```

And you are ready to go!

## Usage

### Environment variables

The following environment variables are required:

- `DATABASE_URI`: The URL for the database connection.

If you are developing, you can create a `.env` file in the root of the project with the following content:

```env
DATABASE_URI=sqlite:///db.sqlite
```

This will create a SQLite database in the root of the project when you run the server for the first time.

### Running the server

Run the following commands to start the server:

```bash
you@machine:~$ source venv/bin/activate # venv\Scripts\activate on Windows
(venv) you@machine:~$ fastapi run core/main.py
```

You can access docs by going to `<server_url>/docs`.

### Running the tests

Run the following command to run the tests:

```bash
(venv) you@machine:~$ pytest
```

The tests will run and show the results in the terminal, including the coverage.

The default configuration is to run the tests with coverage. You can change this by modifying the `pyproject.toml` file in the `[tool.pytest.ini_options]` section.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.