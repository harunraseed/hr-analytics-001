"""Entry point: read the current environment's employees table and
print a small summary. Run locally with `hr-analytics` or
`python -m hr_analytics.main`.
"""

from hr_analytics.config import get_env, get_table_fqn
from hr_analytics.connection import get_connection
from hr_analytics.data import read_employees
from hr_analytics.transform import (
    average_salary_by_department,
    headcount_by_department,
    total_headcount,
)


def main() -> None:
    env = get_env()
    print(f"[hr-analytics] Environment : {env}")
    print(f"[hr-analytics] Reading from: {get_table_fqn(env)}")

    conn = get_connection()
    try:
        df = read_employees(conn, env)
    finally:
        conn.close()

    print(f"[hr-analytics] Total headcount: {total_headcount(df)}")
    print("[hr-analytics] Headcount by department:")
    print(headcount_by_department(df).to_string(index=False))
    print("[hr-analytics] Average salary by department:")
    print(average_salary_by_department(df).to_string(index=False))


if __name__ == "__main__":
    main()
