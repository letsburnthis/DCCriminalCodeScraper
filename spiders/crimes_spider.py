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
        #basically trying to make it only go one page past the start page   
        
        
            #then loops through all links in section2? and passes the link into the parser
        for href in response.xpath('//html/body/main/div/section/section[1]/p/a/@href'):
            
            yield scrapy.Request(response.urljoin(href.extract()))
            
        


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
        


            
            