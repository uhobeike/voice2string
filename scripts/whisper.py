from io import BytesIO
import openai
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 1568
r.dynamic_energy_threshold = True


def get_audio_from_mic():
    with sr.Microphone(sample_rate=16000) as source:
        print("音声入力待機")
        audio = r.listen(source)
        print("音声を文字列に変換")
        return audio


def voice_to_text():
    audio = get_audio_from_mic()
    audio_data = BytesIO(audio.get_wav_data())
    audio_data.name = 'from_mic.wav'
    transcript = openai.Audio.transcribe('whisper-1', audio_data)
    return transcript['text']
