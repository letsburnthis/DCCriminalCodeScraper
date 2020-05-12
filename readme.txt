scrapy that pulls info from the D.C. Criminal Code at https://code.dccouncil.us/dc/council/code/titles/22/
code is heavily commented to explain what is going mainly because I know I'll forget what it does and how it works.

to run and output a json with a list of dictionaries
'scrapy crawl crimes -o crimes.json'

file for spider is in 

spiders
    crimes_spider.py


Only follows links from that page that do not have "Repealed" in their associated text.

Outputs a list of dictionaries.

Each dictionary is a different chapter aka broad crime.

The dictionary entries are 
chapter : the chapter title
titles : list of the different headings on the webpage, these are usually the specific crimes included in the broad crime.
text : list of any <p></p> of text that includes sentencing information, each item in the list is associated with a different heading aka crime.
address : web URL that the info in the dictionary was pulled from.


The text in each dictionary should in theory line up with each title in the page.
ie.

search['titles'][2] "should" give the title (heading) that the sentencing info from search['text'][2] corrisponds with.

There are many headings on these pages that have no sentencing info. In that case, the text list contains an empty string.
There are some headings that have multiple <p></p> with sentencing info so each new <p></p> starts with "NEW PARAGRAPH" just to be able to identify when that is occuring.
