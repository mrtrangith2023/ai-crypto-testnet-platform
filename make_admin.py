import sqlite3

conn = sqlite3.connect("ai_crypto.db")

cursor = conn.cursor()

cursor.execute("""
UPDATE users
SET role='admin'
WHERE email='tran@test.com'
""")

conn.commit()

print("Updated!")

conn.close()