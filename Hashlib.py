import imagehash
from PIL import Image

import sys
class Hashlib:

    def sha256(self,image):
        try:
          img=Image.open(image)
          #print("img=",image)
          hash=imagehash.average_hash(img)
          print("hashh",hash)
          return hash
        except Exception as e:
         print("Error1=" + e.args[0])
         tb = sys.exc_info()[2]
         print(tb.tb_lineno)
    def hashing(self,shash):
        hash = imagehash.average_hash(shash)
        print(hash)
if __name__ == '__main__':
    hl=Hashlib()
    hl.hashing("add")
