
f = open('tests.txt', "r+")
l = f.readlines()
fix = 'fix'
word = 'tehre'
for i in l:
    if word in i:
        replacement = i.replace(word, fix)
        l = replacement

print(l)
f.truncate(0)
f.seek(0)
f.writelines(l)
print(f.readlines())

