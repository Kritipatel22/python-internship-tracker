# db.py
# Handles database connection 
import logging
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kriti@123",   # replace
        database="internship_tracker",
        port=3306  # or 3307 if you used that
    )

def search_by_company(company):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM applications WHERE company LIKE %s"
    cursor.execute(query, ("%" + company + "%",))
    result = cursor.fetchall()
    conn.close()
    logging.info(f"Searched by company: {company}")

    return result

def search_by_status(status):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM applications WHERE status LIKE %s"
    cursor.execute(query, ("%" + status + "%",))
    result = cursor.fetchall()
    conn.close()
    logging.info(f"Searched by status: {status}")

    return result

def search_by_title(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM applications WHERE title LIKE %s"
    cursor.execute(query, ("%" + keyword + "%",))
    result = cursor.fetchall()
    conn.close()
    logging.info(f"Searched by title: {keyword}")

    return result

def sort_by_deadline():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM applications ORDER BY deadline ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    logging.info("Sorted applications by deadline")

    return result

def sort_by_company():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM applications ORDER BY company ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    logging.info("Sorted applications by company")
    return result

def sort_by_status():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT * FROM applications 
    ORDER BY 
        CASE 
            WHEN status='Applied' THEN 1
            WHEN status='Interview' THEN 2
            WHEN status='Selected' THEN 3
            WHEN status='Rejected' THEN 4
            ELSE 5
        END;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    logging.info("Sorted applications by status")

    return result

def get_summary():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        COUNT(*) AS total,
        SUM(status = 'Applied') AS applied,
        SUM(status = 'Interview') AS interview,
        SUM(status = 'Selected') AS selected,
        SUM(status = 'Rejected') AS rejected
    FROM applications;
    """

    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_applications():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM applications")
    result = cursor.fetchall()
    conn.close()
    return result


