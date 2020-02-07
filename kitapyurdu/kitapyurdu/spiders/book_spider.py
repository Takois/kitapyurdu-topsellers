import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    page_count = 0
    book_count = 1
    file = open("books.txt","w",encoding = "UTF-8")
    start_urls = [
        "https://www.merlininkazani.com/oyun/incelemeler?sayfa=1"
    ]

    def parse(self, response):
        game_names = response.css("div.news-list div.caption span.title::text").extract()
        game_dates = response.css("div.news-list div.caption span.date::text").extract
        game_points = response.css("div.preview-point::text").extract()


        i = 0
        while (i < len(book_names)):
            """yield {
                "name" : book_names[i],
                "author" : book_authors[i],
                "publisher" : book_publishers[i]
            }"""
            self.file.write("Oyun İsmi : " + game_names[i] + "\n")
            self.file.write("Tarihi : " + game_dates[i] + "\n")
            self.file.write("Puanı : " + game_points[i] + "\n")
            self.file.write("-----------------------------------------------\n")
            self.book_count += 1
            
            i += 1
        next_url = response.css("div.page-number ul li a.Sonraki Sayfa::attr(href)").extract_first()
        self.page_count += 1

        if next_url is not None and self.page_count != 148:
            yield scrapy.Request(url = next_url,callback = self.parse)
        else:
            self.file.close()