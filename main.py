from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

# Create a Pyrogram client
api_id = 21434357
api_hash = "b5f8ae84db79639640b9076606c52694"
proxy = {
    'hostname': 'proxy.besenior.uz',
    'port': 8080,
    'username': 'ezozbek',
    'password': '20077002'
}
app = Client("telegram_proxy", api_id=api_id, api_hash=api_hash, proxy=proxy)


def message_handler(client: Client, message: Message):

    print("[*] Received message:", message)



app.add_handler(MessageHandler(message_handler))


app.run()
