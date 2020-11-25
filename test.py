import os
import time

for i in range(10):
        
    os.system("curl http://192.168.0.100/ > test.txt")
    f = open("test.txt",'r')
    d = open("data.txt","w")
    markdown = open("test.md",'w')
    line=f.read()
    value=line.replace("water content is",str(i))
    value=value.replace("%","")
    d.write(value)
    markdown.write(value)
    markdown.close()
    f.close()
    d.close()

    os.system("curl http://192.168.0.101/ > test2.txt")
    f = open("test2.txt",'r')
    markdown = open("test2.md",'w')

    markdown.write(f.read())
    markdown.close()
    f.close()

    os.system("curl http://192.168.0.100/ > test3.txt")
    f = open("test3.txt",'r')
    markdown = open("test3.md",'w')

    markdown.write(f.read())
    markdown.close()
    f.close()

    os.system("git add .")

    os.system("git commit -m {}")

    os.system("git push")
    
    time.sleep(60)
