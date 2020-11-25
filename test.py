import os
import time


for i in range(2):
        
    os.system("curl http://192.168.0.100/ > test.txt")
    f = open("test.txt",'r')
    d = open("data.txt","a")
    markdown = open("test.md",'w')
    
    line1=f.read()
    value1=line1.replace("water content is",str(i))
    value1=value1.replace("%","")
    d.write(value1)
    
    #gnuplot "test.gn"
    #plot 'data.txt'
    #set terminal png
    #replot
    #set output "data.png"
    
    markdown.write(f.read())
    
    markdown.close()
    f.close()
    d.close()

    os.system("curl http://192.168.0.101/ > test2.txt")
    f = open("test2.txt",'r')
    d = open("data2.txt","a")
    markdown = open("test2.md",'w')
    
    line2=f.read()
    value2=line2.replace("water content is",str(i))
    value2=value2.replace("%","")
    d.write(value2)

    markdown.write(value2)
    markdown.close()
    f.close()
    d.close()

    os.system("curl http://192.168.0.102/ > test3.txt")
    f = open("test3.txt",'r')
    markdown = open("test3.md",'w')

    markdown.write(f.read())
    markdown.close()
    f.close()

    os.system("git add .")

    os.system("git commit -m {}")

    os.system("git push")
    
    time.sleep(60)
