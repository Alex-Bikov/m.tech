from sqlalchemy import MetaData, Table, Column, INTEGER, String, TIMESTAMP


metadata = MetaData()

data = Table(
    "data",
    metadata,
    Column("key", INTEGER, primary_key=True),
    Column("ip", String, nullable=False),
    Column("uri", String),
    Column("")
)