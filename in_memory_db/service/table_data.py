class TableData:

    def __init__(self, storage, table_name) -> None:
        self.storage_data = storage
        self.table_name = table_name
        
    def get_table_information(self, column_names):
        for column in column_names:
            print(f'Table: {self.table_name} COLUMN', column.__dict__) 

    def delete_row_by_id(self, row_id):
        """Deletes a row from the database by its ID."""
        table_data=[]
        if self.storage_data.get(self.table_name):
            table_data = self.storage_data.get(self.table_name).get('table_data')
        if table_data:
            for i, row in enumerate(table_data):
                if row['id'] == row_id:
                    del table_data[i]
                    print(f"Row with ID {row_id} deleted successfully.")
                    return
            print(f"Row with ID {row_id} not found.")


    def get_all_rows(self):
        rows = []
        try:
            if self.storage_data.get(self.table_name):
                table_data = self.storage_data.get(self.table_name).get('table_data')
            else:
                return ' Table does not exist in the database'

            for data in table_data:
                rows.append(data)
                print(data)
            return rows
        except:
            raise Exception('Table doesnot exist in the database')
        
    def filter_records(self, column_name=None, column_value=None, id=None):
        filtered_data = []
        table_data = self.storage_data[self.table_name].get('table_data', [])
        for data in table_data:
            if (id and data['id']) == id or (column_name and column_value and data.get(column_name) and data[column_name] == column_value):
                filtered_data.append(data)
        return filtered_data