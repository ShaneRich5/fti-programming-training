a = 'All my life I thought air was free, until I bought a bag of chips today.'

b = 'Don\'t worry if plan A fails, there are 25 more letters in the alphabet.'

c = 'Doing nothing is hard, you never know when you\'re done.'

d = 'I\'m the literary equivalent of a big mac and fries.'

e = 'Those who think they know it all are very annoying to those of us who actually do.'

# print "I'm doing nothing today. I think it is annoying."
# tip: if it is tedious finding a word to slice, try embedding the "find" method.
# tip2: is there an easier way to slice from the end of the string?

result = d[0:4] + c[:14].lower() + a[-6:] + a[3] + d[0] + a[3] + e[10:16] + e[26:29] + c[14:17] + e[42:50] + c[-1]

print(result)