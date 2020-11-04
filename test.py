import os

os.system("curl https://researchmap.jp/read0088195 > test.txt")
f = open("test.txt",'r')
markdown = open("test.md",'w')

markdown.write(f.read())
markdown.close()
f.close()

os.system("git add .")

os.system("git commit -m {}")

os.system("git push")