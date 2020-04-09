from crawler import entries

f = open('eksi.md', 'w+', encoding="utf-8")

f.write('| |\n')
f.write('| -- |')

for i in range(1, 2000):
    list = entries(i)
    if list != 404: # if there is content to show.
        for entry in list:
           f.write('\n|' + entry + '|')
    else:
        break