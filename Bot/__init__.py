import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 15821484)) #API ID
API_HASH = environ.get('API_HASH', 'f66b8ad00b991244c65fedc357cc5699') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '6727173187:AAFFrrKkO_mNXmxot3xPvRlSXMLxywI0wX8') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://Mirrorbot:mirrorbot@cluster0.toq6yw9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 1362103108)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1002139530003))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1002114221171))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', 2139530003)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
