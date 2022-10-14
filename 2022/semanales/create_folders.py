import os

n = 52 #cantidad de carpetas a generar desde 0
for i in range(n):
    name = str(i)

    if i in [0,1,2,3,4,5,6,7,8,9]:
        name = '0' + str(i)

    os.mkdir(name)
    readme = open(name + "/readme.md", "a")
    readme.close()
