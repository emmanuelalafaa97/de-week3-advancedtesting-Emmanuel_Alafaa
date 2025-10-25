from order_pipeline.reader import Reader


def test_read_json_file():
    file_path = r"Week3_Tasks\Data_&_other_additional_info\shoplink.json"
    reader = Reader(path=file_path, format="json")
    rows = list(reader.read())
    assert len(rows) == 10  # assuming we know there are 5 rows in the test JSON file
    assert rows[0]["order_id"] == "ORD001"  # check first row's order_id
    assert rows[-1]["order_id"] == "ORD010"  # check last row's order_id