# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import os

class CricinfoCrawlerPipeline:
    def open_spider(self, spider):
        if spider.name == 'teams_spider':
            if not (os.path.exists('teams')):
                os.mkdir(os.path.join(os.getcwd(),'teams'))

    def process_item(self, item, spider):
        if spider.name == 'teams_spider':
            teamInfo = ItemAdapter(item)['team']
            fileName = teamInfo['team_name'].lower()+'-'+str(teamInfo['team_id'])+'.csv'
            if not (os.path.exists('teams/'+fileName)):
                self.file = open(os.path.join("teams", fileName), 'w')
        
        return item
    
    def close_spider(self, spider):
        self.file.close()
