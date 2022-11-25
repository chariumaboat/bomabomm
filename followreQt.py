import tweepy
import sys
from pprint import pprint
from util import *
import time
import random

# 各種データ引数から受け取り
targetScreenName, envName, postData = sys.argv[1], sys.argv[2], sys.argv[3]
# プロモーションデータ取得
promoteVideoUrl, postUrl, twBaseStr = getTwData(postData)
# 認証
api = auth_api(envName)


def main():
    f_list = getFollow_ids(api, targetScreenName)
    print(len(f_list))
    for i in f_list:
        usr = api.get_user(i)
        try:
            scName = usr.screen_name
            id_str = usr.status.id_str
            quoteUrl = f'https://twitter.com/{scName}/status/{id_str}'
            print(quoteUrl)
        except Exception as e:
            print(e)
        else:
            twStr = twBaseStr + postUrl + " " + quoteUrl
            try:
                uploadVideo(envName, promoteVideoUrl, twStr)
                time.sleep(random.uniform(60, 600))
            except Exception as e:
                print(e)


if __name__ == "__main__":
    main()
