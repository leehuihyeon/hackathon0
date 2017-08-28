import sqlite3
 
conn = sqlite3.connect("db.sqlite3")
# Autocommit 사용시:
# conn = sqlite3.connect("test.db", isolation_level=None)
 
cur = conn.cursor()
sql = "insert into singsong(title,content,youtubeurl) values (?, ?, ?)"
cur.execute(sql, ('홍길동', 1, '서울'))
conn.commit()
 
conn.close()