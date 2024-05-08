from psycopg2 import connect
from psycopg2.extras import DictCursor

conn = connect(
    user="postgres",
    database="yaypan_db",
    password="black0613",
    host="localhost",
    port=5432,
    cursor_factory=DictCursor
)
cur = conn.cursor()


async def start_up():
    users = """
        CREATE TABLE IF NOT EXISTS users(
            id BIGSERIAL PRIMARY KEY,
            user_id VARCHAR(100) UNIQUE,
            created_at TIMESTAMP default now()
        );
    """
    taxis = """
        CREATE TABLE IF NOT EXISTS taxis(
            id BIGSERIAL PRIMARY KEY,
            fullname VARCHAR(128) NOT NULL UNIQUE,
            phone VARCHAR(32) NOT NULL,
            username VARCHAR(40),
            description TEXT,
            photo TEXT NOT NULL,
            top BOOLEAN NOT NULL,
            created_at TIMESTAMP default now()
        );
    """
    cur.execute(users)
    cur.execute(taxis)
    conn.commit()

