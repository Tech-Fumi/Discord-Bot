
import discord
from discord.ext import commands


import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


# .envファイルから環境変数をロード
load_dotenv()

TOKEN = os.getenv("TOKEN") 

class MyBot(commands.Bot):
    def __init__(self, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True  # メッセージの内容を取得する権限を追加
        intents.members = True  # メンバーのリストを取得する権限を追加
        super().__init__(**kwargs, intents=intents)
bot = MyBot(command_prefix='$', description='discord bot')
# チャンネルIDとロールIDのマッピング
role_id_map = {
    "https://discord.gg/wswPCRQF": 1194432140637642773,
    "https://discord.gg/Gwdysmt5": 1194430240689233982,
    # 他の招待リンクとロールIDのペアをここに追加
}
@bot.event
async def on_member_join(member):
    invite_list = await member.guild.invites()
    for invite in invite_list:
        if invite.url in role_id_map:
            role_id = role_id_map[invite.url]
            role = discord.utils.get(member.guild.roles, id=role_id)
            if role:
                await member.add_roles(role)
                break
bot.run(TOKEN)
