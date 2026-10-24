<div align="center">

# 🎤 KARAOKE

🇬🇧 English · 🇷🇺 [Русский](README.ru.md)

**A home karaoke app that turns any song into a backing track.**

Search for a song, wait a couple of minutes, and sing. The app removes the vocals,
finds the lyrics, shows the melody, and scores your performance.

`Python` · `PySide6` · `Demucs` · `yt-dlp` · `LRCLIB`

Free · Runs on your own computer · No API keys or subscriptions

</div>

---

## ✨ Features

| | |
|---|---|
| 🔎 **YouTube search** | Type "artist + title" and add the video you want to your library |
| 🎛 **AI vocal removal** | Demucs (htdemucs by Meta) separates vocals from music right on your PC |
| 📝 **Synced lyrics** | Time-synced lyrics come from LRCLIB, and each line fills in as you sing |
| 🎯 **Auto lyric alignment** | If a video has an intro, the lyrics shift to match the actual vocals |
| 🎼 **Pitch lane** | Shows the original melody and your voice: green when you hit the note, pink when you miss |
| 🏆 **Scores and records** | Score out of 100, stars, stats and a personal best for every song |
| 🎧 **Your recordings** | Listen to yourself over the backing track right after singing. Every take is saved |
| 🗣 **Vocal guide** | The "Artist voice" slider mixes the original vocals back in if you forget the melody |
| 🎙 **Mic check** | A live level meter right in the main menu |

> The interface is in Russian. Below, UI labels are given with English translations.

---

## 🚀 Quick start (Windows)

**1. Install Python** 3.11–3.14 from [python.org](https://www.python.org/downloads/).
During setup, make sure to tick **"Add Python to PATH"**.

**2. Run `install.bat`.** It installs:
- **ffmpeg**, for audio processing;
- **Deno**, which yt-dlp needs to download from YouTube;
- **PyTorch**, with CUDA if you have an NVIDIA GPU and the CPU version otherwise;
- **Demucs, PySide6, yt-dlp** and the rest.

> The first install takes 5–15 minutes. If ffmpeg or Deno was just installed,
> close the window and open a new one so Windows can find them.

**3. Run `run.bat`** 🎉

---

## 🎶 How to sing

1. Type something like `Queen Bohemian Rhapsody` and click **Найти** (Search).
2. Click **+ Добавить** (Add) next to the right video.
   💡 Videos with **"Official Audio"** or **"Lyrics"** in the title work best, since music videos often have long intros.
3. The song card shows processing progress:

   | Hardware | Time per song |
   |---|---|
   | NVIDIA GPU | ~20–60 seconds |
   | CPU only | ~1–5 minutes |

   On the very first run, Demucs downloads its model once (~80 MB).
4. Click the finished song, press **🎤 Начать петь** (Start singing), and sing!

### ⌨️ Controls

| Key | Action |
|:---:|---|
| `Space` | pause / resume |
| `←` `→` | seek 5 seconds |
| `[` `]` | shift lyrics 0.25 s earlier / later |
| `Esc` | finish and see your score |

The **Авто** (Auto) button at the bottom re-aligns the lyrics to the vocals.

### 🖱 Right-click a song

- **Найти текст заново** (Find lyrics again): fix the artist or title by hand if the lyrics weren't found or are wrong.
- **Обработать заново** (Reprocess): separate the vocals and fetch the lyrics again.
- **Удалить** (Delete).

---

## 🏆 How scoring works

```
your voice ──► pitch detection (YIN) ───────┐
                                            ├──► compared every 25 ms ──► score
artist vocals ──► original melody ──────────┘
```

- **80% of the score** is pitch accuracy. Tolerance is about one semitone, and **octave doesn't matter**, so you can sing lower or higher than the original.
- **20% of the score** is singing where the artist sings.
- A small delay for reaction time and mic latency is allowed, so you don't have to be frame-perfect.

| Score | Rating |
|:---:|---|
| 92–100 | 🌟 Stage legend! |
| 80–91 | Magnificent! |
| 65–79 | Great singing! |
| 50–64 | Good! |
| 30–49 | Not bad, keep going! |
| 0–29 | Try again! |

---

## 🛠 Troubleshooting

<details>
<summary><b>🎙 Mic is silent / meter doesn't move</b></summary>

1. Pick a **specific microphone** from the list instead of "Microsoft Sound Mapper".
2. Check your laptop's mic-mute key (often F4, F8 or F10, usually with an LED).
3. Windows Settings → System → Sound → Input → raise **Input volume** to 80–100.
4. Settings → Privacy → Microphone → allow access for desktop apps.
5. Close FL Studio and other apps using ASIO drivers, since they can take the mic for themselves.
6. Run **`mic_test.bat`**. It checks every input and shows which one actually picks up sound.
</details>

<details>
<summary><b>📝 Lyrics are early or late</b></summary>

- Click **Авто** (Auto) at the bottom or nudge the lyrics with `[` `]`. The offset is saved per song.
- If the lyrics belong to a different version entirely (live, remix), find them again via right-click or add a different video.
</details>

<details>
<summary><b>⬇️ YouTube downloads fail</b></summary>

YouTube changes things often. Run **`update.bat`** to update yt-dlp.
Also make sure Deno is installed: `winget install DenoLand.Deno`.
</details>

<details>
<summary><b>🐢 Processing is very slow</b></summary>

Without an NVIDIA GPU, the neural network runs on the CPU, which is expected.
Songs are processed one at a time, so you can queue several and go grab a tea ☕
</details>

---

## 📁 Project structure

```
Karaoke website/
├── main.py              entry point
├── install.bat          installs everything
├── run.bat              launches the app
├── update.bat           updates yt-dlp
├── mic_test.bat         microphone diagnostics
├── app/
│   ├── youtube.py       search and download (yt-dlp + ffmpeg)
│   ├── separator.py     vocal removal (Demucs)
│   ├── lyrics.py        lyrics from LRCLIB
│   ├── align.py         auto-aligns lyrics to vocals
│   ├── pitch.py         pitch detection
│   ├── scoring.py       scoring
│   ├── audio.py         playback and mic recording
│   ├── pipeline.py      background processing queue
│   ├── library.py       song library
│   └── ui/              interface: home, singing screen, results
└── library/             your songs (not in git)
    └── <video id>/
        ├── no_vocals.flac   backing track
        ├── vocals.flac      vocals (for scoring and the guide)
        ├── melody.npy       original melody
        ├── lyrics.json      lyrics
        └── takes/           your recordings
```

---

## 🙏 Built with

- [Demucs](https://github.com/facebookresearch/demucs) for music source separation
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube downloads
- [LRCLIB](https://lrclib.net), a free database of synced lyrics
- [PySide6](https://doc.qt.io/qtforpython-6/) for the Qt interface
- [sounddevice](https://python-sounddevice.readthedocs.io/) for audio I/O

> ⚠️ This project is for personal, non-commercial use. Downloaded music and lyrics belong
> to their copyright holders. Don't distribute backing tracks or recordings of other people's music.

<div align="center">

**Sing loud! 🎤✨**

</div>
