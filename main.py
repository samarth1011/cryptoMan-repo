from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 10162136

api_hash = '550ad1c3f2c6efcead36d019ec1b0fba'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
print("Waiting for message...")

# print(client.get_me().stringify())
# with client:
#     client.get_messages('@SamarthGodase', limit=100)
@client.on(events.NewMessage(chats='@Trading_Bitcoin_Signals_Tips'))
async def my_event_handler(event):
    try:
        newMessage = event.message.message
    
        if '💶/💵 Currency pair' in newMessage:
            # print("replacing..")
            newMessage = newMessage.replace('💶/💵 Currency pair', 'Currency pair - ')
        if 'CRYPTO IDX' in newMessage:
            # print("replacing..")
            newMessage = newMessage.replace('CRYPTO IDX', '**CRYPTO IDX**')
        if '5 minute' in newMessage:
            newMessage = newMessage.replace('5 minute', '**5 minute**')
        if 'Bet for' in newMessage:
            newMessage = newMessage.replace('Bet for', 'Time -')

        if "And we're gonna put" in newMessage:
            newMessage = newMessage.replace( "And we're gonna put", 'Put it - ')

        if "http://bit.ly/Trade_pro" in newMessage:
            newMessage = newMessage.replace( "http://bit.ly/Trade_pro", 'https://bit.ly/3xUsD7x')

        if "https://t.me/Joseph_singer_pro" in newMessage:
            newMessage = newMessage.replace( "https://t.me/Joseph_singer_pro", 'https://t.me/cryptoMan1011')

        if "Sign up" in newMessage:
            newMessage = newMessage.replace( "Sign up", 'SignUp & trade with that account to earn more profits\n')
        
        if '"DOWN"' in newMessage:
            print("replacing..")
            newMessage = newMessage.replace('"DOWN"', '**⬇️ DOWN**')
            print(f"replaced to - {newMessage}")
        if '"UP"' in newMessage:
            newMessage  = newMessage.replace('"UP"', '**⬆️ UP**')
        if '❗️Attention, everybody!' in newMessage:
            newMessage = newMessage + ' \n\n SignUp & trade with that account to earn more profits - https://bit.ly/3xUsD7x \n\n Write me -  https://t.me/cryptoMan1011'
            print( newMessage)
        await client.send_message('@binomo_olymptrade_VIP_trading',newMessage)
       
    except:
        await client.send_message('@@binomo_olymptrade_VIP_trading',event.message)
    

client.start()
client.run_until_disconnected()

