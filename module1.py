def hello():
    print("hello from module1")

if __name__== "__main__":
   print("Execute module1 directly")
   hello()
else:
    print ("module1 imported")
