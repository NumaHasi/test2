import os

os.system("curl http://192.168.0.100/ > test.txt")
f = open("test.txt",'r')
markdown = open("test.md",'w')

os.system("curl http://192.168.0.100/ > test2.txt")
f = open("test2.txt",'r')
markdown = open("test2.md",'w')

os.system("curl http://192.168.0.100/ > test3.txt")
f = open("test3.txt",'r')
markdown = open("test3.md",'w')

markdown.write(f.read())
markdown.close()
f.close()

os.system("git add .")

os.system("git commit -m {}")

os.system("git push")