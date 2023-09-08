arr = ["1.py", "2.py"]
line = "__all__ = " + str(arr)
print(line)

openI = line.find('[')
closeI = line.find(']')
print(line[openI+1:closeI])

names = line[openI+1:closeI].split(',')
for n in range(len(names)):
    names[n] = names[n].strip(' ').strip('\'').strip('\"')
print(names)