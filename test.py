import os
import time

for i in range(5):
    
    #max hatarakikaisuu
        
    os.system("curl http://192.168.0.102/ > test.txt")
    f = open("test.txt",'r')
    d = open("water1","a")
    o = open("without.txt","w")
    #markdown = open("test.md",'w')
    line1=f.read()
    value1=line1.replace("water content is",str(i))
    

        
    
    
    
    #tuikasitayatu
    value1=value1.split("%")[0]
    
        #2/4 tuika
    #sankou atodekesu
#     if i>5:
#         
#         x=0
#         with open("water1") as f:
#             x=x+1
#             line=f.readline()
#             if x !=1:
#                 o.write(line)
#         o.close()
#         
#         os.system("cp without.txt water1")
#         

    
 
    #kokogayaritai
    
    x=value1.replace("0 ","")
    
    
#     k=open("withoutX.txt","w")
#     print(x)
# 
    if float(x) < 1792.8:
        
#
        x=str(float(x)/224.1)
        
#         if else:
#             x=str(x)
         
#         k.write(x)
#          
#         k.close()        
#      
         
       
    #2/4 kokomade
        
    #value1=value1.replace("%",".0")
    d.write(x+"\n")

    #markdown.write(value)
    
    #markdown.close()
    f.close()
    d.close() 
    
#     if i>5:
#         
#         x=0
#         with open("water1") as f:
#             x=x+1
#             line=f.readline()
#             if x !=1:
#                 o.write(line)
#         o.close()
#         
#         os.system("cp without.txt water1")
#         
        
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
    
    o = open("without2.txt","w") 
    #markdown = open("test2.md",'w')
    
    line2=f.read()
    value2=line2.replace("water content is",str(i))
    value2=value2.split("%")[0]    
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
    
    




    os.system("curl http://192.168.0.103/ > test3.txt")
    f = open("test3.txt",'r')
    d = open("water3",'a')
    #markdown = open("test3.md",'a')
    o = open("without3.txt","w")
    
    line3=f.read()
    value3=line3.replace("water content is",str(i))
    
    

    
    #value3=value3.removeprefix('%',str(i)   sippai
    
    
    #value3=value3.split("%")[0]

    value1=value1.split("%")[0]
    
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
    
    

    

    
    os.system("gnuplot getGragh.gp")
    os.system("gnuplot getGragh2.gp")
    os.system("gnuplot getGragh3.gp")
    
    os.system("git add .")

    os.system("git commit -m {}")

    os.system("git push")    
    time.sleep(2)