from sqlalchemy import create_engine
from config import DB_CONFIG

def get_engine():
    db_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    return create_engine(db_url)
