# CoC Title Bot

クトゥルフ神話 TRPG（CoC）のセッション情報を Discord スラッシュコマンドで投稿する Bot です。

## 機能

- `/coct` スラッシュコマンドでセッション情報を整形して投稿

## 出力フォーマット

```
【{接頭辞}】{title}【{gm}卓{count}】
{url}
```

- 版数 7 の場合：接頭辞は「新 CoC シナリオ」
- 版数 6 の場合：接頭辞は「CoC シナリオ」

## 使い方

### 1. 依存ライブラリをインストール

```bash
pip install discord.py
```

### 2. Bot トークンを設定

`bot.py` の `TOKEN` 変数に、Discord Developer Portal で取得した Bot トークンを貼り付けてください。

### 3. Bot を起動

```bash
python bot.py
```

### 4. コマンドの使用

Discord で `/coct` と入力してコマンドを実行します。

#### 引数

| 引数 | 説明 |
|------|------|
| `version` | CoC の版数（6 または 7） |
| `gm` | GM の名前 |
| `count` | 卓の回数 |
| `title` | シナリオタイトル |
| `url` | ココフォリア等の部屋 URL |

#### 例

```
/coct version=7 gm=山田 count=1 title=深淵の呼び声 url=https://cofolia.com/room/12345
```

出力：

```
【新 CoC シナリオ】深淵の呼び声【山田卓 1】
https://cofolia.com/room/12345
```

## 設定

- `bot.py` の `TOKEN` 変数を変更して Bot トークンを設定
- `discord.py` のバージョンを最新に保つことを推奨

## 注意事項

- Bot トークンは機密情報なので、公開しないでください
- Discord サーバーに Bot を追加するには、Discord Developer Portal から Bot を招待する必要があります
