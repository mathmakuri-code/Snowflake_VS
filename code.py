import logging
from typing import Any, Dict, List, Optional, Tuple


def configure_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def connect_to_snowflake(
    account: str,
    user: str,
    password: str,
    warehouse: str,
    database: str,
    schema: str,
    role: Optional[str] = None,
    authenticator: Optional[str] = None,
    **kwargs: Any,
):
    """Return a Snowflake connection object."""
    try:
        import snowflake.connector
    except ImportError as exc:
        raise ImportError(
            "Install the Snowflake connector first: pip install snowflake-connector-python"
        ) from exc

    connection_params: Dict[str, Any] = {
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


def fetch_table_data(
    connection,
    table_name: str,
    columns: str = "*",
    limit: Optional[int] = None,
) -> List[Tuple[Any, ...]]:
    """Fetch rows from a Snowflake table."""
    logger = logging.getLogger(__name__)
    query = f"SELECT {columns} FROM {table_name}"
    if limit is not None:
        query += f" LIMIT {limit}"

    logger.info("Executing query: %s", query)
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    logger.info("Fetched %d rows from %s", len(rows), table_name)
    return rows


def main() -> None:
    configure_logging()
    logger = logging.getLogger(__name__)

    conn = connect_to_snowflake(
        account="<YOUR_ACCOUNT>",
        user="<YOUR_USER>",
        password="<YOUR_PASSWORD>",
        warehouse="<YOUR_WAREHOUSE>",
        database="<YOUR_DATABASE>",
        schema="<YOUR_SCHEMA>",
        role="<YOUR_ROLE>",
    )

    try:
        data = fetch_table_data(conn, table_name="PUBLIC.MY_TABLE", limit=10)
        for row in data:
            logger.info(row)
    finally:
        conn.close()
        logger.info("Snowflake connection closed")


if __name__ == "__main__":
    main()
