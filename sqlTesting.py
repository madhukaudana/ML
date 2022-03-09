import mysql.connector
from flask import Flask, render_template
from PIL import Image as PImage
import base64
from io import BytesIO
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
#printing database row count
#print("Total number of rows in table: ", cursor.rowcount)

product = "Watermelon"  #to test
prodChecker= False

prodWeight=None
product_details=None
img_Path=None

#checking product with database
for row in records:               
    if(product==row[1]):
        prodChecker=True
        product_details={'name':row[1],'productPrice':row[2], 'productQuantity':row[4]}
        img_Path=row[5]

        
#reading the selected image
image = PImage.open(img_Path)
#oppening the selected image
#image.show()


im_file = BytesIO()
image.save(im_file, format="JPEG")
im_bytes = im_file.getvalue()  #image in binary format.
encoded_img_data = base64.b64encode(im_bytes)

#print(type(encoded_img_data))
if(prodChecker==True):
    print("Product has found. \nProduct : "+product+"\nprice : Rs ")
else:
    print("Product has not found.")



app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    
    return render_template('home.html', img_data=encoded_img_data.decode('utf-8'), data=product_details)