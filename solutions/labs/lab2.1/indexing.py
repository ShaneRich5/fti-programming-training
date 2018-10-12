a = 'New York'
b = 'Grand Rapids'
c = 'San Francisco'
d = 'Houston'
e = 'Atlanta'
f = 'Boston'

#print the word 'Chicago' by only concatenating indexes from the variables above

result = c[c.find('c')].upper() + d[0].lower() + b[b.find('i')] + c[c.find('c')] + e[-1] + b[0].lower() + f[1]

print(result)