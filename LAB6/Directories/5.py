lst = list(input().split())

with open('C:\Users\daule\OneDrive\Рабочий стол\LAB6\Directories') as f:
    for word in lst:
    	f.write(word + '\n')
cntnt = open('C:\Users\daule\OneDrive\Рабочий стол\LAB6\Directories')
f.close()

print(cntnt.read())