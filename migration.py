from database import database

db = database()
cursor = db.cursor()

def create_table_posts():
    try:
        sql = """CREATE TABLE posts (
              id INT AUTO_INCREMENT PRIMARY KEY,
              title VARCHAR(255),
              content TEXT
              )
              """
        cursor.execute(sql)
        print("- Posts Table created successfully .....")
    except:
        print("- Posts Table Already Exist ! .....")


# Execute :
if db.is_connected():
  print("- Connecting to Database successfully .....")
  create_table_posts()