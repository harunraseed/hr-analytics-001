"""Pure transformation logic — no Databricks, no network.

Because these functions take a DataFrame in and return a DataFrame/number
out, they are fast and deterministic to unit-test. THIS is what CI checks
on every pull request.
"""

import pandas as pd


def total_headcount(df: pd.DataFrame) -> int:
    """Total number of employees."""
    return int(len(df))


def headcount_by_department(df: pd.DataFrame) -> pd.DataFrame:
    """Employee count per department, highest first."""
    return (
        df.groupby("department", as_index=False)
        .size()
        .rename(columns={"size": "headcount"})
        .sort_values("headcount", ascending=False, ignore_index=True)
    )


def average_salary_by_department(df: pd.DataFrame) -> pd.DataFrame:
    """Average salary per department, rounded to 2 decimals."""
    result = (
        df.groupby("department", as_index=False)["salary"]
        .mean()
        .rename(columns={"salary": "avg_salary"})
    )
    result["avg_salary"] = result["avg_salary"].round(2)
    return result
