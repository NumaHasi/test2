import os
import time


for i in range(60):
    if i > 0:
        x = 0
        o = open ("without.txt","w")
        with open("data.txt","r")as f:
            line = f.readline()
            x = x+1
            if x != 1:
                o.write(line)
        o.close()
        
        os.system("cp without.txt data.txt")
        
        x = 0
        o = open ("without2.txt","w")
        with open("data2.txt","r")as f:
            line = f.readline()
            x = x+1
            if x != 1:
                o.write(line)
        o.close()
        
        os.system("cp withou2.txt data2.txt")
        
        x = 0
        o = open ("without3.txt","w")
        with open("data3.txt","r")as f:
            line = f.readline()
            x = x+1
            if x != 1:
                o.write(line)
        o.close()
        
        os.system("cp without3.txt data3.txt")
        
    os.system("curl http://192.168.0.100/ > test.txt")
    f = open("test.txt",'r')
    d = open("data.txt","a")
    #markdown = open("test.md",'w')
    
    line1=f.read()
    value1=line1.replace("water content is",str(i)+str(.0))
    value1=value1.replace("%","")
    d.write(value1+"\n")
    
    
    #markdown.write(f.read())
    #markdown.close()
    f.close()
    d.close()

    os.system("curl http://192.168.0.101/ > test2.txt")
    f = open("test2.txt",'r')
    d = open("data2.txt","a")
    #markdown = open("test2.md",'w')
    
    line2=f.read()
    value2=line2.replace("water content is",str(i)+str(.0))
    value2=value2.replace("%","")
    d.write(value2+"\n")

    #markdown.write(f.read())
    #markdown.close()
    f.close()
    d.close()

    os.system("curl http://192.168.0.102/ > test3.txt")
    f = open("test3.txt",'r')
    d = open("data3.txt","a")
    #markdown = open("test3.md",'w')

    line3=f.read()
    value3=line3.replace("water content is",str(i)+str(.0))
    value3=value3.replace("%","")
    d.write(value3+"\n")

    #markdown.write(f.read())
    #markdown.close()
    f.close()
    d.close()

    os.system("git add .")

    os.system("git commit -m {}")

    os.system("git push")
    
    os.system("gnuplot getGraph.gp")
    os.system("gnuplot getGraph2.gp")
    os.system("gnuplot getGraph3.gp")
    
    time.sleep(60)
    
open("data.txt","w").close
open("data2.txt","w").close
open("data3.txt","w").close

