import scrapy
import re

class BoleListSpider(scrapy.Spider):
    name = "list_spider"
    start_urls = ["http://blog.jobbole.com/all-posts/"]
    total_count = 0

    def parse(self, response):
        result = dict()
        print("++++++"*50)
        container = response.xpath("//div[@class='post floated-thumb']")
        curr_page = int(response.xpath("//span[@class='page-numbers current']/text()").extract_first())
        # print(type(container))
        list_index = 1
        for item in container:
            # print(item)
            result["thumb_url"] = item.xpath("./div[@class='post-thumb']//img/@src").extract_first()
            content_container = item.xpath(".//div[@class='post-meta']")
            result["date"] = ""
            date_b = content_container.xpath("./p/text()").extract()
            match = re.findall("(\d{4}/\d{2}/\d{2})", str(date_b))
            if len(match):
                result["date"] = match[0]
            result["title"] = content_container.xpath("./p/a[@class='archive-title']/text()").extract_first()
            result["tag"] = content_container.xpath("./p/a[@rel]/text()").extract_first()
            result["summary"] = content_container.xpath("./span[@class='excerpt']/p/text()").extract_first()
            result["detail_url"] = content_container.xpath(".//span[@class='read-more']/a/@href").extract_first()
            result["curr_index"] = (curr_page-1) * 20 + list_index
            yield result
            list_index += 1
        next_page = response.xpath("//a[@class='next page-numbers']/@href").extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

