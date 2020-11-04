import os


os.system("curl https://twitter.com/abeshinzo > test8.html")

f = open("test8.html",'r')

markdown = open("test.md",'w')


#print(f.read() )


markdown.write(f.read() )


markdown.close()
f.close()

os.system("git push")