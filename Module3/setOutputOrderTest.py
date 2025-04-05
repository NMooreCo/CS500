import os
import sys



print("PYTHONHASHSEED =", os.environ['PYTHONHASHSEED'])
#print("PYTHONHASHSEED =", os.environ['PYTHONHASHSEED'])

# if os.environ.get('PYTHONHASHSEED') != '321':
#     os.environ['PYTHONHASHSEED'] = '123'
#     os.execv(sys.executable, [sys.executable] + sys.argv)


# print("PYTHONHASHSEED =", os.environ['PYTHONHASHSEED'])

# Set = {5,1,2.6,"python"}
# for i in range(1,20):
#     print(Set)