from urllib.parse import urlparse
import urllib
import ssl
import traceback
from django.http import HttpResponse
import json
from bs4 import BeautifulSoup
import requests
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    request_body = json.loads(request.body)

    sex = request_body['action']['params']['sex']
    age = request_body['action']['params']['age']
    symptom = request_body['action']['params']['symptom']

    rcms = []

    #sex="여자"
    #age="성인"
    #symptom="탈모"

    # age 숫자로 변환
    if age == "성인":
        age = 14866
    elif age == "어린이":
        age = 15084
    elif age == "노인":
        age = 14867
    elif age == "십대":
        age = 17303
    else:
        age = 15083

    url = 'https://kr.iherb.com/search'
    values = {
        'kw': symptom,
        'avids': age
    }
    header = {
        'User-Agent': 'Mozilla/5.0',
    }

    query_string = urllib.parse.urlencode(values)
    #req = urllib.request.Request(url + '?' + query_string, headers=header)
    #context = ssl._create_unverified_context()

    req = requests.get(url+'?'+query_string)

    html=req.text

    html_data = BeautifulSoup(html, 'html.parser')



    list_item = html_data.find_all('div', attrs={"class": "product-title"})
    list_image = html_data.select('span[class = product-image]')
    list_price = html_data.find_all("span", attrs={"class": "price"})

    # size = len(list_item)

    cnt_item = 0
    for i in list_item:
        # 최대 3개 까지만
        if cnt_item < 3:
            # title
            title = list_item[cnt_item].get_text().rstrip('\n')

            # link
            link = html_data.find("a", attrs={"class": "stars"})

            # id
            specific_id = query_string

            # image url
            image = list_image[cnt_item].find("img", attrs={"itemprop": "image"})
            image = image.attrs['src']

            # price
            price = list_price[cnt_item].get_text()

            item_obj = {
                'title': title,
                'link': link.attrs['href'],
                'symptom': str(age) + sex + symptom,
                'specific_id': specific_id,
                'image': image,
                'price': price,
            }

            rcms.append(item_obj)
            cnt_item = cnt_item + 1

    size = len(rcms)

    if size == 0:
        result = {
            "version": "2.0",
            "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "간단한 텍스트 요소입니다."
                    }
                }
            ]
        }
}



    else:
        Items = []
        for it in rcms:
            item = {
                "title": it['title'],
                "description": it['price'],
                "thumbnail": {
                    "imageUrl": it['image']
                },
                "buttons": [
                    {
                        "action":"webLink",
                        "label":"구경가기",
                        "webLinkUrl": it['link']
                    }
                ]
            }

            Items.append(item)


        result = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": Items
                        }
                    }
                ]
            }
        }

    return HttpResponse(json.dumps(result), content_type=u"text/json-comment-filtered; charset=utf-8")
