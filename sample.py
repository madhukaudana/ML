# import mysql.connector
from flask import Flask

from PIL import Image as PImage
import base64
from io import BytesIO

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="smartshopping"
# )
#
# sql_Query = "select * from product_details"
# cursor = db.cursor()
# cursor.execute(sql_Query)
# # getting all records from database prod_details table
# records = cursor.fetchall()
#
# product = "Watermelon"
# prodChecker = False
#
# prodWeight = None
# product_details = None
# img_Path = None
#
# for row in records:
#     if (product == row[1]):
#         prodChecker = True
#         product_details = {"name": row[1], "productPrice": row[2], 'productQuantity': row[4], "imgPath": row[5],
#                            "totalPrice": 350.00}
#         img_Path = row[5]
#
# # print(img_Path)
# # reading the selected image
# # image = PImage.open(img_Path)
# # oppening the selected image
# # image.show()
#
#
# # im_file = BytesIO()
# # image.save(im_file, format="JPEG")
# # im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
# # encoded_img_data = base64.b64encode(im_bytes)
#
# # print(type(encoded_img_data))
# if (prodChecker == True):
#     print("Product has found. \nProduct : " + product + "\nprice : Rs ")
# else:
#     print("Product has not found.")

product_details={"name": "watermelon", "productPrice":350, "productQuantity":1, "imgPath":"images/watermelon.jpg", "totalPrice": 350.00}
app = Flask(__name__)

@app.route("/productDetails")
def members():
    return product_details


if __name__ == "__main__":
    app.run(debug=True)

