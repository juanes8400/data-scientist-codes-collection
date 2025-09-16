# Contributing

Thank you for considering a contribution! This project is designed to serve as a showcase of good practices in data science. To make your contribution smooth and maintain quality, please follow these guidelines.

## Workflow

1. **Fork the repository** and create your feature branch (`git checkout -b feature/YourFeature`).
2. Make your changes with clear commits and descriptive messages.
3. Ensure that your code passes linting checks (`ruff`) and SQL linting (`sqlfluff`).
4. Add or update tests in `tests/` if you introduce new functionality.
5. Submit a pull request describing what your changes accomplish.

## Style

* Python code should follow the [PEP 8](https://pep8.org/) guidelines as enforced by `ruff`.
* SQL should be formatted according to the BigQuery dialect conventions. The SQL examples in this repo serve as a reference.
* Include docstrings for public functions and modules where appropriate.
* Write clear, concise comments when your implementation is not self‑explanatory.

## Licensing

By submitting a contribution, you agree that your code will be licensed under the MIT License contained in this repository.