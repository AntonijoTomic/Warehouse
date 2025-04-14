from cassandra.cluster import Cluster
import os,time
from dotenv import load_dotenv

load_dotenv()

KEYSPACE = os.getenv("CASSANDRA_KEYSPACE", "warehouse")
CASSANDRA_HOST = os.getenv("CASSANDRA_HOST", "cassandra")
CASSANDRA_PORT = int(os.getenv("CASSANDRA_PORT", "9042"))
KEYSPACE = "warehouse"

session = None

def connect_to_cassandra():
     while True:
        try:
            cluster = Cluster(['cassandra'], port=9042)  
            session = cluster.connect()
            print("Connected to Cassandra.")
            return session
        except Exception as e:
            print(f"Cassandra not ready yet: {e}")
            time.sleep(3)

def create_keyspace_and_table(session):
 
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {KEYSPACE}
        WITH replication = {{ 'class': 'SimpleStrategy', 'replication_factor': 1 }};
    """)
    session.set_keyspace(KEYSPACE)

    session.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id UUID PRIMARY KEY,
            name TEXT,
            category_id  TEXT,
            price FLOAT,
            quantity INT,
            description TEXT,
            created_at TIMESTAMP
        );
    """)
    
    session.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id UUID PRIMARY KEY,
            name TEXT
        );
    """)



def init_db():
    global session
    session = connect_to_cassandra()
    create_keyspace_and_table(session)

def get_session():
    global session
    if session is None:
        raise Exception("Session not initialized.")
    return session