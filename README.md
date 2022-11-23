# スパムマーケティングシステム「ボマー」の使い方
## 準備の前に
- 使うな

## 　準備

- ライブラリのインストール
```bash
pip install tweepy==3.10.0 configparser python-twitter
```

- Twitter認証情報の作成

```bash
# 作成
nano setting.ini
# 例
[demo]
consumer_key = XXXX
consumer_secret = XXXX
access_key = XXX-XXXX
access_secret = XXXX
```

- 投稿データの作成

```bash
# 作成
nano postdata.ini
# 例
[demo]
postVideoUrl = https://video.twimg.com/ext_tw_video/1558670883392065536/pu/vid/854x480/NVI4EkmjnJcmC5oK.mp4
postUrl = https://alkamar.jougennotuki.com/
text = こんにちは！AL-KAMALのキーボード、ボマーです！日本最古の偉大な同人ブラックメタルシューゲイザーAL-KAMALを聴きましょう！ストリーミングとフィジカルはURLからどうぞ！
```

## 実行

```bash
chmod 755 darkMarking.sh
sh darkMarking.sh '"\ブラックメタル\"' demo demo
```

![](README.png)

## マーケティング活動の例

```bash
crontab -e
# 追加する
*/10 * * * * cd /home/ubuntu/boma_bomm; /home/ubuntu/boma_bomm/darkMarking.sh '"\ブラックメタル\"' demo demo > /dev/null 2>&1
```

## おまけ
- 特定フォロワーのフォロー・フォロワー全員に引用RTする
  - 邪悪なので使わないように

```bash
python followreQt.py "ターゲットのscreen_name" "setting.iniの環境名" "postdata.iniの環境名"
```

- `nohup python3 followreQt.py "ターゲットのscreen_name" "setting.iniの環境名" "postdata.iniの環境名" >> log 2>&1 &`でログアウトしても安心