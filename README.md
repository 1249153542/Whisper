# Media Transcriber

This is a command-line application that recursively walks through a folder and transcribes all media files using a C++ implementation of OpenAI's Whisper model.

## Features

*   Recursively scans a directory for media files.
*   Transcribes a wide range of media formats (configurable).
*   Powered by a highly optimized C++ Whisper implementation.
*   Configuration is managed through a simple `config.txt` file.
*   Logs all operations to `transcriber.log`.

## Prerequisites

1.  **Whisper C++ Executable:** This tool relies on a compiled C++ executable named `whisper_cpp`. The source code and build instructions are included in this repository. You must compile it and place the `whisper_cpp` executable in the same directory as the `transcribe.py` script.

2.  **Whisper Model:** You need to download a Whisper model in the `ggml` format. The default configuration expects the `ggml-base.en.bin` model.
    *   You can download models from the [Hugging Face repository](https://huggingface.co/ggerganov/whisper.cpp/tree/main).
    *   Create a `models` directory in the root of this project.
    *   Place the downloaded model file (e.g., `ggml-base.en.bin`) inside the `models` directory.

3.  **Python 3:** The wrapper script is written in Python 3.

## Configuration

All configuration is done through the `config.txt` file.

*   **[General]**
    *   `media_extensions`: A comma-separated list of file extensions to look for (e.g., `.wav,.mp3,.mp4`).
    *   `output_format`: The desired output format for the transcriptions. Supported formats are `txt`, `vtt`, and `srt`.

*   **[WhisperParams]**
    *   This section contains all the parameters to be passed to the `whisper_cpp` executable. You can customize the model path, language, number of threads, and many other options. Refer to the comments in the `config.txt` file for more details.

## Usage

Once you have the `whisper_cpp` executable and the model file in place, you can run the transcriber from your terminal.

**Basic Usage:**

```bash
python3 transcribe.py /path/to/your/media/folder
```

This command will scan the specified folder, find all media files matching the extensions in your `config.txt`, and transcribe them one by one.

**Dry Run:**

If you want to see which files would be transcribed and what commands would be executed without actually running the transcription, you can use the `--dry-run` flag:

```bash
python3 transcribe.py /path/to/your/media/folder --dry-run
```

This is useful for testing your configuration and ensuring the script is finding the correct files.
