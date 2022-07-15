from bot import client

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    exam_info = (
        'Welcome to the exam, please sign-in using your intranet account to proceed to the exam session.\n'
        ' \n'
        'REMINDER There is NO practice mode available, REAL mode only, your grade will be counted on the intranet.\n'
        'By the grace of REZNET, may your exam be good and DON\'T PANIC.\n'
        ' \n'
        'Normally, exams should be silent, though, as we don\'t have any physical campuses... Listening to music is OK.\n')

    if message.content == 'yes':
        await message.channel.send(exam_info)