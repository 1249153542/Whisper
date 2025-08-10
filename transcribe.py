import argparse
import os
import subprocess
import configparser
import logging

def setup_logging():
    """Sets up logging to a file."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("transcriber.log"),
            logging.StreamHandler()
        ]
    )

def load_config(config_path="config.txt"):
    """
    Loads the configuration from the specified file.
    """
    config = configparser.ConfigParser()
    if not os.path.exists(config_path):
        logging.error(f"Config file not found at '{config_path}'")
        return None
    config.read(config_path)
    return config

def main():
    """
    Main function for the transcription script.
    """
    setup_logging()
    parser = argparse.ArgumentParser(description="Recursively transcribe media files in a folder.")
    parser.add_argument("folder", help="The folder to scan for media files.")
    parser.add_argument("--dry-run", action="store_true", help="Print the commands without executing them.")
    args = parser.parse_args()

    config = load_config()
    if not config:
        return

    if not os.path.isdir(args.folder):
        logging.error(f"Folder not found at '{args.folder}'")
        return

    logging.info(f"Scanning folder: {args.folder}")

    general_config = config["General"]
    media_extensions = [ext.strip() for ext in general_config["media_extensions"].split(",")]

    media_files = find_media_files(args.folder, media_extensions)

    if not media_files:
        logging.info("No media files found to transcribe.")
        return

    logging.info(f"Found {len(media_files)} media files to transcribe.")

    for media_file in media_files:
        transcribe_file(media_file, config, args)

def transcribe_file(file_path, config, args):
    """
    Transcribes a single media file using the whisper_cpp executable.
    """
    logging.info(f"Preparing to transcribe {file_path}...")
    whisper_params = config["WhisperParams"]
    general_params = config["General"]

    command = ["./whisper_cpp"]

    # Add arguments from config
    for key, value in whisper_params.items():
        if key in ["model", "language", "threads", "prompt", "offset_t_ms", "offset_n", "duration_ms", "max_context", "max_len", "word_thold"]:
            if value:
                command.extend([f"--{key.replace('_', '-')}", value])
        else: # Boolean flags
            if whisper_params.getboolean(key):
                command.append(f"--{key.replace('_', '-')}")

    # Add output format flag
    output_format = general_params.get("output_format", "txt")
    command.append(f"--output-{output_format}")

    # Add the file to transcribe
    command.extend(["-f", file_path])

    if args.dry_run:
        logging.info("DRY RUN: Would execute the following command:")
        logging.info(" ".join(command))
        return

    try:
        logging.info(f"Transcribing {file_path}...")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logging.info(f"Successfully transcribed {file_path}")
        logging.debug(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error transcribing {file_path}:")
        logging.error(e.stderr)
    except FileNotFoundError:
        logging.error("Error: whisper_cpp executable not found. Make sure it's in the same directory as the script.")


def find_media_files(folder, extensions):
    """
    Recursively finds all files in a folder with the given extensions.
    """
    found_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                found_files.append(os.path.join(root, file))
    return found_files

if __name__ == "__main__":
    main()
