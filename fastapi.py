import datetime
from datetime import time
import pymysql
from fastapi import FastAPI

app = FastAPI()
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='tempandhumi',
        password='xxxxxxxxxx',
        database='tempandhumi',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/")
async def read_root():
    return {"LN1202-humi&temp API"}


@app.get("/temperature/data/")
def get_temp_data(device: str, numpoint: int):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `tempdata` WHERE `device` = %s ORDER BY `id` DESC LIMIT %s"
            cursor.execute(sql,(device, numpoint))
            result = cursor.fetchall()
            return result
        connection.colse()
    except Exception as e:
        print(e)
        return {"error": "Unable to fetch data from database"}

@app.get("/temperature/")
async def read_item(id: str, temp: str, humi: str):
    nowTime = datetime.datetime.now()
    date_string = nowTime.strftime('%Y-%m-%d')
    time_string = nowTime.strftime('%H:%M:%S')
    intime_string = date_string+' ' +time_string
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO `tempdata` (`temperature`, `humidity`,`device`, `intime`) VALUES (%s, %s, %s, %s)"
            values = (temp, humi, id, intime_string )
            cursor.execute(sql, values)
        connection.commit()
    finally:

    return nowTime


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
