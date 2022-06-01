
c=input('Digite la cadena')
c1=c.split()
c1=list(map(str.upper,c1))
print(c1)
withoutdupl=set(c1)
print(withoutdupl)