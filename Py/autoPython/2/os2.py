import os
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize( os.path.join('C:\\Windows\\System32', filename) )
print('\n')
print(totalSize)