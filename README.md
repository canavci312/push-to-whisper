# 🎯 Whisper Voice-to-Text Hotkey Tool

A fast, local voice-to-text tool that instantly inserts transcribed speech at your cursor position.

## ✨ Features

- **Instant transcription**: Hold a key, speak, release to insert text
- **Works anywhere**: Inserts text at cursor in any app
- **Fast & local**: Uses OpenAI's Whisper Turbo model locally
- **No typing lag**: Text appears instantly at cursor position
- **Privacy focused**: All processing happens on your machine

## 🚀 Quick Start

### Installation

1. **Clone or download these files**:
   - `whisper_mic_hotkey.py`
   - `start_whisper_mic.sh`
   - `install.sh`

2. **Run the installer**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

3. **Start the tool**:
   ```bash
   ./start_whisper_mic.sh
   ```

### Usage

1. **Hold Right Command (⌘) key** and speak
2. **Release the key** when done speaking
3. **Text appears instantly** at your cursor position
4. **Press Esc** to exit the tool

## 📋 Requirements

- macOS (tested on macOS 11+)
- Python 3.8+
- Homebrew
- Microphone access permission

## 🔧 Troubleshooting

### First Run Issues
- **Microphone permission**: Grant permission when prompted
- **Model download**: First run downloads ~1.5GB Whisper model

### Performance Tips
- **Faster model**: Change `"turbo"` to `"base"` in the code for speed over accuracy
- **Better accuracy**: Change `"turbo"` to `"large-v3"` for accuracy over speed

### Common Issues
- **No text appears**: Check microphone permissions in System Preferences
- **Slow transcription**: Ensure you're using a recent Mac with enough RAM
- **Wrong characters**: Make sure your system language is set correctly

## 🛠️ Customization

Edit `whisper_mic_hotkey.py` to customize:

- **Hotkey**: Change `Key.cmd_r` to different key
- **Model**: Change `"turbo"` to `"base"`, `"small"`, `"medium"`, or `"large-v3"`
- **Language**: Add `language="en"` for English-only (faster)

## 📄 License

This tool uses OpenAI's Whisper model and various open-source libraries. 
Use responsibly and respect privacy when transcribing conversations.

## 🤝 Contributing

Found a bug or want to improve the tool? Feel free to modify and share!

---

**Enjoy hands-free typing! 🎤✨**