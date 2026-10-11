"""Builds a Databricks SQL connection from environment variables.

We never hard-code credentials. The three values below come from
GitHub environment secrets at run time (and from your shell locally).
"""

import os

from databricks import sql


def get_connection():
    """Create a Databricks SQL connection using env-var credentials.

    Requires: DATABRICKS_HOST, DATABRICKS_HTTP_PATH, DATABRICKS_TOKEN.
    """
    return sql.connect(
        server_hostname=os.environ["DATABRICKS_HOST"],
        http_path=os.environ["DATABRICKS_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    )
