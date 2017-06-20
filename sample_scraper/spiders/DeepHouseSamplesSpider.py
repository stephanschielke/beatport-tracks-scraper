import os
import json
import scrapy

from ..items import SampleScraperItem

class DeepHouseSamplesSpider(scrapy.Spider):
    """
    Sample MP3 URL Spider for DeepHouse tracks on Beatport.com
    Start the script with:
        scrapy crawl deephouse
    or
        scrapy crawl deephouse -o tracks.json
    for full information.

    Then use:
        wget -e robots=off --input-file=sample_urls.json
    """
    name = "deephouse"

    auto_download = False

    # Results per page
    per_page = 150
    # Sort by newest releases first
    sort = 'release-desc'
    # Only deep house tracks
    genres = '12'  # deep house

    # https://www.beatport.com/tracks/all?per-page=150&sort=release-desc&genres=12
    base_url_template = "https://www.beatport.com/tracks/all?per-page={per_page}&sort={sort}&genres={genres}&page={page}"
    base_url_template = base_url_template.format(per_page=per_page, sort=sort, genres=genres, page='{page}')

    # Last page to visit
    last_page = 1

    def start_requests(self):
        """
        Triggered once on start of scraping.
        :return: A page request generator.
        """
        for num in range(1, self.last_page + 1):
            url = self.base_url_template.format(page=num)
            request = scrapy.Request(url=url, callback=self.parse)
            yield request

    def parse(self, response):
        """
        Parses a single result page for track information.
        :param response: The request response object.
        :return: A generator for Track samples
        """

        # Extract the data-object element, containing all the information we need
        # Conveniently nearly pure json
        data_objects = response.xpath('//*[@id="data-objects"]/text()').extract_first()

        # Remove javascript variable name
        data_objects = data_objects.replace('window.Playables = ', '')

        # Remove the first 2 lines and the last 7
        data_objects_lines = data_objects.splitlines()
        data_objects_json_text = os.linesep.join(str(x) for x in data_objects_lines[2:len(data_objects_lines) - 7])

        # remove ';' at the very end
        data_objects_json_text = data_objects_json_text[:-1]

        # Get the track information
        data_objects_json = json.loads(data_objects_json_text)
        tracks = data_objects_json['tracks']

        # print(tracks)
        # For every track in the list create a sample item
        for track in tracks:
            # Store ALL the information, because why not
            yield SampleScraperItem(active=track['active'],
                                    artists=track['artists'],
                                    audio_format=track['audio_format'],
                                    bpm=track['bpm'],
                                    component=track['component'],
                                    component_type=track['component_type'],
                                    date=track['date'],
                                    duration=track['duration'],
                                    exclusive=track['exclusive'],
                                    formats=track['formats'],
                                    genres=track['genres'],
                                    guest_pick=track['guest_pick'],
                                    id=track['id'],
                                    images=track['images'],
                                    key=track['key'],
                                    label=track['label'],
                                    mix=track['mix'],
                                    name=track['name'],
                                    preorder=track['preorder'],
                                    preview=track['preview'],
                                    price=track['price'],
                                    purchase=track['purchase'],
                                    purchase_type=track['purchase_type'],
                                    release=track['release'],
                                    remixers=track['remixers'],
                                    sale_type=track['sale_type'],
                                    slug=track['slug'],
                                    sponsored=track['sponsored'],
                                    sub_genres=track['sub_genres'],
                                    title=track['title'],
                                    type=track['type'],
                                    waveform=track['waveform'], )
