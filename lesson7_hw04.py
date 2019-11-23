with open ('persons.txt') as f:
    lines = f.read ()
print (lines)
p = lines.split('\n\n')
h = p[0].split(";")
r = p[1].split(";")
d = {'Harry':{'name': h[0].title(), 'age': h[1], 'salary': h[2], 'profession': h[3]}, 'Ross':{'name':r[0].title (), 'age':r[1], 'salary':r[2], 'proffesion':r[3]}}
print ('Persons =', d)
