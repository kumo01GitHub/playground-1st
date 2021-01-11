from urllib.parse import urlparse
import mysql.connector

from hoge import dtos

class HogeDAO:
    def get_all():
        url = urlparse('mysql://localhost:3306/helloworld')

        conn = mysql.connector.connect(
            host = url.hostname or 'localhost',
            port = url.port or 3306,
            user = url.username or 'root',
            database = url.path[1:],
        )

        cur = conn.cursor(dictionary=True)
        cur.execute('SELECT id, value from HOGE')

        rows = cur.fetchall()
        hoge_list = []
        for row in rows:
            hoge_list.append(dtos.HogeDTO(row['id'], row['value']))

        conn.close()

        return hoge_list
