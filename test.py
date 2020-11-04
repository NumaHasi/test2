import os

#os.system("curl http://abehiroshi.la.coocan.jp/ > test.txt")
f = open("test.txt",'r')
markdown = open("test.md",'w')

markdown.write(f.read())
markdown.close()
f.close()

os.system("git add .")

os.system("git commit -m {}")

os.system("git push")