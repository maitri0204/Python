x="Python"
print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.swapcase())

print(x.islower())
print(x.isupper())
print(x.istitle())

y='123'
print(y.isdigit())
print(y.isalnum())
print(y.isalpha())

z='--------Python---------'
print(z.strip('-'))
print(z.lstrip('-'))
print(z.rstrip('-'))

print(x.startswith('P'))
print(x.endswith('n'))
# count(), index(), replace()

alpha='abcdefghijklmnopqrstuvwxyz'
s='maitri'
print(alpha.index(s[0]))
t=''
i=0
t=t+(alpha[(((alpha.index(s[i]))+1)%26)])
print(t)