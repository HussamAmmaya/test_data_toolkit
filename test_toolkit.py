import pytest
import csv
from toolkit import get_value_by_key, read_test_data, send_result_to_file, get_record_count


@pytest.mark.smoke
def test_sanity():
    assert True



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
    assert result == expected


def test_get_record_count(sample_csv_file):
    records = read_test_data(sample_csv_file)
    assert get_record_count(records) == 1

def test_read_test_data_missing_file(tmp_path):
    missing = tmp_path / "does_not_exist.csv"
    with pytest.raises(FileNotFoundError):
        read_test_data(missing)

def test_send_result_to_file_empty_list(tmp_path):
    output_file = tmp_path / "output.csv"
    with pytest.raises(ValueError):
        send_result_to_file([], output_file)

