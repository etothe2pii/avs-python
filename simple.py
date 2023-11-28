import simpleavs
# import wave
from scipy.io.wavfile import read
import numpy as np

def handle_speak(speak_directive):
    """ called when a speak directive is received from AVS """
    print(speak_directive)

config = {
   "client_id": "amzn1.application-oa2-client.1ef94c1474bc43a58f4f699037173ce3",
   "client_secret": "amzn1.oa2-cs.v1.5f73d27b79af4c59865a3adfc68499bdbfb17e3fc831ae962ba2babd0591527b",
   "refresh_token": "Atzr|IwEBIDOXTzFgnUmBlxW5uc6N84HXeT3-FXV4LqHSo2AJszdC1wy42ZP7p1XeGzM1aokpiyd1INsST4rTwOOPu_dvLZG210FOhLjq3HMpYsPn3uRHIaOKN8CmqJpFYGqBeKnVfAF8C-8OSsJG3aLhkrixQJJ1pWXri3hHjt48jldcoVZlN8zX9GUdDAsR_RDYYzRZuepJ_mQqUHdZ7Kiqg8yzGKb7ht_SsnWbvb6vqEDBWSCIIc4WjilkvwiKpLdT0sCQwnfUJfgW5M4AGI_jW7wtFiN0nSfgf-RYH4dEOzN8CoO2qBK9VoI0B8KvQ4fm6NQRQ1imYkW7ItkqyjegTQXecGYm56NF6Onk1vugXGZFg3NzkQ",
}

print("Hello")

# AvsClient requires a dict with client_id, client_secret, refresh_token
avs = simpleavs.AvsClient(config)

avs.speech_synthesizer.speak_event += handle_speak

avs.connect()

# wav_request_data = wave.open("../bark-with-voice-clone/output/attenborough_to_class_0.wav", "r")
r, wav_request_data = read("../bark-with-voice-clone/output/attenborough_to_class_0.wav")


avs.speech_recognizer.recognize(audio_data=wav_request_data.tobytes(), profile='NEAR_FIELD')



# sleep / poll for quit

avs.disconnect()