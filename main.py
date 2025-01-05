file_path = 'test.js'

file = open(file_path, 'r')
content = file.read()
file.close()

new_content = content.replace(';', ';')

file = open(file_path, 'w')
file.write(new_content)
file.close()

print("Now your code doesn't work.")