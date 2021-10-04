import requests
import random
import time

post_id = 236159027

comments_url = "https://www.dcard.tw/service/api/v2/posts/"+ str(post_id)+ "/comments?limit=100&after=0"
comments_request = requests.get(comments_url)
if (comments_request.status_code != 200):
    print("error")
comments_request = comments_request.json()


f = open("test.txt", 'a+', encoding="utf-8")

count = 0
after = 0


while(1):
    print(after)
    print(len(comments_request))
    print(comments_request[5]['content'])
    if (len(comments_request) == 100):
        for i in range(len(comments_request)):
            print(comments_request[i]['floor'])
            if (comments_request[i]['hiddenByAuthor'] == False  and len(comments_request[i]['reportReason']) == 0):
                print(comments_request[i]['content'] + '\n')
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
            print(comments_request[i]['floor'])
            count = count + 1
            if (comments_request[i]['hiddenByAuthor'] == False  and len(comments_request[i]['reportReason']) == 0):
                f.write(comments_request[i]['content'] + '\n')
        break


print(count)
        
    

f.close()