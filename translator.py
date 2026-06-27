import requests

SUPPORTED_LANGUAGES = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh",
    "Arabic": "ar",
    "Hindi": "hi",
    "Tamil": "ta",
    "Sinhala": "si",
}

def translate_text(text: str, source_lang: str, target_lang: str) -> dict:
    """
    Returns: {"translated": str, "error": str | None}
    """
    if not text.strip():
        return {"translated": "", "error": "Input text is empty."}
    
    lang_pair = f"{source_lang}|{target_lang}"
    url = "https://api.mymemory.translated.net/get"
    
    try:
        response = requests.get(url, params={"q": text, "langpair": lang_pair}, timeout=10)
        data = response.json()
        
        if data["responseStatus"] == 200:
            return {"translated": data["responseData"]["translatedText"], "error": None}
        else:
            return {"translated": "", "error": data.get("responseDetails", "Translation failed.")}
    
    except requests.exceptions.Timeout:
        return {"translated": "", "error": "Request timed out. Please try again."}
    except Exception as e:
        return {"translated": "", "error": str(e)}