from telethon.sync import TelegramClient
from telethon.sessions import StringSession

def generate_telethon_session(api_id, api_hash, session_string):
    with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        return client.session.save()

    return None
