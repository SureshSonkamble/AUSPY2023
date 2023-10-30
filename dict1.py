dict={
'1':'aaa',
'2':'bbb',
'3':'ccc',
'kk':'vvvv',
'kk':'nnn',
    }
print(dict)
dict['3']='zzz'
print(dict)
dict['4']='ddd'
print(dict)
dict.pop('kk')
print(dict)
print(len(dict))
print(dict.get('1'))
print(dict.get('3'))
print(dict.get('6'))

dict.clear()
print(dict)


'''for i in dict:
    print(i)
    print(dict.get(i))'''

