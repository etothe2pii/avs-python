import simpleavs
# import wave
from scipy.io.wavfile import read, write
import numpy as np
import time

def handle_speak(speak_directive):
    """ called when a speak directive is received from AVS """
    global handled
    handled = True

    print("Handling speak!")
    print(speak_directive)
    write("response.wav", 24000, speak_directive.audio_data)


def init():
    global handled
    handled = False

config = {
   "client_id": "amzn1.application-oa2-client.1ef94c1474bc43a58f4f699037173ce3",
   "client_secret": "amzn1.oa2-cs.v1.5f73d27b79af4c59865a3adfc68499bdbfb17e3fc831ae962ba2babd0591527b",
   "refresh_token": "Atzr|IwEBILXhuqeDaXLsYXIXCZ8imNwlOEWKxO5vD_zXltD86y5v1db8Y8OxB09hUw2cpxs-xrjPfmQJ1ypn4WZzpmjUuKm78DLYsV7RGTvP8mENEKsTbHSgHB7jA1_zVsQ4SbhHUNaXckPU8eM6DfL86cBNWbHbW1wEDvgpXcmNnteCZ4PGjST0r72sOvQrOU_ggTDPbjS5G-A0wL7XbqhkOvhxvcrTDfy1i45Zm10MZDOGIEAL0qKnw1A_HUVUtKlOWGIjGIY38u2QSwDTcO6JeIYpnwwYPawU3xLWijQXfw75SoMQ0GE5dMIk0zSaLTbRA5MevpeWW-aRdsCcls6nKZI4L3CvW-KNLzuKPhYp-CmRK60D3uORDMcHKwStMowjKlw3fBU",
}

print("Hello")

init()



# AvsClient requires a dict with client_id, client_secret, refresh_token
avs = simpleavs.AvsClient(config)

avs.speech_synthesizer.speak_event += handle_speak
avs.speech_synthesizer.speak_event.handle(handle_speak)

avs.connect()

# wav_request_data = wave.open("../bark-with-voice-clone/output/attenborough_to_class_0.wav", "r")
r, wav_request_data = read("audio/attenborough_to_class_0.wav")


avs.speech_recognizer.recognize(audio_data=wav_request_data.tobytes(), profile='NEAR_FIELD')
start = time.time()
while not handled:
    print(f"Time since start: {time.time() - start:.2f}", end = "\r")
    time.sleep(0.2)
    avs.speech_synthesizer.speak_event.fire()

# sleep / poll for quit

avs.disconnect()