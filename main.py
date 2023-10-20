import interactions, requests

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
    match responses.status_code: 
        case 404 :
            await ctx.send("Error IP not found")
        case 200 :
            await ctx.send(str(responses.json()))

bot = interactions.Client()
bot.start(TOKEN)
