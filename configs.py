# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "29346781"))
    API_HASH = getenv("API_HASH", "75fb004873db1864a09c71cd1307bfa8")
    BOT_TOKEN = getenv("BOT_TOKEN", "7373116422:AAG55hLxYnE4eMTbYu_xa93aqywF59JaBYo")
    FSUB = getenv("FSUB", "SihagBots")
    CHID = int(getenv("CHID", "-1001959367903"))
    SUDO = list(map(int, getenv("SUDO", "5860332990").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Sihagbots:585xpplus@cluster0.7o52a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
