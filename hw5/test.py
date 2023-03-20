
import numpy as np
f = open('rules_in_List.txt','r+')

t = f.readlines()
h= f.readline()
print(len(t))
print(t[0][:-1])
print(t)
""" f = f.replace('[', '')
f = f.replace(']', '')
f = f.replace(',','')
f= f.replace('\'', '')
#
f = f.replace('\n', ' ')
f = f.split(" ")
#f = f[:-1]
print(f[:-1]) """

""" new_arr = []
for i in range(0,len(f)):
    print(i%3)
    if(i%3 <= 1):
        print("If here" , i)
        print('f',f[i])
        new_arr.append(int(f[i]))
    elif(i%3 == 2 ):
        #print("elfi here", i)
        #print('\'',str(f[i]),'\'')
        new_arr .append(str(f[i]))

#print('new_arr',new_arr)

right_f = []
left_f = []
center_f = []
_2_arr = []
hold = []

right_f=new_arr[-3:]
#print(len(right_f))

left_f = new_arr[:-3]
#print('left',left_f)
nw_left = []
for i in range(len(left_f)):
    #print(left_f[i])
    hold.append(left_f[i])
    #print('hold',hold)
    if(len(hold) == 3):
        nw_left.append(hold)
        #print('in if nw_left',nw_left)
        hold = []

print('nw_left',nw_left)
print('right_f',right_f)
_2_arr.append(nw_left)
_2_arr.append(right_f)

print('2arr',_2_arr[0]) """
