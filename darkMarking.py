import sys
from pprint import pprint
from util import *

# get args
search_words, envName, postData = sys.argv[1], sys.argv[2], sys.argv[3]
# Twiter Auth
promoteVideoUrl, postUrl, twBaseStr = getTwData(postData)
api = auth_api(envName)


def main():
    jogaiStatusId = []
    jogaiUserId = []
    rawJsonList = simple_tweet_search_j(search_words, envName)
    postedStatusIds = csvToList('jogaiStatusId.csv')
    postedUserIds = csvToList('jogaiUserId.csv')
    for i in rawJsonList:
        if i['id_str'] not in postedStatusIds and i['user']['id_str'] not in postedUserIds:
            idStr = i['id_str']
            screenName = i['user']['screen_name']
            quoteUrl = f'https://twitter.com/{screenName}/status/{idStr}'
            twStr = twBaseStr + postUrl + " " + quoteUrl
            try:
                uploadVideo(envName, promoteVideoUrl, twStr)
            except Exception as e:
                print(f'{i} is {e}')
            else:
                jogaiStatusId.append(i['id'])
                jogaiUserId.append(i['user']['id'])
    # 投稿済みIDを記録
    listToCsv('jogaiStatusId.csv', jogaiStatusId)
    # 投稿済みスクリーンネームを記録
    listToCsv('jogaiUserId.csv', jogaiUserId)


if __name__ == "__main__":
    main()
