import tempfile

temp_file = tempfile.TemporaryFile()
temp_file.write(b"This is written to tempfile")
temp_file.seek(0)
print(temp_file.read())

temp_file.close()