import csv
from pathlib import Path

def read_test_data(path: str) -> list[dict]:
    """
    Reads test data from a CSV file and returns it as a list of dictionaries.

    Args:
        path (str): The path to the CSV file.

    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"The file at {path} does not exist.")

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

        
def get_value_by_key(records: list[dict], key: str) -> list:
    """
    Retrieves values associated with a specific key from a list of dictionaries.

    Args:
        records (list[dict]): A list of dictionaries.
        key (str): The key for which to retrieve values.

    Returns:
        list: A list of values corresponding to the specified key.
    """
    if not records:
        return []
    
    if key not in records[0]:
        raise KeyError(f"The key '{key}' does not exist in the records.")

    return [record[key] for record in records]

def send_result_to_file(results:list[dict], path:str) -> None:
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        results (list[dict]): A list of dictionaries to write to the CSV file.
        path (str): The path to the output CSV file.
    """
    if not results:
        raise ValueError("The results list is empty. Cannot write to file.")

    file_path = Path(path)
    fieldnames = list(results[0].keys())
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    def get_record_count(records):
        return len(records)

    def test_get_record_count():
        records = [{"id": 1}, {"id": 2}, {"id": 3}]
        result =  get_record_count(records)
        assert result == 3, f"Expected 3, but got {result}"