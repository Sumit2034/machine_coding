from datetime import datetime
from typing import List
import uuid

from model.column import Column


class Table:

    def __init__(self, table_name, column_names: List[Column], storage_data) -> None:
        self.table_name = table_name
        self.column_names = column_names
        self.storage_data = storage_data

    def set_table_in_database(self):
        self.storage_data[self.table_name] = {
            'table_statitics' : self.column_names,
            'table_data': [],
            'meta_info': {
                'created_at' : datetime.now()
            }
        }
    
        
    def insert_row(self, row_data):
        row_data['id'] = uuid.uuid4()
        self.storage_data[self.table_name]['table_data'].append(row_data)
        return row_data['id']


    



 
        