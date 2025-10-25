# de-week3-advancedtesting-Emmanuel_Alafaa
Data pipeline testing

## Project Objective

Design a bulletproof data pipeline for ShopLink that:

Reads standardized JSON input

Validates and filters incorrect data

Transforms values into consistent formats

Analyzes clean data for insights

Exports the processed results

Verifies each step using comprehensive unit tests

You are the data quality engineer — your goal is to break the pipeline before the data breaks the business.



## Pipeline Components

The pipeline is modular and consists of five main components:

### Component	Description
Reader	Reads JSON data and returns a list of dictionaries. Raises errors for unsupported formats or empty files.
Validator	Ensures required fields are present and valid (order_id, timestamp, item, quantity, price, payment_status, total). Rejects invalid or missing data.
Transformer	Cleans and normalizes fields (e.g., converts currency text to numbers, standardizes payment_status, recalculates totals).
Analyzer	Computes total revenue, average revenue, and counts per payment status.
Exporter	Writes cleaned and analyzed data to a new JSON file (shoplink_cleaned.json).

## How to Run

Clone the repository

````
git clone https://github.com/emmanuelalafaa97/de-week3-advancedtesting-Emmanuel_Alafaa.git
cd de-week3-advancedtesting-<yourname>
```


Install dependencies

```
pip install -r requirements.txt

```


Run the tests

```
pytest -v

```


Run the full pipeline

```
python -m order_pipeline.pipeline

```