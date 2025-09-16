# Data Scientist Codes Collection

This repository collects Python scripts implementing algorithms and techniques widely used by leading data scientists. It also includes a portfolio of SQL templates for common analytics tasks and a minimal continuous‑integration setup.

## Quick start

1. Clone the repository and install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the static code analysis and formatting checks:
   ```bash
   ruff .
   sqlfluff lint sql/
   ```

3. Execute the tests:
   ```bash
   pytest -q
   ```

## Contents

| Path                    | Description                                                |
|-------------------------|------------------------------------------------------------|
| `python_scripts/`       | The original collection of example algorithms by top data scientists. |
| `sql/`                  | A portfolio of SQL scripts (BigQuery dialect) for data modelling, quality checks and feature engineering. |
| `tests/`                | Minimal unit tests to ensure scripts can be imported.      |
| `.github/workflows/`    | GitHub Actions workflow to run linting and tests on each commit. |
| `notebooks/`            | Case study outlines and other notebook assets.             |
| `LICENSE`               | MIT license for open use of this repository.               |

For a deeper dive into the SQL templates, see [README_SQL.md](sql/README_SQL.md).