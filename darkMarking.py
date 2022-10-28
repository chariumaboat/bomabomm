import sys
from pprint import pprint
from util import *

# get args
search_words, envName = sys.argv[1], sys.argv[2]
# Twiter Auth
promoteVideoUrl = 'https://video.twimg.com/ext_tw_video/1558670883392065536/pu/vid/854x480/NVI4EkmjnJcmC5oK.mp4'
api = auth_api(envName)


def main():
    tmpArt = "AL-KAMAL"
    postUrl = "https://alkamar.jougennotuki.com/"
    jogaiStatusId = []
    jogaiUserId = []
    twBaseStr = f'こんにちは！{tmpArt}のキーボード、ボマーです！\n日本最古の偉大なポストブラック{tmpArt}を聴きましょう！\nストリーミングとフィジカルはURLからどうぞ！ {postUrl}'
    rawJsonList = simple_tweet_search_j(search_words, envName)
    postedStatusIds = csvToList('jogaiStatusId.csv')
    postedUserIds = csvToList('jogaiUserId.csv')
    for i in rawJsonList:
        if i['id_str'] not in postedStatusIds and i['user']['id_str'] not in postedUserIds:
            idStr = i['id_str']
            screenName = i['user']['screen_name']
            quoteUrl = f'https://twitter.com/{screenName}/status/{idStr}'
            twStr = twBaseStr + " " + quoteUrl
            print(quoteUrl)
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
