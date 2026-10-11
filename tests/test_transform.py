"""Unit tests for the pure transform functions.

These need NO Databricks connection — they run in a fraction of a second
on a small in-memory DataFrame. This is exactly what CI runs on every PR.
"""

import pandas as pd
import pytest

from hr_analytics.transform import (
    average_salary_by_department,
    headcount_by_department,
    total_headcount,
)


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "employee_id": [1, 2, 3, 4, 5],
            "department": [
                "Sales",
                "Sales",
                "Engineering",
                "Engineering",
                "Engineering",
            ],
            "salary": [50000, 60000, 90000, 100000, 110000],
        }
    )


def test_total_headcount(sample_df):
    assert total_headcount(sample_df) == 5


def test_headcount_by_department(sample_df):
    result = headcount_by_department(sample_df)
    # Engineering (3) should sort above Sales (2)
    assert result.iloc[0]["department"] == "Engineering"
    assert result.iloc[0]["headcount"] == 3
    assert result.iloc[1]["department"] == "Sales"
    assert result.iloc[1]["headcount"] == 2


def test_average_salary_by_department(sample_df):
    result = average_salary_by_department(sample_df)
    eng = result.loc[result["department"] == "Engineering", "avg_salary"].iloc[0]
    sales = result.loc[result["department"] == "Sales", "avg_salary"].iloc[0]
    assert eng == 100000.00
    assert sales == 55000.00
