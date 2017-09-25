# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import sys

class Antonym():
    def __init__(self):
        pass

    def get(self, word):
        return self._en(word) if word.encode("utf-8").isalnum() else self._jp(word)

    def _jp(self, word):
        antnm = ""
        soup = self._open_soup("http://thesaurus.weblio.jp/antonym/content/" + urllib.parse.quote(word))
        try:
            antnm = soup.find(id = 'main').find(class_ = 'wtghtAntnm').a.string
        except AttributeError:
            print("cannot find the antonym.")
        except Exception as e:
            print(e)
        return antnm

    def _en(self, word):
        antnmlist = []
        try:
            soup = self._open_soup("http://www.thesaurus.com/browse/" + word + "?s=t")
            for ul in soup.find(class_ = 'container-info antonyms').findAll("ul"):
                for li in ul.findAll('li'):
                    antnmlist.append(li.a.string)
        except urllib.error.HTTPError:
            print("cannot find the antonym.")
        except Exception as e:
            print(e)
        return antnmlist

    def _open_soup(self, url):
        with urllib.request.urlopen(url) as response:
            return BeautifulSoup(response, "html.parser")


if __name__ == '__main__':
    word = u'嘘'
    if len(sys.argv) > 1:
        word = sys.argv[1]

    print(Antonym().get(word))
