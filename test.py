import os
import time

<<<<<<< HEAD
for i in range(5):
=======

for i in range(60):
    if i > 3:
        x = 0
        o = open ("without.txt","w")
        with open("water1","r")as f:
            line = f.readline()
            x = x+1
            if x !=1:
                o.write(line)
        o.close()
        
        os.system("cp without.txt data.txt")
        
        x = 0
        o = open ("without2.txt","w")
        with open("water2","r")as f:
            line = f.readline()
            x = x+1
            if x != 1:
                o.write(line)
        o.close()
        
        os.system("cp withou2.txt data2.txt")
        
        x = 0
        o = open ("without3.txt","w")
        with open("water3","r")as f:
            line = f.readline()
            x = x+1
            if x != 1:
                o.write(line)
        o.close()
        
        os.system("cp without3.txt data3.txt")
>>>>>>> 6ad6f06fed6cd5699e8d7a91584fb67fc4c7f009
        
    os.system("curl http://192.168.0.102/ > test.txt")
    f = open("test.txt",'r')
    d = open("water1","a")
<<<<<<< HEAD
    o = open("without.txt","w")    
    #markdown = open("test.md",'w')
    line1=f.read()    
    value1=line1.replace("water content is",str(i))
    #tuikasitayatu
    value1=value1.split("%")[0]
    
    #value1=value1.replace("%",".0")
    d.write(value1+"\n")
    
  
        
        
    

    #markdown.write(value)
    
    #markdown.close()
    f.close()
    d.close()
    
    if i>2:
        
        x=0
        with open("water1") as f:
            x=x+1
            line=f.readline()
            if x !=1:
                o.write(line)
        o.close()
        
        os.system("cp without.txt water1")
        
        
    f = open("test.txt",'r')
    c = open("kasoku.txt","w")
    speed1=f.read()
    
    #s=open("without-kasoku.txt","w")
    
    #s.write
    speed1=speed1.split("%")[1]
    c.write(speed1)
    c.close()
    
#       with open("test.txt") as f:
#           next(f)
#           for line in f :
#               print(line.strip("\n"))
    

    os.system("curl http://192.168.0.101/ > test2.txt")
    f = open("test2.txt",'r')
    d = open("water2",'a')
    markdown = open("test2.md",'w')
    
    line2=f.read()
    value2=line2.replace("water content is",str(i))
    value2=value2.replace("%","")
    
    d.write(value2+"\n")

    #markdown.write(value)
    #markdown.close()
    f.close()
    d.close()
    
    if i>2:
        
        x=0
        with open("water2") as f:
            x=x+1
            line=f.readline()
            if x !=1:
                o.write(line)
        o.close()
        
        os.system("cp without2.txt water2")
    
    




    os.system("curl http://192.168.0.102/ > test3.txt")
    f = open("test3.txt",'r')
    d = open("water3",'a')
    #markdown = open("test3.md",'a')
    
    line3=f.read()
    value3=line3.replace("water content is",str(i))
    
    

    
    #value3=value3.removeprefix('%',str(i)   sippai
    
    
    #value3=value3.split("%")[0]

    value3=value3.replace("%","")
    
#     import re
#     r=re.compile("(.*)(acc)(.*)")
#     m=r.match(value3)
#     print m.group(1)
    
    
    
    
    
    
    d.write(value3+"\n")

    #markdown.write(value)
    #markdown.close()
    f.close()
    d.close()
    
    if i>2:
        
        x=0
        with open("water3") as f:
            x=x+1
            line=f.readline()
            if x !=1:
                o.write(line)
        o.close()
        
        os.system("cp without3.txt water3")
    
    
=======
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
    d = open("water2","a")
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
    d = open("water3","a")
    #markdown = open("test3.md",'w')

    line3=f.read()
    value3=line3.replace("water content is",str(i)+str(.0))
    value3=value3.replace("%","")
    d.write(value3+"\n")

    #markdown.write(f.read())
    #markdown.close()
    f.close()
    d.close()
>>>>>>> 6ad6f06fed6cd5699e8d7a91584fb67fc4c7f009

    
    os.system("git add .")

    os.system("git commit -m {}")

    os.system("git push")
    
<<<<<<< HEAD
    os.system("gnuplot getGragh.gp")
    os.system("gnuplot getGragh2.gp")
    os.system("gnuplot getGragh3.gp")
    time.sleep(6)
    
        
    
=======
    os.system("gnuplot getGraph.gp")
    os.system("gnuplot getGraph2.gp")
    os.system("gnuplot getGraph3.gp")
    
    time.sleep(30)
    
open("water1","w").close
open("water2","w").close
open("water3","w").close

>>>>>>> 6ad6f06fed6cd5699e8d7a91584fb67fc4c7f009
