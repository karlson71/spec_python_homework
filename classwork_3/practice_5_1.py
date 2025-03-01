import time
import string


st = 'My  test string - the best string. ' * 100
st = st.lower()

print(type(st))

z = ''.join(c for c in st if c not in string.punctuation)
y = list(set(z.strip().replace('  ','').split(' ')))
y.sort()


print(y)

# st_new = ','.join([st.replace(x, '') for x in string.punctuation])
#
# print(st_new)
# print(string.punctuation)
#
# print(set(st.split(',')))
# print(set(st))