from validator import validator
from typing import List, Dict, Any
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class Analyzer:
    """ Analyze cleaned Shoplink order data."""

    def __init__(self, validator: validator):
        self.validator = validator

    def analyze(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Perform basic analysis on the data."""
        total_orders = len(data)
        total_revenue = sum(item['total'] for item in data if 'total' in item)
        average_order_value = total_revenue / total_orders if total_orders > 0 else 0

        analysis = {
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "average_order_value": average_order_value
        }

        logger.info(f"Analysis complete: {analysis}")
        return analysis