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
            #trying to pull out text that includes duration of imprisonment since anything with a max penalty > 1 year is a felony
            
            #each title's paragraphs get their own section. "number" is the number of titles aka sections there will be paragraphs for
            def term(number):
                #each title's paragraphs with sentencing info will be a seperate entry in the list
                prisonLength = []
                #tracks which section collecting info from
                x=1
                 
                while x <= number:
                    #creates path to desired section's paragraphs
                    path = "./section[2]/section["+str(x)+"]/section/p/text()"
                    paragraphs = crime.xpath(path).getall()
                    #will collect all paragraphs with sentence info into one string seperate by "NEW PARAGRAPH"
                    prisonParagraphs = ""
                    #checks for sentence info and makes sure paragraph isn't about amendments aka old info
                    for text in paragraphs:
                        if "prison" in text and "rewrote" not in text:
                            prisonParagraphs = prisonParagraphs + " NEW PARAGRAPH "+text      
                    prisonLength.append(prisonParagraphs)
                    x=x+1
                    
                return prisonLength
                        

            
            #for text in crime.xpath('./section[2]/section/section/p/text()').getall():
            #    if "prison" in text:
            #        prisonLength.append(text)
                    
            #pages with subchapters use h1 for links to another page that contains same info
            if 'Subchapter' in str(crime.xpath('./section[2]/h1').get()):
                

                
                numberTitles = len(crime.xpath('./section[2]/h2/text()').getall())
                    #if "Repealed" not in title:
                    #    listTitles.append(title)
                prisonText = term(numberTitles)
                
                yield {
                    'chapter':crime.xpath('./h1/text()').get(),
                    'titles':crime.xpath('./section[2]/h2/text()').getall(),
                    'texts': prisonText,
                    'address': response.request.url
                    } 
            else:
                #old thing I was using to remove repealed titles from list. decided to leave them 
                # at least short term to make it easier to keep track of which paragraphs 
                # go with which titles. 
                #listTitles = []
                #for title in crime.xpath('./section[2]/h1/text()').getall():
                #    if "Repealed" not in title:
                #        listTitles.append(title) 

                numberTitles = len(crime.xpath('./section[2]/h1/text()').getall())
                prisonText = term(numberTitles)
                yield {
                    'chapter':crime.xpath('./h1/text()').get(),
                    'titles': crime.xpath('./section[2]/h1/text()').getall(),
                    'text': prisonText,
                    'address': response.request.url
                    }

         
        
       
        
        #then loops through all links in section2? and passes the link into the parser
        for a in response.xpath('//html/body/main/div/section/section[1]/p/a'):
            
            #checks text associated with link for word "Repealed" and only follows link if word not found and word "chapter" appears also skips chapters that have no crimes
            linkText = str(a.xpath('./text()').extract())
            avoidList = ['Repealed', '35', '36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52']
            if all(x not in linkText for x in avoidList) and 'Chapter' in linkText:
                yield response.follow(a, callback=self.parse)
                
                
                #what I was using before I found the built in function
                #turns the link from a list into a string and removes the list elements
                #then feeds into the urljoin to scrape the linked page
                #link = str(a.xpath('./@href').extract())
                #link = link[2:-2]
                #yield scrapy.Request(response.urljoin(link)) 
                

            
            
           
            
            
        


       


            
            