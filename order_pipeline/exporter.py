from transformer import Transformer
from validator import validator

from typing import List, Dict, Any
import logging 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class Exporter:
    """ Export cleaned Shoplink order data to desired format."""

    def __init__(self, transformer: Transformer, validator: validator):
        self.transformer = transformer
        self.validator = validator

    def export_to_json(self, data: List[Dict[str, Any]], file_path: str) -> None:
        """Export data to a JSON file."""
        import json

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"Data successfully exported to {file_path}")

    def export_to_csv(self, data: List[Dict[str, Any]], file_path: str) -> None:   # remember to import the List and Dict from typing module so that you can use them in the function annotation
        """Export data to a CSV file."""
        import csv

        if not data:
            logger.warning("No data to export.")
            return

        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        logger.info(f"Data successfully exported to {file_path}")



if __name__ == "__main__":
    # Example usage
    transformer = Transformer()
    validator_instance = validator()
    exporter = Exporter(transformer, validator_instance)

    # Sample cleaned data
    cleaned_data = [
        {
            "order_id": "123",
            "timestamp": "2023-10-01T12:00:00Z",
            "item": "widget",
            "quantity": 2,
            "price": 19.99,
            "total": 39.98,
            "payment_status": "paid"
        },
        {
            "order_id": "124",
            "timestamp": "2023-10-02T15:30:00Z",
            "item": "gadget",
            "quantity": 1,
            "price": 29.99,
            "total": 29.99,
            "payment_status": "paid"
        }
    ]

    # Export to JSON
    exporter.export_to_json(cleaned_data, 'cleaned_orders.json')

    # Export to CSV
    exporter.export_to_csv(cleaned_data, 'cleaned_orders.csv')