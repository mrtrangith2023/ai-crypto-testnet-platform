import sqlite3

conn = sqlite3.connect("ai_crypto.db")

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE users
ADD COLUMN role TEXT DEFAULT 'user'
""")

conn.commit()

print("Role column added!")

conn.close()