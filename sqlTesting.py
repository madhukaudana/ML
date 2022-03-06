import os
import mysql.connector
from flask import Flask, render_template


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="smartshopping"
)

sql_Query = "select * from product_details"
cursor = db.cursor()
cursor.execute(sql_Query)
# getting all records from database prod_details table
records = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)

product = "watermelon"
prodChecker= False
prodPrice= None
prodWeight=None
product_details=None

#compare with database
for row in records:               
    if(product==row[1]):
        prodChecker=True
        prodPrice=row[2]
        


if(prodChecker==True):
    print("Product has found. \nProduct : "+product+"\nprice : Rs "+str(prodPrice))
else:
    print("Product has not found.")


PEOPLE_FOLDER = os.path.join('static', 'people_photo')





app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
@app.route('/home')
def home_page():
    
    return render_template('home.html', data=prodPrice)