# usage : to detect system error:

try:
    read = open("index.html")
    print(read.read())
    fet = 1 + "ffrf"
except Exception as e:
    print("Error type:",e)
finally:
    print("your file is read complletely.")