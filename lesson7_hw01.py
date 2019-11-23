st = "harry potter; 30; 127.45 galeon; auror"
st1 = st.split(";")
st2 = st1[0].split()
st3 = st1[2].split()
d = {"name":{"first_name":st2[0].title(), "last_name": st2[1].title()}, "age": st1[1], "profession": st1[3], "salary": {"amount": st3[0], "currency": st3[1]}}
print (d)
