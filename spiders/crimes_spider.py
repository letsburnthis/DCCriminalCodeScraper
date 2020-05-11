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
        for crime in response.xpath('//html/body/main/div/section/section[2]/h1'):
            yield {
                'title': crime.extract()
            }
         
        
        
            #then loops through all links in section2? and passes the link into the parser
        for href in response.xpath('//html/body/main/div/section/section[1]/p/a'):
            
            #checks text associated with link for word "Repealed" and only follows link if word not found
            linkText = str(href.xpath('./text()').extract())
            
            if "Repealed" not in linkText:
                link = str(href.xpath('./@href').extract())
                link = link[2:-2]
                yield scrapy.Request(response.urljoin(link)) 
                

            
            
           
            
            
        


        #next_page_url = response.xpath('//html/body/main/div/section/section[1]/p/a/@href').extract_first()
        #if next_page_url is not None:
        #    yield scrapy.Request(response.urljoin(next_page_url))
        #else:
        #    yield scrapy.Request('https://code.dccouncil.us/dc/council/code/titles/22/')

        
        
        
        #href = response.xpath('//html/body/main/div/section/section[1]/p/a/@href')
        #url =response.urljoin(href.extract_first())
        #yield scrapy.Request(url)
        
        
        
        
        #for href in response.xpath('//html/body/main/div/section/section[1]/p/a/@href'):
        #    print( response.urljoin(href.extract()))
            



        #for crime in response.xpath('//html/body/main/div/section/section[2]/h1'):
        #    yield {
        #        'title': crime.extract()
        #    }
        
        #next_page_url = response.xpath('//html/body/main/div/section/section[1]/p/a/@href').extract_first()
        #if next_page_url is not None:
        #    yield scrapy.Request(response.urljoin(next_page_url))
        


            
            