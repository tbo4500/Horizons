dict = {'a':2, 'b':1, 'c':3}
array = sorted(dict.iteritems(), key=lambda k:k[1], reverse=True)
print array
