import csv
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import mysql.connector
class Barchart:
    def view(self,bytes):

        plt.rcdefaults()
        objects = ('De-Duplication','Non-Deduplication')
        y_pos = np.arange(len(objects))
        plt.bar(y_pos,bytes, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Bytes')
        plt.title('Cloud Storage Analysis')
        plt.show()
