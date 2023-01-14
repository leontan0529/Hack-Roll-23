import os

n = os.stat("./uploads/sample.txt").st_size 
print(n == 0)