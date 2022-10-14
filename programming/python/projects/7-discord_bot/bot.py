import hikari
import lightbulb

bot = lightbulb.BotApp(token='INSERTTOKENHERE')

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot has started")

@bot.command
@lightbulb.command('noob', 'Finds noobs')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Ben is a noob!')
bot.run()