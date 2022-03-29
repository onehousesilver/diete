# coding=utf8
import base64

class ImageIncoder():

    def getBase64String(self, string):
        try:
            with open(".\\images\\" + string +".jpg", "rb") as img:
                print(string + " 사진 있음!")
                return base64.b64encode(img.read())
        except:
            with open(".\\images\\음식사진없음.jpg", "rb") as img:
                print(string + " 사진 없음")
                return base64.b64encode(img.read())
        