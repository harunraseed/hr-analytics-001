"""Environment configuration — the single source of truth for
'which catalog does this environment read from?'.

The CD pipeline sets the APP_ENV variable to dev / uat / prod, and this
module maps that to the matching Databricks catalog. This tiny file is
the whole idea of the session: one variable decides the environment.
"""

import os

# Which Databricks catalog each environment reads from.
CATALOG_BY_ENV = {
    "dev": "hrb_dev",
    "uat": "hrb_uat",
    "prod": "hrb_prod",
}


def get_env() -> str:
    """Return the current environment name. Defaults to 'dev' locally."""
    env = os.environ.get("APP_ENV", "dev").lower()
    if env not in CATALOG_BY_ENV:
        raise ValueError(
            f"Unknown APP_ENV '{env}'. Expected one of {list(CATALOG_BY_ENV)}."
        )
    return env


def get_catalog(env: str | None = None) -> str:
    """Map an environment name to its Databricks catalog."""
    env = env or get_env()
    return CATALOG_BY_ENV[env]


def get_schema() -> str:
    """Schema holding the table (same name in every catalog)."""
    return os.environ.get("HR_SCHEMA", "hr")


def get_table() -> str:
    """Table to read."""
    return os.environ.get("HR_TABLE", "employees")


def get_table_fqn(env: str | None = None) -> str:
    """Fully-qualified name: catalog.schema.table (e.g. hrb_dev.hr.employees)."""
    return f"{get_catalog(env)}.{get_schema()}.{get_table()}"
