from crawler import entries

f = open('eksi.md', 'a', encoding="utf-8")

for i in range(1548):
    list = entries(i)
    if list:
        for entry in list:
           f.write('|' + entry + '| \n')