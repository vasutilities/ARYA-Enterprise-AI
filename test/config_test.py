from app.config import get_settings

def test_get_settings():
    settings = get_settings()
    assert settings.BEDROCK_EMBED_MODEL == "amazon.titan-embed-text-v2:0"
    assert settings.BEDROCK_CHAT_MODEL == "amazon.nova-lite-v1:0"


    
