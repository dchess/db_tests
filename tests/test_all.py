from sqlsorcery import MSSQL
import pandas as pd


def test_this_works():
    config = {
        "server": "db",
        "db": "master",
        "user": "sa",
        "pwd": "Just4TestingThis",
        "schema": "dbo",
    }
    sql = MSSQL(**config)
    data = [{"id": 1, "value": "test1"}, {"id": 2, "value": "test2"}]
    df = pd.DataFrame(data)
    sql.insert_into("test_table", df)
    results = pd.read_sql_table("test_table", con=sql.engine, schema=sql.schema)
    assert len(results) == 2
