rm coins.json
scrapy runspider coin_spider.py -o coins.json
python parser.py > down-16.sh
python parser32.py > down-32.sh

bash down-16.sh
mkdir small-icons
mv *.png small-icons/

bash down-32.sh
mkdir big-icons
mv *.png big-icons/
