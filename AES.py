import mysql.connector
import hashlib
from PIL import Image
import image_slicer
from DBConnection import DBConnection
from Hashlib import Hashlib
import glob
import imagehash
import os
import base64
import base64
import sys
from mysql.connector import MySQLConnection, Error
class AES:

    def tags(self,id,filename):
        try:
            query = "SELECT *FROM temp"
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            for r in row:
                ct1 = r[0]
                ct2 = r[1]
                ct3 = r[2]
                ct4 = r[3]
                ct5 = r[4]
                ct6 = r[5]
            tag1 = hashlib.sha256(base64.b64decode(ct1)).hexdigest()
            tag2 = hashlib.sha256(base64.b64decode(ct2)).hexdigest()
            tag3 = hashlib.sha256(base64.b64decode(ct3)).hexdigest()
            tag4 = hashlib.sha256(base64.b64decode(ct4)).hexdigest()
            tag5 = hashlib.sha256(base64.b64decode(ct5)).hexdigest()
            tag6 = hashlib.sha256(base64.b64decode(ct6)).hexdigest()
            #print("tag1", tag1)
            #print("tag2", tag2)
            #self.duplicatecheck(id,filename,str(tag1),str(tag2),str(tag3),str(tag4),str(tag5),str(tag6),ct1,ct2,ct3,ct4,ct5,ct6)
            values = (id, filename, str(tag1), str(tag2),str(tag3),str(tag4),str(tag5),str(tag6))
            query = "insert into tags values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()


        except Exception as e:
            print("Error2=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    def duplicatecheck(self,id,filename,tag1,tag2,tag3,tag4,tag5,tag6,ct1,ct2,ct3,ct4,ct5,ct6):
        try:
            b = 0;
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("select *from tags")
            row = cursor.fetchall()
            for r in row:
                imgid = r[0]
                #####    block1  ######
                sql = "select *from tags where b1=%s and imgid=%s"
                values = (tag1,imgid)
                cursor.execute(sql,values)
                one = cursor.fetchone()
                if str(one)!='None':
                    ref=imgid+"#b1"
                    sql="insert into checks values(%s)"
                    values = (ref,)
                    print("val",values)
                    cursor.execute(sql,values)
                    database.commit()
                else:
                    sql = "insert into checks values(%s)"
                    print("sql1=", sql)
                    values = (ct1,)
                    print("val",values)
                    cursor.execute(sql,values)
                    database.commit()
                #####    block2  ######

                sql = "select *from tags where b2=%s and imgid=%s"
                values = (tag2, imgid)
                cursor.execute(sql, values)
                one = cursor.fetchone()
                if str(one) != 'None':
                    ref = imgid + "#b2"
                    sql = "insert into checks values(%s)"
                    values = (ref,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()
                else:
                    sql = "insert into checks values(%s)"
                    print("sql2=", sql)
                    values = (ct2,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()

             #####    block3  ######

                sql = "select *from tags where b3=%s and imgid=%s"
                values = (tag3, imgid)
                cursor.execute(sql, values)
                one = cursor.fetchone()
                if str(one) != 'None':
                    ref = imgid + "#b3"
                    sql = "insert into checks values(%s)"
                    values = (ref,)
                    print("val",values)
                    cursor.execute(sql, values)
                    database.commit()
                else:
                    sql = "insert into checks values(%s)"
                    print("sql3=", sql)
                    values = (ct3,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()

             #####    block4  ######

                sql = "select *from tags where b4=%s and imgid=%s"
                values = (tag4, imgid)
                cursor.execute(sql, values)
                one = cursor.fetchone()
                if str(one) != 'None':
                    ref = imgid + "#b4"
                    sql = "insert into checks values(%s)"
                    values = (ref,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()
                else:
                    sql = "insert into checks values(%s)"
                    print("sql4=", sql)
                    values = (ct4,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()

                #####    block5  ######

                sql = "select *from tags where b5=%s and imgid=%s"
                values = (tag5, imgid)
                cursor.execute(sql, values)
                one = cursor.fetchone()
                if str(one) != 'None':
                    ref = imgid + "#b5"
                    sql = "insert into checks values(%s)"
                    values = (ref,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()
                else:
                    sql = "insert into checks values(%s)"
                    print("sql5=", sql)
                    values = (ct5,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()

                #####    block6  ######

                sql = "select *from tags where b6=%s and imgid=%s"
                values = (tag6, imgid)
                cursor.execute(sql, values)
                one = cursor.fetchone()
                if str(one) != 'None':
                    ref = imgid + "#b6"
                    sql = "insert into checks values(%s)"
                    values = (ref,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()
                else:
                    sql = "insert into checks values(%s)"
                    print("sql6=", sql)
                    values = (ct6,)
                    print("val", values)
                    cursor.execute(sql, values)
                    database.commit()

                query = "SELECT res FROM checks"
                cursor.execute(query)
                row = cursor.fetchall()
                ct1, = row[0]
                ct2, = row[1]
                ct3, = row[2]
                ct4, = row[3]
                ct5, = row[4]
                ct6, = row[5]
                cursor.execute("delete from checks")
                database.commit()
            values = (id,filename, ct1, ct2, ct3, ct4, ct5, ct6)
            query = "insert into cloud values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()

            values = (id, filename, str(tag1), str(tag2),str(tag3),str(tag4),str(tag5),str(tag6))
            query = "insert into tags values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()


        except Exception as e:
            print("Error1=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def ENCRYPT(self,id, filename,fp,imgdata,unm):

        tiles = image_slicer.slice(fp, 6 * 6, save=False)
        image_slicer.save_tiles(tiles, directory='./blocks')
        all_files = glob.glob('./blocks/*.png')
        c = 0
        self.write_file1(imgdata)
        query = "SELECT img,imgid FROM files"
        database = DBConnection.getConnection()
        cursor = database.cursor()
        try:
            my_dict={}
            cursor.execute(query)
            images = cursor.fetchall()
            for row in images:
                img = row[0]
                imgid = row[1]
                img = base64.b64decode(img)
                self.write_file(img)
                hash = imagehash.average_hash(Image.open('train.jpg'))
                print(hash)
                hash1 = imagehash.average_hash(Image.open('test.jpg'))
                print(hash1)
                thrv=hash - hash1
                print(thrv)
                my_dict[int(imgid)]=int(thrv)
            key_min = min(my_dict,key=lambda x: my_dict.get(x))
            #print("key=",key_min)
            #print('Min Value: ', my_dict[key_min])
            #print('Min Value: ', my_dict)
            query = "SELECT img,imgid FROM files where imgid="+str(key_min)
            print("q=",query)
            cursor = database.cursor()
            cursor.execute(query)
            images = cursor.fetchall()
            for row in images:

                imglst = []
                id1 = 0
                img = row[0]
                imgid = row[1]
                imgid1 = id
                imgg = base64.b64decode(img)
                self.write_file1(imgg)
                tiles = image_slicer.slice("test.jpg", 6 * 6, save=False)
                image_slicer.save_tiles(tiles, directory='./test')

                for file1 in all_files:
                    print(file1)
                    path, file = os.path.split(file1)
                    c = c + 1
                    if c < 6:
                        imglst.append(str(file))
                    else:
                        imglst.append(str(file))
                        id1 = id1 + 1
                        id2 = str(imgid) + "." + str(id1)
                        id3 = str(imgid1) + "." + str(id1)
                        self.duplicatcheck(imglst, id3, filename)
                        imglst.clear()
                        c = 0

            query = "insert into files values(%s,%s,%s,%s)"
            imgdata=base64.b64encode(imgdata)
            values = (id,filename,imgdata,unm)
            cursor.execute(query, values)
            database.commit()



        except Error as e:
            #print(e)
            print("Error=" + str(e.args[0]))
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def duplicatcheck(self,img,imgid1,filename):
        try:

            i = 0;
            c = 0
            haslib = Hashlib()
            hashlst = []
            hashlst1 = []
            taglst = []
            hashlst.clear()
            hashlst1.clear()
            taglst.clear()

            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("delete from checks")
            database.commit()
            for row in img:
                i = i + 1
                print("img=", str(row))
                hash = haslib.sha256('./test/' + str(row))
                hash1 = haslib.sha256('./blocks/' + str(row))
                print("hash=",hash)
                print("hash1=", hash1)
                thv = hash - hash1
                print("v=", thv)
                if thv == 0 or thv == 1 or thv == 2 or thv == 3 or thv == 4 or thv == 5 or thv == 6 or thv == 7 or thv == 8 or thv == 9 or thv == 10:
                    b = "b" + str(i)
                    imgidd2=0
                    qry = "SELECT imgid FROM blockhash where "+b+"=%s  limit 1"
                    print("qry=",qry)
                    print("hash=", str(hash))
                    values = (str(hash),)
                    cursor.execute(qry,values)
                    print("cursor=",cursor.rowcount)
                    imgidd= cursor.fetchall()
                    print("lenimg=",len(imgidd))
                    print("cursor1=", cursor.rowcount)

                    #print("imgidddd=",imgidd1[0])
                    if len(imgidd)!=0:
                        imgidd1 = imgidd[0]
                        imgidd2=str(imgidd1[0])
                        bkid = str(imgidd1[0]) + "#b" + str(i)
                        sql = "insert into checks values(%s)"
                        values = (bkid,)
                        print("val", values)
                        cursor.execute(sql,values)
                        database.commit()
                    else:
                        qrryy = "SELECT imgid FROM refhash where blockhash=%s  limit 1"
                        print("qrryy=", qrryy)
                        print("hash=", str(hash1))
                        values = (str(hash1),)
                        cursor.execute(qrryy, values)
                        imgid = cursor.fetchone()[0]
                        imgidd2=imgid
                        bkid = imgid + "#b" + str(i)
                        sql = "insert into checks values(%s)"
                        values = (bkid,)
                        print("val", values)
                        cursor.execute(sql, values)
                        database.commit()

                    sql = "insert into refhash values(%s,%s)"
                    values = (str(imgidd2),str(hash1))
                    print("vall=", values)
                    cursor.execute(sql, values)
                    database.commit()
                    hashlst.append(str(hash))

                else:
                    sqll = "insert into checks values(AES_ENCRYPT(%s,%s))"
                    sql = "insert into checks values(%s)"
                    print("sql=" + str(i), sql)
                    bdata = self.read_file('./blocks/' + row)
                    bdataa = base64.b64encode(bdata)
                    hashh = haslib.sha256('./blocks/' + row)
                    values = (bdataa,)
                    cursor.execute(sql, values)
                    database.commit()
                    hashlst.append(str(hashh))
                    hashlst1.append(str(hash1))

            query = "SELECT res FROM checks"
            cursor.execute(query)
            row = cursor.fetchall()
            #print("r0=", row[0])
            ct1, = row[0]
            ct2, = row[1]
            ct3, = row[2]
            ct4, = row[3]
            ct5, = row[4]
            ct6, = row[5]
            print( ct1)
            ct11 = str(ct1).split("#")
            print("ct111=",len(ct11))
            if len(ct11) == 2:
                ct12= ct11[0]
                print("ct12=", ct12)
                ct13 = ct11[1]
                print("ct13=", ct13)
                imid =ct12[2:]
                blck = ct13[0:2]
                qry = "SELECT " + blck + " FROM tags where imgid=%s"
                print("qry=", qry)
                print("imgid=", imid)
                values = (imid,)
                cursor.execute(qry, values)
                tag = cursor.fetchone()[0]
                print("tg=", tag)
                taglst.append(tag)
                print("if")
            else:
                tag = hashlib.sha256(base64.b64decode(ct1)).hexdigest()
                taglst.append(tag)

            ct22 = str(ct2).split("#")
            print("ct22=", len(ct22))
            if len(ct22) == 2:
                ct12 = ct22[0]
                ct13 = ct22[1]
                imid = ct12[2:]
                blck = ct13[0:2]
                qry = "SELECT " + blck + " FROM tags where imgid=%s"
                values = (imid,)
                cursor.execute(qry, values)
                tag = cursor.fetchone()[0]
                taglst.append(tag)
                print("if2")
            else:
                tag = hashlib.sha256(base64.b64decode(ct2)).hexdigest()
                taglst.append(tag)

            ct33 = str(ct3).split("#")
            print("ct33=", len(ct33))
            if len(ct33) == 2:
                ct12 = ct33[0]
                ct13 = ct33[1]
                imid = ct12[2:]
                print("ct13=",ct13)
                blck = ct13[0:2]
                print("blck=",blck)
                qry = "SELECT " + blck + " FROM tags where imgid='"+imid+"' "
                print("qry=",qry)
                #values = (imid,)
                cursor.execute(qry)
                tag = cursor.fetchone()[0]
                print("tag=",tag)
                taglst.append(tag)
                print("if3")
            else:
                tag = hashlib.sha256(base64.b64decode(ct3)).hexdigest()
                taglst.append(tag)

            ct44 = str(ct4).split("#")
            print("ct44=", len(ct44))
            if len(ct44) == 2:
                ct12 = ct44[0]
                ct13 = ct44[1]
                imid = ct12[2:]
                blck = ct13[0:2]
                qry = "SELECT " + blck + " FROM tags where imgid=%s"
                values = (imid,)
                cursor.execute(qry, values)
                tag = cursor.fetchone()[0]
                taglst.append(tag)
            else:
                tag = hashlib.sha256(base64.b64decode(ct4)).hexdigest()
                taglst.append(tag)

            ct55 = str(ct5).split("#")
            print("ct555=", len(ct55))
            if len(ct55) == 2:
                ct12 = ct55[0]
                ct13 = ct55[1]
                imid = ct12[2:]
                blck = ct13[0:2]
                qry = "SELECT " + blck + " FROM tags where imgid=%s"
                values = (imid,)
                cursor.execute(qry, values)
                tag = cursor.fetchone()[0]
                taglst.append(tag)
            else:
                tag = hashlib.sha256(base64.b64decode(ct5)).hexdigest()
                taglst.append(tag)

            ct66 = str(ct6).split("#")
            print("ct66=", ct66)
            if len(ct66) == 2:
                ct12 = ct66[0]
                ct13 = ct66[1]
                imid = ct12[2:]
                blck = ct13[0:2]
                qry = "SELECT " + blck + " FROM tags where imgid=%s"
                values = (str(imid),)
                cursor.execute(qry, values)
                tag = cursor.fetchone()[0]
                taglst.append(tag)
            else:
                tag = hashlib.sha256(base64.b64decode(ct6)).hexdigest()
                taglst.append(tag)
            #print("imgid=", imgid)
            values = (
            str(imgid1), filename, str(taglst[0]), str(taglst[1]), str(taglst[2]), str(taglst[3]), str(taglst[4]),
            str(taglst[5]))
            query = "insert into tags values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()

            values = (
            imgid1, filename, str(hashlst[0]), str(hashlst[1]), str(hashlst[2]), str(hashlst[3]), str(hashlst[4]),
            str(hashlst[5]))
            query = "insert into blockhash values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()

            '''valuess = (
                imgid1, filename, str(hashlst1[0]), str(hashlst1[1]), str(hashlst1[2]), str(hashlst1[3]), str(hashlst1[4]),
                str(hashlst1[5]))
            queryy = "insert into refhash values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(queryy, valuess)
            database.commit()'''

            values = (imgid1, filename, ct1, ct2, ct3, ct4, ct5, ct6,)
            query = "insert into cloud values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()

            cursor.execute("delete from checks")
            database.commit()
            c = c + 1
            print("count=", c)



        except Error as e:
            print("Error=" + str(e.args[0]))
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def write_file(self,data):
        with open("train.jpg", 'wb') as f:
            f.write(data)

    def write_file1(self,data):
        with open("test.jpg", 'wb') as f:
            f.write(data)

    def read_file(self,filename):
        with open(filename, 'rb') as f:
            photo = f.read()
        return photo

    def ENCRYPTT(self,id,filename,img,hash):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            bh1 = hash[0]
            bh2 = hash[1]
            bh3 = hash[2]
            bh4 = hash[3]
            bh5 = hash[4]
            bh6 = hash[5]
            values = (id, filename, bh1, bh2, bh3, bh4, bh5, bh6)
            query = "insert into blockhash values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()
            bdata1 = self.read_file(img[0])
            bdata11= base64.b64encode(bdata1)
            bdata2 = self.read_file(img[1])
            bdata22 = base64.b64encode(bdata2)
            bdata3 = self.read_file(img[2])
            bdata33 = base64.b64encode(bdata3)
            bdata4 = self.read_file(img[3])
            bdata44 = base64.b64encode(bdata4)
            bdata5 = self.read_file(img[4])
            bdata55 = base64.b64encode(bdata5)
            bdata6 = self.read_file(img[5])
            bdata66 = base64.b64encode(bdata6)

            cursor.execute("delete from temp")
            database.commit()

            values = (bdata11, bdata22, bdata33, bdata44, bdata55, bdata66,)
            #query = "insert into temp values(AES_ENCRYPT(%s,'" + bh1 + "'),AES_ENCRYPT(%s,'" + bh2 + "'),AES_ENCRYPT(%s,'" + bh3 + "'),AES_ENCRYPT(%s,'" + bh4 + "'),AES_ENCRYPT(%s,'" + bh5 + "'),AES_ENCRYPT(%s,'" + bh6 + "'))"
            query = "insert into temp values(%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()
            self.tags(id, filename)
            # self.temp(id,filename)
            values = (id, filename,bdata11, bdata22, bdata33, bdata44, bdata55, bdata66,)
            #query = "insert into cloud values(%s,%s,AES_ENCRYPT(%s,'" + bh1 + "'),AES_ENCRYPT(%s,'" + bh2 + "'),AES_ENCRYPT(%s,'" + bh3 + "'),AES_ENCRYPT(%s,'" + bh4 + "'),AES_ENCRYPT(%s,'" + bh5 + "'),AES_ENCRYPT(%s,'" + bh6 + "'))"
            query = "insert into cloud values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, values)
            database.commit()



        except Exception as e:
            print("Error1=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


'''
if __name__ == '__main__':
    aes=AES()'''
