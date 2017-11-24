# -*- coding: utf-8 -*-
import scrapy
#导入模块
from dangdang.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4008150.html']
                    #所有的信息都在网页的相应response中
    ####parse回调函数
    def parse(self, response):
        #pass
        #实例化这个项目
        item = DangdangItem()
        #已经爬取了首页，所有的信息都存储在response中，提取信息需要调用xpath去匹配，extract()解压缩
        item["title"] = response.xpath("//a[@name='itemlist-title']/@title").extract()
        #关键点在与xpath表达式怎么写  取所有的a标签//定位使用@name='itemlist-title'
        item["link"] = response.xpath("//a[@name='itemlist-title']/@href").extract()
        item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        #print(item["link"])
        yield item
        #将数据提交到pipelines中，提交item这个数据
        #爬取首页后进入for循环，从第二页开始爬取
        for i in range(2,50):
            url= "http://category.dangdang.com/pg%d-cid4008150.html" %(i)
            yield Request(url,callback=self.parse)  #依次去返回
