
## eksi-crawler

<div align="center">

[![HitCount](http://hits.dwyl.com/enesusta/eksi-crawler.svg)](http://hits.dwyl.com/enesusta/eksi-crawler)
![GitHub language count](https://img.shields.io/github/languages/count/enesusta/eksi-crawler?color=green)
![GitHub last commit](https://img.shields.io/github/last-commit/enesusta/eksi-crawler)

</div>

<p align="center">
<img src="https://camo.githubusercontent.com/821bd5dd17620c871e81b8760a97cdf50219f551/68747470733a2f2f656b7369736f7a6c756b2e636f6d2f636f6e74656e742f696d672f6e65772d64657369676e2f656b7369736f7a6c756b5f6c6f676f2e737667" width=300 height=300>
</p>

Ekşi Sözlük is one of the most popular social media platform in Turkey.

<p align="center">
    <img src="https://raw.githubusercontent.com/enesusta/assets-host-for-github-pages/assets/eksi-crawler/eksi-crawler.gif">
</p>

### Installation

```bash
git clone https://github.com/enesusta/eksi-crawler
cd eksi-crawler
pip install -r requirements.txt 
```


### How to use it?

`Assume that we have a title which we want to examine`

For example:

- https://eksisozluk.com/almanya--49635

#### How you can change title?

Go `./request.py`

You will see a variable named host.

```py
host='https://eksisozluk.com/almanya--49635'
```

Change it and save.

---

We have keywords and we want matches those entries on crawling.

`keywords.txt` located in root path.

I added some examples that demonstrates how eksi-crawler works



```txt
java
Java
Javascript
JavaScript
javascript
yazılım
Yazılım
Bilgisayar Mühendisliği
bilgisayar Mühendisliği
bilgisayar mühendisi
bilgisayar Mühendisliği
geliştiricisi
Geliştirici
react
React
angular
Angular
jdbc
Jdbc
Spring
spring
yazilimci
Yazilimci
IT
bilisim
Bilisim
```

If any matches happen eksi-crawler adds the entry to our list

```py
keywords = []

with open('keywords.txt', "r", encoding='utf-8') as f:
    keywords = f.read().split()

def isMatch(entry):
    if any(words in entry for words in keywords):
        return True
    else:
        return False
```

I save the list as 'md' format. You can change it to any other format that you what.

### Final Step

```py
py main.py
```

Do you want to see the result?

[Click](https://github.com/enesusta/eksi-crawler/blob/master/eksi.md)


### License

This code is under the **MIT**

> It's open source. Feel free.