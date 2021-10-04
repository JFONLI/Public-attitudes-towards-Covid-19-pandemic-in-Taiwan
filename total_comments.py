import requests
from bs4 import BeautifulSoup
import datetime as dt
import jieba
from wordcloud import WordCloud
import cloudscraper
import matplotlib.pyplot as plt
import time
import random

import json

#---------Start----------#

#--------Initial---------#
#stop_time 爬到幾號
stop_time = dt.datetime(2020, 12, 31, 23, 59, 59)
#fourm 爬哪個論壇
fourm = "2019_ncov"

#--------抓最新----------#
api = "https://www.dcard.tw/_api/forums/"+fourm+"/posts?popular=false"

r = requests.get(api)
print(r)
r = r.json()

messages = list()
ids = list()
times = list()

#last_id 這邊是自動搜索最新一篇
last_id = r[0]['id']
last_time = r[0]['createdAt']
last_time = last_time.split(".")
last_time = dt.datetime.strptime(last_time[0], '%Y-%m-%dT%H:%M:%S')


#last_id 可手動設置從哪一篇開始爬
# last_id = 236081691
# last_time = dt.datetime(2021 ,4,7,23,57,0)

def sum_comments(total_comments):
    comments_url = "https://www.dcard.tw/service/api/v2/posts/"+ str(post_id)+ "/comments?limit=100&after=0"
    comments_request = requests.get(comments_url)
    if (comments_request.status_code != 200):
        print("error")
    comments_request = comments_request.json()

    count = 0
    after = 0

    while(1):
        if (len(comments_request) == 100):
            for i in range(len(comments_request)):
                # print(comments_request[i]['floor'])
                if (comments_request[i]['hiddenByAuthor'] == False  and len(comments_request[i]['reportReason']) == 0):
                    # print(comments_request[i]['content'] + '\n')
                    f.write(comments_request[i]['content'] + '\n')
                    
            after += 1


            comments_url = "https://www.dcard.tw/service/api/v2/posts/"+ str(post_id)+ "/comments?limit=100&after=" + str(after * 100)
            time.sleep(random.randint(3,5))
            comments_request = requests.get(comments_url)
            if (comments_request.status_code != 200):
                print("error")
            comments_request = comments_request.json()

        


        else:
            for i in range(len(comments_request)):
                # print(comments_request[i]['floor'])
                count = count + 1
                if (comments_request[i]['hiddenByAuthor'] == False  and len(comments_request[i]['reportReason']) == 0):
                    f.write(comments_request[i]['content'] + '\n')
            break


#--------------Start crawl---------------#

total_comments = dict()

while (1):
    time.sleep(random.randint(3,5))
    url = "https://www.dcard.tw/_api/forums/"+fourm+"/posts?popular=false&limit=100&before=" + str(last_id)
    request = requests.get(url)
    if (request.status_code != 200):
        break
    request = request.json()
    
    for i in range(len(request)):
        post_id = request[i]['id']
        post_title = request[i]['title']
        post_time = request[i]['createdAt']
        comment_count = request[i]['commentCount']
        post_time = post_time.split(".")
        post_time = dt.datetime.strptime(post_time[0], '%Y-%m-%dT%H:%M:%S')

        dict_key = str(post_time.year) + "_" + str(post_time.month) + "_" + str(post_time.day)

        print(post_title)
        print(post_id)
        print(post_time)
        print(comment_count)
        
        if total_comments.__contains__(dict_key):
            total_comments[dict_key] = total_comments[dict_key] + comment_count
        else:
            total_comments.setdefault(dict_key, comment_count)

        jsObj = json.dumps(total_comments)
        fileObject = open(fourm + "_comments.json", 'w')
        fileObject.write(jsObj)
        fileObject.close

        if (post_time < stop_time):
            break
    
    if (post_time < stop_time):
        break

    last_id = post_id

    

# # f = open('test.txt', 'w', encoding="utf-8")
# # for i in range(len(messages)):
# #     f.write(messages + '\n')
# # f.close()

# f = open('trending_ids.txt', 'a+', encoding="utf-8")
# for item in ids:
#     f.write(str(item) + '\n')
# f.close()

# f = open('trending_times.txt', 'a+', encoding="utf-8")
# for item in times:
#     f.write(str(item) + '\n')
# f.close() 




# # 下面跑不動 把test.txt裡文字複製到 徐的code就能跑

# with open("test.txt", encoding="utf-8", errors='ignore') as f:
#     text = f.read()

# with open("stopwords.txt", encoding="utf-8", errors='ignore') as f2:
#     stopwords = f2.read().split('\n')

# jieba.set_dictionary('dict.txt.big')
# wordList = jieba.lcut(text)


# final_wordList = list()

# for word in wordList:
#     if len(word) > 1 and word not in stopwords:
#         final_wordList.append(word)

# words = " ".join(final_wordList)

# myWordCloud = WordCloud(background_color="white", font_path="simsun.ttf").generate(words)

# plt.imshow(myWordCloud)
# plt.axis("off")
# plt.show()

# myWordCloud.to_file('word_cloud.png')