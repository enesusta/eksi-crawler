from crawler import entries

f = open('eksi.md', 'a', encoding="utf-8")

for i in range(1, 2000):
    list = entries(i)
    if list != 404:
        for entry in list:
           f.write('\n|' + entry + '|')
    else:
        break