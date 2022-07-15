from bot import client

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    examshell_info = (
        'You are starting examshell.\n'
        'Are you sure you want to start an exam session ?\n'
        'There is no Practice mode available, you\'ll be in real mode for this session.\n'
        ' \n'
        'During this exam you\'ll receive multiple exercises, get as many aswers correct as possible,\n'
        'getting points helps you progress further in your exam, though, don\'t panic if you don\'t \n'
        'have the same exercise as your neighbors, life\'s unfair. Deal with it.\n'
        ' \n'
        'For more information on how to use examshell, please type README, you\'ll be DMed the Instructions manual.\n')
    
    if message.content == 'examshell':
    #    response = message.channel.send(examshell_info)
        await message.channel.send(examshell_info)