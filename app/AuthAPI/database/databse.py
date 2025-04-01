from cassandra.cluster import Cluster

KEYSPACE = "warehouse"
session = None

def connect_to_cassandra():
    cluster = Cluster(["127.0.0.1"], port=9042)
    session = cluster.connect()
    print("Cassandra success!")
    return session

def create_keyspace_and_tables(session):
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {KEYSPACE}
        WITH replication = {{ 'class': 'SimpleStrategy', 'replication_factor': 1 }};
    """)
    session.set_keyspace(KEYSPACE)

    session.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id UUID PRIMARY KEY,
            email TEXT,
            password TEXT,
            role TEXT,
            created_at TIMESTAMP
        );
    """)
   

def init_db():
    global session
    session = connect_to_cassandra()
    create_keyspace_and_tables(session)

def get_session():
    global session
    if session is None:
        raise Exception("Session not initialized.")
    return session
