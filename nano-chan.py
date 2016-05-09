import sopel.module

@sopel.module.commands('hello')
def hello(bot, trigger):
    bot.say('Hello!')

@sopel.module.commands('bots')
def bots(bot, trigger):
    bot.say('Reporting in! [Python]')

