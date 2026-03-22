import discord
from discord import app_commands
import os 
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # スラッシュコマンドを同期
        await self.tree.sync()

client = MyClient()

@client.tree.command(name="coct", description="CoC のセッション情報を整形して出力します")
@app_commands.describe(
    version="CoC の版数 (6 か 7)",
    gm="GM の名前",
    count="卓の回数",
    title="シナリオ名",
    url="ココフォリアの URL"
)
async def coct(interaction: discord.Interaction, version: int, gm: str, count: str, title: str, url: str):
    # 版数による表記の分岐
    prefix = "新 CoC シナリオ" if version == 7 else "CoC シナリオ"
    
    # フォーマットに合わせてメッセージを作成
    formatted_message = f"【{prefix}】{title}【{gm}卓{count}】\n{url}"
    
    # メッセージを送信
    await interaction.response.send_message(formatted_message)

if TOKEN is not None:
    client.run(TOKEN) #
else:
    print("エラー：TOKENが.envファイルに見つからないよ！確認してね。")