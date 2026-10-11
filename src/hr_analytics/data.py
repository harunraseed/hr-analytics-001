"""Reads data from the employees Delta table in Databricks."""

import pandas as pd

from hr_analytics.config import get_table_fqn


def read_employees(conn, env: str | None = None) -> pd.DataFrame:
    """Read the employees Delta table for the given environment.

    The catalog is chosen by env (hrb_dev / hrb_uat / hrb_prod), so the
    SAME code reads different data depending on where it runs.
    """
    table = get_table_fqn(env)
    query = f"SELECT * FROM {table}"
    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall_arrow().to_pandas()
