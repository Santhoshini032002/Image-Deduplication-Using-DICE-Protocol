from DBConnection import DBConnection
from Barchart import Barchart
import sys
def plotview():
    try:
        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select *from files")
        images = cursor.fetchall()
        bytes=0
        bytes1=0
        list=[]
        list.clear()
        for row in images:
            imgid=row[0]
            query = "SELECT LENGTH(img) FROM files where imgid='"+str(imgid)+"'"
            cursor.execute(query)
            imgdata = cursor.fetchall()
            for j in imgdata:
                print(j[0])
                bytes=bytes+int(j[0])
                #print("b=",bytes)


            for i in range(1,7):
                id=str(imgid)+"."+str(i)
                blck="b"+str(i)
                query="select "+blck+" from cloud where imgid=%s"
                print(id)
                print(blck)
                print("qry=",query)
                values = (str(id),)
                cursor.execute(query, values)
                b1=cursor.fetchone()[0]
                b11= str(b1).split("#")
                print("lenb=",len(b11))
                if len(b11)!= 2:
                    query = "select length("+blck+") from cloud where imgid=%s"
                    #print("select length("+blck+") from cloud where imgid=%s")
                    values = (str(id),)
                    cursor.execute(query, values)
                    bytes1 =bytes1+int(cursor.fetchone()[0])

        #print("bytes",bytes1)
        list.append(bytes1)
        list.append(bytes)
        chart=Barchart()
        chart.view(list)



    except Exception as e:
        print("Error=" + str(e.args[0]))
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)
        print(e)
plotview()
