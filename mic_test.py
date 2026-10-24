"""Диагностика микрофона: показывает устройства и уровень сигнала с каждого."""
import time

import numpy as np
import sounddevice as sd

print("=== Аудио-системы ===")
for i, api in enumerate(sd.query_hostapis()):
    mark = "  <- по умолчанию" if i == sd.default.hostapi else ""
    print(f"[{i}] {api['name']}{mark}")

print("\n=== Микрофон по умолчанию ===")
print(sd.default.device)

print("\n=== Проверка входов (говори в микрофон!) ===")
for i, d in enumerate(sd.query_devices()):
    if d["max_input_channels"] < 1:
        continue
    api = sd.query_hostapis(d["hostapi"])["name"]
    name = f"[{i}] {d['name']}  ({api}, {int(d['default_samplerate'])} Гц)"
    peaks = []
    try:
        def cb(indata, frames, t, status):
            peaks.append(float(np.sqrt(np.mean(indata[:, 0] ** 2))))
        with sd.InputStream(device=i, channels=1, samplerate=int(d["default_samplerate"]),
                            dtype="float32", callback=cb):
            time.sleep(1.5)
        lvl = max(peaks) if peaks else 0.0
        bar = "#" * int(min(40, lvl * 400))
        verdict = "ТИШИНА (0)" if lvl == 0 else ("очень тихо" if lvl < 0.003 else "OK")
        print(f"{name}\n     уровень {lvl:.4f}  {bar}  {verdict}")
    except Exception as e:
        print(f"{name}\n     ОШИБКА: {e}")

print("\nЕсли везде ТИШИНА (0): Параметры Windows -> Конфиденциальность -> Микрофон ->")
print("включи «Доступ к микрофону» и «Разрешить классическим приложениям доступ к микрофону».")
