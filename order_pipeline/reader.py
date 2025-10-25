from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional, Iterable
from datetime import time, date, datetime, timedelta
from string import Template
import csv
import json
import logging
import math
from collections import OrderedDict

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


@dataclass
class sales_record:
        order_id: str
        timestamp : datetime
        item : str
        quantity : int
        price : float
        total: float
        payment_status : str
    
        def to_dict(self) -> Dict[str, Any]:
             return asdict(self)
    
class Reader:
     
     def __init__(self, path: str, format: str = "csv"):
         self.path = path
         self.format = format

     def read(self) -> Iterable[Dict[str, Any]]:

        if self.format == "csv":
            with open(self.path, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                     yield dict(row)

        elif self.format == "json":
            with open(self.path, "r", encoding="utf-8") as file:
                 data = json.load(file)
                 for item in data:
                     yield item             # note the use of yield rather than return
        else:
            raise ValueError("Unsupported format: " + str(self.format))
        

         
        
#Now read the file using the Reader class
file_to_read = Reader(r"Week3_Tasks\Data_&_other_additional_info\shoplink.json", format="json")
print("Reading file contents:")
for row_data in file_to_read.read():
    print(row_data)
    print("File read complete.")

all_rows = list(file_to_read.read())
total_rows = len(list(file_to_read.read())) 
#or total_rows = len(all_rows)
print(f"Total number of rows: {total_rows}")

n_rows = 0
for row_data in file_to_read.read():
    n_rows += 1
    #print(f"Total number of rows read: {n_rows}")    # if it printsinside the for loop it would be printing everytime until the last number which is not ideal in this case 

print(f"Total number of rows read: {n_rows}")






if __name__ == "__main__":
      file_to_read = Reader(r"Week3_Tasks\Data_&_other_additional_info\shoplink.json", format="json")
      print("Reading file contents:")
      for row_data in file_to_read.read():
                print(row_data)
      print("File read complete.")

      # or alternatively use a list (as it is a list object in the file) to collect all rows at once
      #print(list(file_to_read.read()))
      # the for loop method is better and more organized

            