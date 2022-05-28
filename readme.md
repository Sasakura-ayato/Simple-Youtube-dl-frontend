# YouTube Downloader Frontend for youtube-dl.py
このツールを使用して、YouTube の動画をダウンロードするときは、動画の著作者ガイドラインや、お住まいの国の法令にしたがってください。

## Installation
```sh
git clone https://github.com/Sasakura-ayato/Simple-Youtube-dl-frontend.git
pip3 install -r requirements.txt
```

ydl_search.py を利用する場合は、YouTube API v3 が必要です。
API キーは、ydl_search.py 内の、

```py
DEVELOPER_KEY = **'{DEVELOPER_KEY}'**
```

に記入してください。

## Usage

```
ydl.py -u {YouTube-URL} -t {audio / video}
ydl_search.py -k {Keyword}
```

ydl.py は URL を直接指定します。`-t` は非必須です（デフォルトは `audio`）
ydl_search.py はキーワードを入力して直接検索しますが、近似 5 件しか出力しません。