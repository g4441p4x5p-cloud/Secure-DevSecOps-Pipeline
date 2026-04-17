import sqlite3

def get_user_data(user_id):
    # تحذير: هذا الكود يحتوي على ثغرة SQL Injection مقصودة للاختبار
    query = "SELECT * FROM users WHERE id = " + user_id 
    return query

print(get_user_data("1 OR 1=1"))
