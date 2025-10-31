from fastapi import FastAPI
import psycopg2
app = FastAPI()

@app.get("/")
def read_root():
    # Try to connect to Postgres and send back status and email
    try:
        conn = psycopg2.connect(
            host="db",
            database="postgres",
            user="postgres",
            password="example"
        )
        conn.close()
        db_status = "connected"
    except Exception as e:
        db_status = str(e)
    return {
        "email": "23f3004176@ds.study.iitm.ac.in",
        "db_status": db_status
    }
