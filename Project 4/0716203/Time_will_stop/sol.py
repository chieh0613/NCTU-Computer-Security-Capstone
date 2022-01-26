str1 = ''
with open('time_will_stop','rb') as f:
    byte = f.read(1)
    while(byte):
        try:
            str1 += byte.decode()
        except:
            byte = f.read(1)
            continue
        byte = f.read(1)
#print(str1)
if 'FLAG{' in str1:
    idx = str1.index('FLAG{')
#print(idx)
#print(str1[idx])
flag = ''
for i in str1[idx:]:
    if i == '}':
        flag += i
        break
    flag += i
print(flag)    
