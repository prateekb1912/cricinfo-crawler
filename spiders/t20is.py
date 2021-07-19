"""
    The first spider in this project which will be used to scrape and store
    all the T20I match results
"""
import scrapy

class T20ISpider(scrapy.Spider):
    name = "t20i"

    def start_requests(self):
        urls = []

        # URLS for all T20I results from 2005 to 2020 
        for year in range(2005, 2021):
            urls.append("https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=${year};type=year")
        
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
    
    def parse(self, response):
        """
            The data is stored in a table with each result in a different row
        """
        table = response.xpath("//table")[0]
        data_rows = table.xpath("//tr[@class='data1']")
