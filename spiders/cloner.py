import scrapy
import requests
import os

class QuotesSpider(scrapy.Spider):
        name = "cloner"
        start_urls = [
                'https://adityayadav800.github.io/JHU-HCJ-Assignments/Assignment3-solution/index.html'
                        ]
        def parse(self, response):
            print(response.url)
            temp=response.url
            temp1=temp.split('/')
            print(temp1)
            mainFolder=temp1[2]
            print(mainFolder)
            if(not os.path.isdir(mainFolder)):
                os.makedirs(mainFolder)    
            os.chdir(mainFolder)
            imagesLinks=response.xpath('//img/@src').extract()
            ijsLinks=response.xpath('//script[@type=\'text/javascript\']/text()').extract()
            ejsLinks=response.xpath('//script/@src').extract()
            for url in ejsLinks:
                if(not ('https' in url)):
                    it=[]
                    for i in range(len(temp1)-1):
                        it.append(temp1[i])
                    print(it,"+++++++++++++++++++++++++")
                    imdt='/'.join(it)
                    url=imdt+'/'+url
                    print(url,"+++++++++")

                res=requests.get(url)
                x=url.split('/',3)
                y=x[3].split('/')
                print(y)
                s=''
                for i in range(len(y)-1):
                    #print(y[i])
                    if(i==0):
                        s=s+y[i]
                    else:
                        s=s+'/'+y[i]
                print(s)
                if(not os.path.isdir(s)):
                    os.makedirs(s)
                open(x[3],'wb').write(res.content)
            ecss=response.xpath('//link[@rel=\'stylesheet\' or  @type=\'text/css\']/@href').extract()
            print(ecss)
            for url in ecss:
                print(url)
                if(not ('https' in url)):
                    it=[]
                    for i in range(len(temp1)-1):
                        it.append(temp1[i])
                    print(it,"+++++++++++++++++++++++++")
                    imdt='/'.join(it)
                    url=imdt+'/'+url
                    print(url,"+++++++++")
                res=requests.get(url)
                x=url.split('/',3)
                y=x[3].split('/')
                print(y)
                s=''
                for i in range(len(y)-1):
                    #print(y[i])
                    if(i==0):
                        s=s+y[i]
                    else:
                        s=s+'/'+y[i]
                print(s)
                if(not os.path.isdir(s)):
                    os.makedirs(s)
                open(x[3],'wb').write(res.content)
            icss=response.xpath('//style[@type=\'text/css\']/text()').extract()
            ind=open('index.html','w')
            ind.write(response.text)



