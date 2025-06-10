from .database import get_db_connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todo_items (
            id VARCHAR(50) PRIMARY KEY,
            name VARCHAR(100),
            description TEXT,
            is_complete BOOLEAN
        );
        INSERT INTO todo_items (id, name, description, is_complete)
        VALUES
            ('1', 'Task 1', 'Description for Task 1', false),
            ('2', 'Task 2', 'Description for Task 2', true)
        ON CONFLICT DO NOTHING;
    """)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()