print("Version 1 - Initial Code")


def connect_to_snowflake(account, user, password, warehouse, database, schema, role=None, authenticator=None, **kwargs):
    """Create and return a Snowflake connection object."""
    try:
        import snowflake.connector
    except ImportError as exc:
        raise ImportError("Install the Snowflake connector first: pip install snowflake-connector-python") from exc

    connection_params = {
        "account": account,
        "user": user,
        "password": password,
        "warehouse": warehouse,
        "database": database,
        "schema": schema,
    }

    if role:
        connection_params["role"] = role
    if authenticator:
        connection_params["authenticator"] = authenticator

    connection_params.update(kwargs)
    return snowflake.connector.connect(**connection_params)


# Example usage:
# conn = connect_to_snowflake(
#     account="xy12345.us-east-1",
#     user="your_user",
#     password="your_password",
#     warehouse="COMPUTE_WH",
#     database="MY_DB",
#     schema="PUBLIC"
# )