import string
step = 3
keys = list(string.ascii_lowercase) 
values = list(string.ascii_lowercase[step:] + string.ascii_lowercase[:step]) 
d = dict (zip(keys, values))
print (d)
