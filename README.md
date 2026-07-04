# Test Data Toolkit

A simple Python toolkit for reading test data from CSV files, extracting values,
and writing results to file — built with testability in mind and fully covered
by a pytest suite.

## Project Structure

test_data_toolkit/
├── toolkit.py          # Core functions
├── test_toolkit.py      # pytest suite
├── pytest.ini            # Marker configuration
├── requirements.txt
└── data/
└── test_data.csv     # Sample test data


## Functions
- `read_test_data(path)` — reads a CSV file and returns a list of dicts.
- `get_value_by_key(records, key)` — extracts values by key.
- `send_result_to_file(results, path)` — writes results to a file.

## Setup

```bash
python -m venv venv
venv\Scripts\activate      # on Windows
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

Run only smoke tests:
```bash
pytest -m smoke
```

## Requirements
See `requirements.txt`.