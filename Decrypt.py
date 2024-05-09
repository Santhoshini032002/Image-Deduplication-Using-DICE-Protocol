from DBConnection import DBConnection

import numpy as np
import sys
import cv2
import PIL.Image
import base64
from PIL import Image
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def decrypt(imgid,imgnm):
    try:
        database = DBConnection.getConnection()
        cursor = database.cursor()

        for x in range(1, 7):
            imid = str(imgid) + "." + str(x)
            qry = "SELECT *FROM cloud where imgid=%s"
            print("qrry=", qry)
            print("imiid=", imid)
            values = (str(imid),)
            # cursor.execute(qry, values)
            sl = "SELECT *FROM cloud where imgid='" + str(imid) + "'"
            print("sl=", sl)
            cursor.execute(sl)
            rows = cursor.fetchall()
            print("row=", rows)
            for r in rows:
                b1 = r[2]
                b2 = r[3]
                b3 = r[4]
                b4 = r[5]
                b5 = r[6]
                b6 = r[7]

                ct11 = str(b1).split("#")
                if len(ct11) == 2:
                    qry = "SELECT b1 FROM blockhash where imgid=%s"
                    print("qry1=", qry)
                    values = (str(ct11[0]),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    print("c=",ct11[0])
                    queery1 = "select AES_DECRYPT(b1,%s) from cloud where imgid=%s"
                    query1 = "select b1 from cloud where imgid=%s"
                    values = (str(ct11[0]),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data1 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data1, "./output/b1.jpg")

                else:
                    qry = "SELECT b1 FROM blockhash where imgid=%s"
                    print("qry1=", qry)
                    values = (str(imid),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b1,%s) from cloud where imgid=%s"
                    query1= "select b1 from cloud where imgid=%s"
                    values = (str(imid),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data1 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data1, "./output/b1.jpg")

                ct22 = str(b2).split("#")
                if len(ct22) == 2:
                    qry = "SELECT b2 FROM blockhash where imgid=%s"
                    print("qry2=", qry)
                    values = (str(ct22[0]),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b2,%s) from cloud where imgid=%s"
                    query1 = "select b2 from cloud where imgid=%s"
                    print("ct22[0]=", ct22[0])
                    values = (str(ct22[0]),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data2 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data2, "./output/b2.jpg")

                else:
                    qry = "SELECT b2 FROM blockhash where imgid=%s"
                    print("qry2=", qry)
                    values = (str(imid),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b2,%s) from cloud where imgid=%s"
                    query1 = "select b2 from cloud where imgid=%s"
                    values = (str(imid),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data2=base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data2, "./output/b2.jpg")

                ct33 = str(b3).split("#")
                if len(ct33) == 2:
                    qry = "SELECT b3 FROM blockhash where imgid=%s"
                    print("qry3=", qry)
                    values = (str(ct33[0]),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b3,%s) from cloud where imgid=%s"
                    query1 = "select b3 from cloud where imgid=%s"
                    values = (str(ct33[0]),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data3 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data3, "./output/b3.jpg")

                else:
                    qry = "SELECT b3 FROM blockhash where imgid=%s"
                    print("qry3=", qry)
                    values = (str(imid),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b3,%s) from cloud where imgid=%s"
                    query1 = "select b3 from cloud where imgid=%s"
                    values = (str(imid),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data3 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data3, "./output/b3.jpg")

                ct44 = str(b4).split("#")
                if len(ct44) == 2:
                    qry = "SELECT b4 FROM blockhash where imgid=%s"
                    print("qry4=", qry)
                    values = (str(ct44[0]),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b4,%s) from cloud where imgid=%s"
                    query1 = "select b4 from cloud where imgid=%s"
                    values = (str(ct44[0]),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data4 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data4, "./output/b4.jpg")

                else:
                    qry = "SELECT b4 FROM blockhash where imgid=%s"
                    print("qry4=", qry)
                    values = (str(imid),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b4,%s) from cloud where imgid=%s"
                    query1 = "select b4 from cloud where imgid=%s"
                    values = (str(imid),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data4 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data4, "./output/b4.jpg")

                ct55 = str(b5).split("#")
                if len(ct55) == 2:
                    qry = "SELECT b5 FROM blockhash where imgid=%s"
                    print("qry4=", qry)
                    values = (str(ct55[0]),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b5,%s) from cloud where imgid=%s"
                    query1 = "select b5 from cloud where imgid=%s"
                    values = (str(ct55[0]),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data5 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data5, "./output/b5.jpg")
                else:
                    qry = "SELECT b5 FROM blockhash where imgid=%s"
                    print("qry4=", qry)
                    values = (str(imid),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b5,%s) from cloud where imgid=%s"
                    query1 = "select b5 from cloud where imgid=%s"
                    values = (str(imid),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data5 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data5, "./output/b5.jpg")

                ct66 = str(b6).split("#")
                if len(ct66) == 2:
                    qry = "SELECT b6 FROM blockhash where imgid=%s"
                    print("qry4=", qry)
                    values = (str(ct66[0]),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b6,%s) from cloud where imgid=%s"
                    query1 = "select b6 from cloud where imgid=%s"
                    values = (str(ct66[0]),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data6 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data6, "./output/b6.jpg")

                else:
                    qry = "SELECT b6 FROM blockhash where imgid=%s"
                    print("qry4=", qry)
                    values = (str(imid),)
                    cursor.execute(qry, values)
                    hash = cursor.fetchone()[0]
                    print("h=", hash)
                    print("id=", imid)
                    queery1 = "select AES_DECRYPT(b6,%s) from cloud where imgid=%s"
                    query1 = "select b6 from cloud where imgid=%s"
                    values = (str(imid),)
                    cursor.execute(query1, values)
                    imgdata = cursor.fetchall()
                    data6 = base64.b64decode(imgdata[0][0])
                    # write blob data into a file
                    write_file(data6, "./output/b6.jpg")

                image1 = cv2.imread("./output/b1.jpg")
                image2 = cv2.imread("./output/b2.jpg")
                image3 = cv2.imread("./output/b3.jpg")
                image4 = cv2.imread("./output/b4.jpg")
                image5 = cv2.imread("./output/b5.jpg")
                image6 = cv2.imread("./output/b6.jpg")

                firsrt = np.concatenate((image1, image2, image3, image4, image5, image6), axis=1)
                cv2.imwrite("./output/"+str(x) + ".jpg", firsrt)

        ex = "SELECT img FROM files where imgid='" + str(imgid) + "'"
        cursor.execute(ex)
        imgs = cursor.fetchall()


        image1 = cv2.imread("./output/1.jpg")
        image2 = cv2.imread("./output/2.jpg")
        image3 = cv2.imread("./output/3.jpg")
        image4 = cv2.imread("./output/4.jpg")
        image5 = cv2.imread("./output/5.jpg")
        image6 = cv2.imread("./output/6.jpg")
        output = base64.b64decode(imgs[0][0])
        #outtPut = np.concatenate((image1, image2, image3, image4, image5, image6), axis=0)
        #cv2.imwrite("output.jpg", output)
        write_file(output, "output.jpg")


    except Exception as e:
            print("Error=" + str(e.args[0]))
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

#decrypt(1,"ct")
