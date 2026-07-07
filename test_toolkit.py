import pytest
import csv

@pytest.mark.smoke
def test_sanity():
    assert True

from toolkit import get_value_by_key, read_test_data, send_result_to_file

def test_get_value_by_key_returns_correct_values():
    records = {"id": 1, "status": "pass"}
    result = get_value_by_key([records], "status")
    assert result == ["pass"]

def test_get_value_by_key_raises_key_error_for_invalid_key():
    records = {"id": 1, "status": "pass"}
    with pytest.raises(KeyError):
        get_value_by_key([records], "invalid_key")

@pytest.fixture
def sample_csv_file(tmp_path):
    # Create a sample CSV file for testing
    file_path = tmp_path / "sample.csv"
    with open(file_path, "w", newline="") as f:
        writer =csv.DictWriter(f, fieldnames=["id", "status"])
        writer.writeheader()
        writer.writerow({"id": "1", "status": "pass"})
    return file_path

def test_read_test_data_reads_csv_file_correctly(sample_csv_file):
    result = read_test_data(sample_csv_file)
    assert result == [{"id": "1", "status": "pass"}]

@pytest.mark.parametrize("key, expected", [
    ("id", [1]),
    ("status", ["pass"])
])
def test_get_value_by_key_various_keys(key, expected):
    records = [{"id": 1, "status": "pass"}]
    result = get_value_by_key(records, key)
    assert result == records
