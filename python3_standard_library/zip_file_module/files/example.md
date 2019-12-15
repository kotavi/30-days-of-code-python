```python
import zipfile

zf = zipfile.ZipFile('example.zip')
for filename in [ 'README.txt', 'notthere.txt' ]:
    try:
        info = zf.getinfo(filename)
    except KeyError:
        print('ERROR: Did not find %s in zip file' % filename)
    else:
        print('%s is %d bytes' % (info.filename, info.file_size))
```