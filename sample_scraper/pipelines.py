import json
import os
import urllib.request

class SampleScraperPipeline(object):
    def open_spider(self, spider):
        """
        Write the results to a file.
        :param spider: The spider used.
        :return: None
        """
        self.file = open('sample_urls.txt', 'w')

        if spider.auto_download:
            self.download_folder = './downloads/'
            if not os.path.exists(self.download_folder):
                os.makedirs(self.download_folder)
            self.export_file_path_template = './downloads/{}.mp3'

    def close_spider(self, spider):
        """
        Close the file at the end.
        :param spider: The spider used.
        :return: None
        """
        self.file.close()

    def process_item(self, item, spider):
        """
        For every item save its mp3 url to a file.
        :param item: The SampleScraperItem
        :param spider: The spider
        :return: The processed item.
        """
        url = item['preview']['mp3']['url']
        self.file.write(url + os.linesep)

        if spider.auto_download:
            url = url.replace('https', 'http')
            urllib.request.urlretrieve(url, self.export_file_path_template.format(item['id']))

        return item
