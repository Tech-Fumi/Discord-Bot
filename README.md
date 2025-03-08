# Discord Role Assignment Bot

このプロジェクトは、Discord サーバーでメンバーが特定の条件（招待リンクまたはボタン）に基づいてロールを自動的に割り当てるボットです。

## 機能

### 1. `invite_url_role.py`
- メンバーが特定の招待リンクから参加すると、自動的に対応するロールを付与します。
- `role_id_map` に招待リンクとロール ID のペアを登録できます。

### 2. `role_assignment_button.py`
- Discord のボタンをクリックすることで、特定のチャンネルごとにロールを割り当てる機能を提供します。
- `role_id_map` にチャンネル ID とロール ID のペアを登録できます。
- ボタンをクリックすると、対応するロールが付与されます。
- `on_ready` イベント時にボタン付きのメッセージを送信します。

## 環境変数
`.env` ファイルを使用して以下の値を設定してください。

```
TOKEN=your_discord_bot_token
channelId=your_target_channel_id  # (role_assignment_button.py で使用)
```

## インストール & 実行方法
1. 必要なパッケージをインストール

```
pip install -r requirements.txt
```

2. `.env` ファイルを作成し、TOKEN などを設定

3. ボットを実行

```
python invite_url_role.py
python role_assignment_button.py
```

## 設定方法
### 招待リンクによるロール付与
- `invite_url_role.py` の `role_id_map` に、招待リンクとロール ID を追加。

### ボタンによるロール付与
- `role_assignment_button.py` の `role_id_map` に、チャンネル ID とロール ID を追加。
- `channelId` を `.env` に設定。

## 注意事項
- Discord の Bot に適切な権限を付与してください。
- `intents.members = True` を設定することで、メンバー管理が可能になります。
- `.env` の `TOKEN` は安全に管理してください。

## ライセンス
MIT License

