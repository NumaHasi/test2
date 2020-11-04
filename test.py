import os
#os.system("curl http://abehiroshi.la.coocan.jp/ > test8.html")
f = open("test8.html",'r')
markdown = open("test.md",'w')
#print(f.read() )
#markdown.write(f.read())
markdown.close()
f.close()

os.system("git add .")

os.system("git commit -m {}")

os.system("git push")