import scrapy


class MangoSpider(scrapy.Spider):
    name = 'mango'

    def start_requests(self):
        url = 'https://shop.mango.com/services/garments/1704202008'
        headers = {"stock-id": "068.IN.0.true.false.v0"}
        req = scrapy.http.JsonRequest(url, headers=headers)
        yield req

    def parse(self, response):
        response = response.json()
        size_data = response["colors"]["colors"][0]["dataLayer"]

        yield {
            "name": response["name"],
            "price": response["price"]["price"],
            "color": response["colors"]["colors"][1]['label'],
            "size": size_data["sizeAvailability"].split(",") + size_data["sizeNoAvailability"].split(",")
        }
    
