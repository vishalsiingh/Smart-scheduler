# import magic
# print(magic.from_file('C:\\Python313\\Scripts\\'))

import magic

file_type = magic.from_file(r'C:\Python313\python.exe')
print(file_type)
