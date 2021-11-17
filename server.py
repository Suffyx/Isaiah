from quart import Quart, render_template, request, session, redirect, url_for
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc
from core import Isaiah

bot = Isaiah()

app = Quart(__name__)
ipc_client = ipc.Client(secret_key = bot.config.IPC_SECRET_KEY)

discord = DiscordOAuth2Session(app)

@app.route("/")
async def home():
  """Renders the home page."""
  return await render_template("index.html", auhtorized = await discord.authorized)

@app.route("/login")
async def login():
  """Creates an Oauth2 Session for Users to Login Via Discord."""
	return await discord.create_session()

@app.route("/callback")
async def callback():
  """Returns OAuth2 Callback if the user is authorized."""
	try:
		await discord.callback()
	except Exception:
		pass
  
	return redirect(url_for("dashboard"))

@app.route("/dashboard")
async def dashboard():
  """Returns the dashboard is a user is authorized, or redirects them to authorize themselves."""
	if not await discord.authorized:
		return redirect(url_for("login")) 

	guild_count = await ipc_client.request("get_guild_count")
	bot_guild_ids = await ipc_client.request("get_guild_ids")

	user_guilds = await discord.fetch_guilds()

	guilds = []

	for guild in user_guilds:
		if guild.permissions.administrator:			
			guild.class_color = "green-border" if guild.id in bot_guild_ids else "red-border"
			guilds.append(guild)
      
    else:
      guild.class_color = "red-border"
      guilds.append(guild)

	guilds.sort(key = lambda x: x.class_color == "red-border")
	name = (await discord.fetch_user()).name
	return await render_template("dashboard.html", guild_count = guild_count, guilds = guilds, username=name)

@app.route("/dashboard/<int:guild_id>")
async def dashboard_server(guild_id):
  """Returns the guild dashboard if the user is authorized else redirects to the login page.
  
     Paremeters:
        guild_id: int - The guild id for the guild that the dashboard is attempting to reach.
  """
	if not await discord.authorized:
		return redirect(url_for("login")) 

	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	if guild is None:
		return redirect(f'https://discord.com/oauth2/authorize?&client_id={bot.config.DISCORD_CLIENT_ID}&scope=bot&permissions=8&guild_id={guild_id}&response_type=code&redirect_uri={bot.config.DISCORD_REDIRECT_URI}')
	return guild["name"]

if __name__ == "__main__":
	app.run(debug=False)
