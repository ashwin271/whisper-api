#!/bin/bash

# Function to detect OS
detect_os() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$NAME
    elif [ "$(uname)" == "Darwin" ]; then
        OS="macOS"
    else
        OS="unknown"
    fi
}

# Function to install ffmpeg on Ubuntu/Debian
install_ffmpeg_debian() {
    echo "Installing ffmpeg on Ubuntu/Debian..."
    sudo apt update
    sudo apt install -y ffmpeg
}

# Function to install ffmpeg on macOS
install_ffmpeg_mac() {
    echo "Installing ffmpeg on macOS..."
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found. Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install ffmpeg
}

# Main installation logic
main() {
    detect_os
    echo "Detected OS: $OS"

    case $OS in
        "Ubuntu"|"Debian GNU/Linux")
            install_ffmpeg_debian
            ;;
        "macOS")
            install_ffmpeg_mac
            ;;
        *)
            echo "Unsupported operating system: $OS"
            echo "Please install ffmpeg manually"
            exit 1
            ;;
    esac

    # Verify installation
    if command -v ffmpeg &> /dev/null; then
        echo "ffmpeg installed successfully!"
        ffmpeg -version | head -n 1
    else
        echo "ffmpeg installation failed!"
        exit 1
    fi
}

main