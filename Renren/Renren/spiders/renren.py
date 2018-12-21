# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com']

    # 重写spider类的start_requests()方法,去掉start_urls     
    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        # FormRequest()方法
        yield scrapy.FormRequest(
            url = url,
            formdata = {"email":"13603263409","password":"zhanshen001"},
            callback = self.parseHtml,
            )

    def parseHtml(self,response):
        with open("zhanshen.html","w") as f:
            f.write(response.text)








    def parse(self, response):
        pass
