
from constants.column import ColumnType
from model.column import Column
from model.database import Database
from model.table import Table
from service.table_data import TableData


def main():
    storage = {}
    database = Database("main_db", storage_data=storage)
    column_name = Column("name", ColumnType.STRING)
    column_age = Column("age", ColumnType.INTEGER)
    column_salary = Column("salary", ColumnType.INTEGER)

    table_columns = [column_name, column_age, column_salary]
    identity_table = Table(table_name='Identity', column_names=table_columns, storage_data=database.get_storage())
    identity_table.set_table_in_database()

    payload_to_insert3 = {
        "name": "Shyam",
        "age": 52,
        "salary": 35000000
    }
    payload_to_insert2 = {
        "name": "Soham",
        "age": 54,
        "salary": 25000000
    }
    payload_to_insert1 = {
        "name": "Lisa",
        "age": 30,
        "salary": 15000000
    }
    payload_to_insert = {
        "name": "Mario",
        "age": 27,
        "salary": 5000000
    }

    insert = identity_table.insert_row(row_data=payload_to_insert)
    insert1 = identity_table.insert_row(row_data=payload_to_insert1)
    insert2 = identity_table.insert_row(row_data=payload_to_insert2)
    insert3 = identity_table.insert_row(row_data=payload_to_insert3)

    table_data = TableData(storage=database.get_storage(), table_name='Identity')
    print(f"all rows of the tbale {table_data.get_all_rows()}")

    print(table_data.filter_records(id=insert))

    table_data.delete_row_by_id(insert2)

    database.delete_table('Identity')

    table_data2 = TableData(storage=database.get_storage(), table_name='Identity')
    print(f"all rows of the table 2{table_data2.get_all_rows()}")

if __name__ =='__main__':
    main()