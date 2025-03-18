from vosk import Model, KaldiRecognizer
import wave

model_path = "models/vosk-model-ru-0.42"
model = Model(model_path)

# Загрузка аудиофайла
audio_file = "audio1.wav"
wf = wave.open(audio_file, "rb")

# Проверьте параметры аудиофайла
sample_rate = wf.getframerate()
channels = wf.getnchannels()

print(f"Sample rate: {sample_rate} Hz")
print(f"Channels: {channels}")

if channels != 1:
    raise ValueError("Аудиофайл должен быть моно.")

rec = KaldiRecognizer(model, sample_rate)

results = []
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        results.append(rec.Result())

final_result = rec.FinalResult()
results.append(final_result)

for result in results:
    print(result)