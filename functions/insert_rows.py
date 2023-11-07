import sqlite3

def insert_one_row(
    database_name:str,
    table_name:str,
    columns_name:str,
    values:str
) -> None:

    """Create a table on a specific database

    Args:
        database_name (str): A database's name.
        table_name (str): A table's name.
        columns (str): A query specifying the columns.
        columns_name(str): Columns to insert the valiues.
        values (str): Values to insert.

    Example: 
    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {table_name} ({columns_name}) VALUES ({values})
    """)

    conn.commit()
    conn.close()
