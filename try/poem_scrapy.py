import scrapy

class PoemsSpider(scrapy.Spider):
	name='peoms'
    allowed_domains=['diwany.org']
    start_urls=['http://diwany.org/']
    
    def parse(self,response):
        bahrs_links=response.xpath("//div[@class='menu-behers-ar-container']//a")
        for link in bahrs_links:
            yield response.follow(link,callback=self.parse_bahr,cb_kwargs=dict(poems_links=list()))
    
    def parse_bahr(self,respone,poems_links):
        print('the initial number of poems links for the url:',response.url,'is',len(poems_links))
        poems_links+=respone.xpath("//div[@class='post hentry ivycat-post']/h2//a")
        next_page=response.css(".pip-nav-next a")
        if next_page:
            yield response.follow(
                next_page[0],
                callback=self.parse_bahr,
                cb_kwargs=dict(poems_links=poems_links),
                )
        else:
            yield from respone.follow_all(
                poems_links,callback=self.parse_poem,)
     
    def parse_poem(self,response):
        return None
    
    def parse_hard(self,response):
        return "I try my best to win the game"
       
              