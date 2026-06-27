#  Language Translation Tool

A multilingual text translation web application built with **Python** and **Streamlit**, powered by the **MyMemory Translation API**. Users can enter text, select source and target languages, and receive instant translations.



## 📁 Project Structure

```
language_translation_tool/
│
├── app.py               # Main Streamlit UI
├── translator.py        # API call logic (MyMemory)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MYVirajani/Language_Translation_Tool.git
cd language-translation-tool
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---


## 🖥️ How to Use

1. **Enter text** in the "Enter text to translate" box
2. **Select Source Language** (e.g., English)
3. **Select Target Language** (e.g., French)
4. Click **Translate**
5. View the translated text in the output box

---

## 🌐 Supported Languages

| Language | Code |
|---|---|
| English | `en` |
| French | `fr` |
| Spanish | `es` |
| German | `de` |
| Japanese | `ja` |
| Chinese | `zh` |
| Arabic | `ar` |
| Hindi | `hi` |
| Tamil | `ta` |
| Sinhala | `si` |

---

## 🔌 API Details

This project uses the **MyMemory Translation API** — a free, no-key-required REST API.

**Endpoint:**
```
GET https://api.mymemory.translated.net/get?q={text}&langpair={source}|{target}
```

**Free Tier Limits:**
- 1,000 requests/day (anonymous)
- 10,000 requests/day (with a registered email)

**Why MyMemory?**
- No API key or billing setup required
- Can be swapped for Google Translate API or Microsoft Azure Translator for production use

