#coding:utf-8
#尝试爬取花瓣网上图片
import urllib2,re,urllib,os

class HuaBan:
    def __init__(self):
        self.url = 'http://huaban.com/boards/'
        self.index = 'http://huaban.com/jppil/'
        self.files = 'huaban/'

    def getPage(self,url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        page = response.read()
        return page

    def getPanel(self):
        page = self.getPage(self.index)
        pattern = re.compile('<div data-id="(.*?)"')
        panel = re.findall(pattern,page)
        return panel

    def getImgs(self,url):
        content = self.getPage(url)
        pattern = re.compile('<div data-id=.*?<img src="//(.*?)_fw236"',re.S)
        imgs = re.findall(pattern,content)
        return imgs

    def saveImgs(self,imgs,files):
        num = 1
        for i in imgs:
            file = files + '/' + str(num) + '.jpg'
            im = u'http://'+i
            img = urllib.urlopen(im)
            data = img.read()
            with open(file,'wb')as f:
                f.write(data)
            num += 1

    def getDirName(self):
        page = self.getPage(self.index)
        pattern = re.compile('<div data-id.*?<div class="over ".*?<h3>(.*?)</h3>')
        dirs = re.findall(pattern,page)
        return dirs

    def mkDir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False

    def solveProblem(self):
        panels = self.getPanel()
        num = 0
        dirs = self.getDirName()
        for i in panels:
            url = self.url + str(i)
            imgs = self.getImgs(url)
            self.mkDir(dirs[num])
            self.saveImgs(imgs,dirs[num])
            num+=1

if __name__ == '__main__':
    hb = HuaBan()
    hb.solveProblem()
