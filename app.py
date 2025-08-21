from flask import Flask, request, Response, send_from_directory
from twilio.twiml.voice_response import VoiceResponse
import openai
from gtts import gTTS
import os

app = Flask(__name__)

# === OpenAI API key (SAKA A Render ko Railway Dashboard -> Environment Variables) ===
openai.api_key = os.environ.get("OPENAI_API_KEY")

# static folder don adana mp3
OUTPUT_DIR = "static"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/voice", methods=["POST"])
def voice():
    """Lokacin da aka kira Twilio number"""
    resp = VoiceResponse()
    resp.say("Sannu! Wannan AI Translator ne. Yi magana yanzu.", language="ha")
    resp.record(max_length=5, transcribe=True, action="/process")
    return Response(str(resp), mimetype="application/xml")

@app.route("/process", methods=["POST"])
def process():
    text = request.form.get("TranscriptionText", "")
    print("Rubutun daga mai kira:", text)

    if not text:
        text = "Ban ji komai ba."

    # Tambayi GPT don gane harshen rubutu
    detect = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Detect the language of this text: {text}. Reply only 'Hausa' or 'English'."}]
    )
    lang = detect["choices"][0]["message"]["content"].strip()
    print("An gano harshen:", lang)

    # Fassara bisa harshen da aka gano
    if "Hausa" in lang:
        prompt = f"Translate this Hausa to English: {text}"
        target_lang = "en"
    else:
        prompt = f"Translate this English to Hausa: {text}"
        target_lang = "ha"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    translated = response["choices"][0]["message"]["content"]
    print("Fassara:", translated)

    # TTS bisa harshen da muka mayar
    tts = gTTS(text=translated, lang=target_lang)
    filename = "out.mp3"
    filepath = os.path.join(OUTPUT_DIR, filename)
    tts.save(filepath)

    # Gina TwiML don Twilio
    resp = VoiceResponse()
    resp.play(url=request.url_root + "static/out.mp3")
    # Sake sauraro
    resp.record(max_length=5, transcribe=True, action="/process")
    return Response(str(resp), mimetype="application/xml")

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Twilio zai iya samun mp3 daga nan"""
    return send_from_directory(OUTPUT_DIR, filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
