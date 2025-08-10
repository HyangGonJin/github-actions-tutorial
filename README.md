# github-actions-tutorial

A simple Flask application with a CI/CD pipeline using GitHub Actions.

This project serves as a tutorial for setting up a basic Python project with automated testing and linting using GitHub Actions.

## Project Structure

```
.
├── .github
│   └── workflows
│       └── main.yml
├── app.py
├── README.md
├── requirements.txt
└── test_app.py
```

## Getting Started

### Prerequisites

*   Python 3.10 or later
*   pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/HyangGonJin/github-actions-tutorial.git
    cd github-actions-tutorial
    ```

2.  Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the Flask application, use the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

### Running Tests

To run the tests, use the following command:

```bash
pytest
```

## CI/CD Pipeline

This project uses GitHub Actions to automate the following tasks:

*   **Linting:** Checks the code for style issues using `flake8`.
*   **Testing:** Runs the test suite using `pytest`.

The workflow is defined in the `.github/workflows/main.yml` file and is triggered on every push to the `main` branch.