import scrapy


class CoinSpider(scrapy.Spider):
    name = "coins"
    start_urls = [
        'https://coinmarketcap.com/1',
    ]

    def parse(self, response):
        page = response.url.rpartition('/')[2]
        if not page:
            next_page = 2
        else:
            next_page = int(page) + 1
        hasNext = False
        for coin in response.css('table#currencies tbody tr'):
            hasNext = True
            url = 'https://s2.coinmarketcap.com/static/img/coins/16x16/%s.png'
            srcUrl = coin.css('td.currency-name img.logo-sprite::attr("data-src")').extract_first()
            if not srcUrl:
                tid = coin.css('td.dropdown::attr("data-cc-id")').extract_first()
                srcUrl = url % tid
            yield {
                'imgSrc': srcUrl,
                'name': coin.css('td.percent-change::attr("data-symbol")').extract_first()
            }

        next_page = 'https://coinmarketcap.com/%s' % (next_page)
        if hasNext:
            yield response.follow(next_page, self.parse)