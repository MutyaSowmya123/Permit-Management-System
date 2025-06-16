import pymysql

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Sowmya@123',
        database='permits'
    )
    print("✅ Connected to MySQL successfully!")
    conn.close()
except pymysql.MySQLError as e:
    print("❌ MySQL connection failed:")
    print(e)
