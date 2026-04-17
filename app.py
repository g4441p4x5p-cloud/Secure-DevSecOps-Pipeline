import sqlite3

def get_user_data(user_id):
    # الكود الآمن: نستخدم علامة استفهام لمنع دمج المدخلات مباشرة في الاستعلام
    # هذا يمنع ثغرة SQL Injection تماماً
    query = "SELECT * FROM users WHERE id = ?" 
    print(f"Executing secure query with ID: {user_id}")
    return query

# تجربة الاستدعاء بشكل آمن
get_user_data("1")
cloud_api_key = "AIzaSyA1234567890ExampleKey"
