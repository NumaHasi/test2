import os
import time

for i in range(2):
        
    os.system("curl http://192.168.0.100/ > test.txt")
    f = open("test.txt",'r')
    d = open("data.txt","a")
    o = open("without.txt","w")
    
    #markdown = open("test.md",'w')
    
    
    line1=f.read()
    value1=line1.replace("water content is",str(i))
    value1=value1.replace("%","")
    d.write(value1+"\n")
    
  
        
        
    

    #markdown.write(value)
    
    #markdown.close()
    f.close()
    d.close()
    
    x=0
    
    with open("data.txt") as f:
        x=x+1
        line=f.readline()
        if x !=1:
            o.write(line)
    o.close()
    
    os.system("cp without.txt data.txt")
    
    

    os.system("curl http://192.168.0.101/ > test2.txt")
    f = open("test2.txt",'r')
    d = open("data2.txt",'a')
    markdown = open("test2.md",'w')
    
    line2=f.read()
    value2=line2.replace("water content is",str(i))
    value2=value2.replace("%","")
    d.write(value2+"\n")

    #markdown.write(value)
    #markdown.close()
    f.close()
    d.close()




    os.system("curl http://192.168.0.103/ > test3.txt")
    f = open("test3.txt",'r')
    d = open("data3.txt",'a')
    #markdown = open("test3.md",'a')
    
    line3=f.read()
    value3=line3.replace("water content is",str(i))
    value3=value3.replace("%","")
    d.write(value3+"\n")

    #markdown.write(value)
    #markdown.close()
    f.close()
    d.close()
    
    os.system("git add .")

    os.system("git commit -m {}")

    os.system("git push")
    
    os.system("gnuplot getGragh.gp")
    os.system("gnuplot getGragh2.gp")
    os.system("gnuplot getGragh3.gp")
    time.sleep(60)
    
        
    