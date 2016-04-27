import arrayStorage

print(arrayStorage.arr)
print(arrayStorage.dic)

ks = arrayStorage.dic.keys()
ks.sort()
print(ks)

for key in ks:
    print(key, '=>', arrayStorage.dic[key])

i = 10
while i > 0:
    if i % 2 == 0:
        print(i)
    i -= 1

dic = arrayStorage.dic

dic['zxcv'] = [[1,2,3,4,5,6]]
print(dic)

if not 'zxcv' in dic:
    print('missing')
else:
    print('yes')

f = open('../script.txt' , 'w')
f.write('Hello\nmister\nJack!\n')
f.close()

f1 = open('../script.txt')
w = set(f1.read())
w1 = set('hello')
print(w-w1)