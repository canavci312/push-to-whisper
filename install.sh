#!/bin/bash

echo "🎯 Installing Whisper Voice-to-Text Hotkey Tool"
echo "=============================================="

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Please install Homebrew first:"
    echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
fi

# Install required system dependencies
echo "📦 Installing system dependencies..."
brew install portaudio ffmpeg

# Install Python packages
echo "🐍 Installing Python packages..."
pip install whisper-mic sounddevice pyperclip pynput pyautogui

echo "✅ Installation complete!"
echo ""
echo "🚀 Usage:"
echo "1. Run: ./start_whisper_mic.sh"
echo "2. Hold Right Command (⌘) key and speak"
echo "3. Release key to transcribe and insert text"
echo "4. Press Esc to exit"
echo ""
echo "📝 Note: You may need to grant microphone permissions when first running."