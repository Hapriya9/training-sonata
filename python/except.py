def myfile():
    try:
        c = open('priya.txt','h')
       print(c.read())
    except(FileNotFoundError):
        return  ('not exists')
emp=myfile()
print(emp)