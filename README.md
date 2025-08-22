# 📞 AI Translator for Phone Calls (Hausa ↔ English)

Wannan project ɗin yana bada damar yin **wayar AI interpreter** ta amfani da:
- 🗣 Twilio (kiran waya)
- 🤖 OpenAI (fassara & gano harshen magana)
- 🔊 gTTS (Text-to-Speech)
- 🌐 Flask (Python web server)

---

## 🚀 Features
- Gane harshen Hausa ↔ English.
- Fassara nan take (ba streaming ba, sai bayan magana).
- Maida rubutu zuwa murya a cikin kira.
- Gudana kai tsaye a cikin **Twilio call**.

---

## ☁️ Deployment Options

### 🔹 Render
1. Create new Web Service on [Render](https://render.com).
2. Connect this repo.
3. Environment:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
   - Environment Variables:
     - `OPENAI_API_KEY=YOUR_OPENAI_KEY`
4. After deploy, Render will give you a URL.

### 🔹 Railway (One-Click Deploy)
Click below to deploy instantly to Railway 👇

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/babbajee/ai-translator&envs=OPENAI_API_KEY&OPENAI_API_KEYDesc=Your+OpenAI+API+Key)



---

## 📞 Twilio Setup
1. Go to [Twilio Console](https://www.twilio.com/console).
2. Buy a phone number (if you don’t have one).
3. Under **Voice & Fax → A CALL COMES IN**, set webhook:
(or Railway URL).
4. Save changes.

---

## 🎤 Usage
- Call your Twilio number.
- Speak in **Hausa** → AI will translate and play in **English**.
- Speak in **English** → AI will translate and play in **Hausa**.

---

## 🙌 Author
Built by **Umar Salisu Aliyu**  
Student of ATBU | AI Enthusiast | Programmer & Tailor
