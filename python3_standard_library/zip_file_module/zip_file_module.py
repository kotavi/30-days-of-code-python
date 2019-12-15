from zipfile import ZipFile
import os

"""
Purpose: Read and write ZIP archive files.
The zipfile module can be used to manipulate ZIP archive files.
"""

zipping = ZipFile('additionalInfo.zip', 'w')
zipping.write('files/example.md')
zipping.write('files/info.txt')

print(zipping.namelist())

# Metadata in zip folder
for meta in zipping.infolist():
    print(meta)

info_file = zipping.getinfo('files/info.txt')
print(info_file)

# Access to files in zip folder
print(zipping.read('files/example.md'))

with open('files/info.txt') as f:
    print(f.read())

# Extract files
zipping.extract('files/example.md', 'extracted/')

zipping.close()

# Remove all created files and dirs
os.remove('additionalInfo.zip')
os.chdir("extracted/files/")
os.remove('example.md')
os.chdir("../")
os.rmdir('files')
os.chdir("../")
os.rmdir('extracted')