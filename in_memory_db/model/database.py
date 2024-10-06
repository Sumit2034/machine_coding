class Database:

    def __init__(self, name, storage_data) -> None:
        self.database = name
        self.storage_data = storage_data

    def delete_table(self, table_name):
        if self.storage_data.get(table_name):
            print(f"Table {table_name} found")
            del self.storage_data[table_name]
            return
        else:
            raise Exception(f"{table_name} not exist in database")
        
    def get_storage(self):
        return self.storage_data 
        
