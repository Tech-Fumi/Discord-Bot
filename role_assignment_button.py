
import discord
import requests
from discord.ext import commands
from pprint import pprint
import aiohttp

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


# .envファイルから環境変数をロード
load_dotenv()

# 環境変数から値を取得 
TOKEN = os.getenv("TOKEN") 
channelId= os.getenv("channelId")


AuthB = "Bot " + TOKEN
headers = {
    "Authorization": AuthB
}
def returnNormalUrl(channelId):
    return "https://discordapp.com/api/channels/" + str(channelId) + "/messages"
async def notify_callback(id, token):
    url = "https://discord.com/api/v8/interactions/{0}/{1}/callback".format(id, token)
    json = {
        "type": 6
    }
    async with aiohttp.ClientSession() as s:
        async with s.post(url, json=json) as r:
            if 200 <= r.status < 300:
                return
class MyBot(commands.Bot):
    def __init__(self, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True  # メッセージの内容を取得する権限を追加
        intents.members = True  # メンバーのリストを取得する権限を追加
        super().__init__(**kwargs, intents=intents)
bot = MyBot(command_prefix='$', description='discord bot')
# チャンネルIDとロールIDのマッピング
role_id_map = {
    1194355292096430203: 1194432140637642773,
    1194426512015888415: 1194430240689233982,
    # 他のチャンネルIDとロールIDのペアをここに追加
}
@bot.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component:
        custom_id = interaction.data.get('custom_id')
        if custom_id == "click_one":
            # チャンネルIDに基づいてロールIDを取得
            your_role_id = role_id_map.get(interaction.channel.id)
            if your_role_id is None:
                await interaction.response.send_message("このチャンネルに対応するロールが設定されていません。", ephemeral=True)
                return
            role = discord.utils.get(interaction.guild.roles, id=your_role_id)
            if role:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"{role.name} ロールを付与しました！", ephemeral=True)
            else:
                await interaction.response.send_message("ロールが見つかりません。", ephemeral=True)
@bot.event
async def on_ready():
    channel = bot.get_channel(channelId)  
    if channel:
        normal_url = returnNormalUrl(channel.id)
        json = {
            "content": "スクリム参加希望者は、以下のボタンをクリックして参加し、Yunite認証というチャンネルから認証を行って登録を完了してください。",
            "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "label": "スクリムに参加",
                            "style": 1,
                            "custom_id": "click_one",
                        },
                    ]
                }
            ]
        }
        r = requests.post(normal_url, headers=headers, json=json)
bot.run(TOKEN)
