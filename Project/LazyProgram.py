f = open('lazy.txt','r+')
w = open("lazer.txt", 'w')
f = f.read().split('\n')
print(f)
for i in range(len(f)-1):
    print(f[i+1])
    w.write("df= df.replace({'state': r'"+f[i+1]+"'}, {'state':"+str(i)+"}, regex=True)\n")

w.close()