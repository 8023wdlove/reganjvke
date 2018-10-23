#本爬虫仅用于学习，纯属爱好，虽然本爬虫很简单，但还是请大家不要滥用
#python3, Firefox浏览器
 
import requests
from bs4 import BeautifulSoup
import time
import csv
 
# 定制请求头，请求头在浏览器中查看，具体方法见附录一
headers = {
    'User-Agent': 'MMozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
}
 
# 将要访问的网址
link = 'https://qd.zu.anjuke.com/fangyuan/licangqu/fx2-x1/'
# 访问该网站
r = requests.get(link, headers=headers, timeout=100)
 
# 使用BeautifulSoup提取html中的内容
# BeautifulSoup 中文官方文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id37
soup = BeautifulSoup(r.text, 'lxml')
house_list = soup.find_all('div', class_="zu-itemmod")

for house in house_list:
    print(house.find('a',class_="img").get("href"),111)
    print(house.find('a',class_="img").get("title"),222)
    print(house.find('a',class_="img").get("_soj"),333)
    print(house.find('a',class_="img").get("title"),444)

    


 
# 将爬取的内容写入 test.csv中，编码格式为 'UTF-8'
# with open('test.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
#     w = csv.writer(csvfile)
 
#     for house in house_list:
#         temp = []
        
#         name = house.find('div', class_="house-title").a.text.strip()
#         price = house.find('span', class_='price-det').text.strip()
#         price_area = house.find('span', class_='unit-price').text.strip()
#         no_room = house.find('div', class_='details-item').span.text
#         area = house.find('div', class_='details-item').contents[3].text
#         floor = house.find('div', class_='details-item').contents[5].text
#         year = house.find('div', class_='details-item').contents[7].text
#         broker = house.find('span', class_='brokername').text
#         broker = broker[1:]
#         address = house.find('span', class_='comm-address').text.strip()
#         address = address.replace('\xa0\xa0\n                  ', ' ')
#         tag_list = house.find_all('span', class_='item-tags')
#         tags = [i.text for i in tag_list]
#         temp = [name, price, price_area, no_room, area,
#                 floor, year, broker, address, tags]
#         print(temp)
#         # 写入表格（test.csv）
#         w.writerow(temp)