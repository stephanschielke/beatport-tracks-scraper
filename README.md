# beatport-tracks-scraper
Sample MP3 URL Spider for DeepHouse tracks on Beatport.com

# Installation
To use it install python3 on your system.

Then `pip install scrapy`

# Configuration
Edit the entries within
`sample_scraper/spiders/DeepHouseSamplesSpider`

# Start the scraper
Start the script with 
    `scrapy crawl deephouse`
or
    `scrapy crawl deephouse -o tracks.json`
for full information.

# Download mp3s
`wget -e robots=off --input-file=sample_urls.json`
 
