# -*- coding: utf-8 -*-
import scrapy
#to run type 'scrapy crawl crimes -o crimes.json'
#need to mess with to figure out correct formatting of code/xpath
class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'crimes'
    start_urls = [
        'https://code.dccouncil.us/dc/council/code/titles/22/',
    ]

    def parse(self, response):
        #parser loops through instances of h1 in section3? and yields them
        for crime in response.xpath('//html/body/main/div/section'):
            #/section[2]/h1 what I removed from originial xpath
            yield {
                'chapter':crime.xpath('./h1/text()').get(),
                'title': crime.xpath('./section[2]/h1').getall(),
                'address': response.request.url
            }
         
        
        
            #then loops through all links in section2? and passes the link into the parser
        for a in response.xpath('//html/body/main/div/section/section[1]/p/a'):
            
            #checks text associated with link for word "Repealed" and only follows link if word not found
            linkText = str(a.xpath('./text()').extract())
            avoidList = ['Repealed', '35', '36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52']
            if all(x not in linkText for x in avoidList):
                yield response.follow(a, callback=self.parse)
                
                
                #what I was using before I found the built in function
                #turns the link from a list into a string and removes the list elements
                #then feeds into the urljoin to scrape the linked page
                '''link = str(a.xpath('./@href').extract())
                link = link[2:-2]
                yield scrapy.Request(response.urljoin(link)) '''
                

            
            
           
            
            
        


       


            
            