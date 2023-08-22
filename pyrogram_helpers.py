from pyrogram import Client, StringSession

def generate_pyrogram_session(api_id, api_hash, session_string):
    with Client(StringSession(session_string), api_id, api_hash) as app:
        return app.export_session_string()

    return None
