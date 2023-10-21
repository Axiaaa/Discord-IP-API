import interactions, requests, json

TOKEN = "token"

@interactions.slash_command(
    name="ip",
    description="Get info from an IP"
)
@interactions.slash_option(
    name="ip",
    description="give the IP",
    opt_type=interactions.OptionType.STRING,
    required=True,
)
async def ip(ctx : interactions.InteractionContext, ip : str) :
    responses = requests.get(f"http://ip-api.com/json/{ip}")
    isfail = True if responses.json()["status"] == "success" else False
    await ctx.send(json.dumps(responses.json(), indent=4)) if isfail == True else await ctx.send(f"Error from the API :\n" + responses.json()["message"])

bot = interactions.Client()
bot.start(TOKEN)
