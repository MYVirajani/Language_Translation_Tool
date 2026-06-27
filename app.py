import streamlit as st
from translator import translate_text, SUPPORTED_LANGUAGES

st.set_page_config(page_title="Translator", layout="wide")

st.title("Language Translator")
st.markdown("Translate text across 10+ languages instantly.")

lang_names = list(SUPPORTED_LANGUAGES.keys())
col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("Source Language", lang_names, index=0)

with col2:
    target_lang_name = st.selectbox("Target Language", lang_names, index=1)

input_text = st.text_area("Enter text to translate", height=150, placeholder="Type something here...")

if st.button("Translate", type="primary"):
    if not input_text.strip():
        st.warning("Please enter some text first.")
    else:
        source_code = SUPPORTED_LANGUAGES[source_lang_name]
        target_code = SUPPORTED_LANGUAGES[target_lang_name]
        
        with st.spinner("Translating..."):
            result = translate_text(input_text, source_code, target_code)
        
        if result["error"]:
            st.error(f"Translation error: {result['error']}")
        else:
            st.text_area("Translated Text", value=result["translated"], height=150)
