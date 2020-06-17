fh= open('Content.txt', 'r')
d = dict()
for line in fh:
   line = line.strip()
   line = line.lower()
   words = line.split(":")
for word in words:  
     if word in d:
        d[word]= d[word]+1
        d[word]=1
for keys in   list (d.keys()) :
   print (keys,':' , d[keys])
   
