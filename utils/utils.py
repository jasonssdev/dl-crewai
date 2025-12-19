from dotenv import load_dotenv, find_dotenv
import json
import os


def load_env():
    _ = load_dotenv(find_dotenv())


def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key


def get_exa_api_key():
    load_env()
    exa_api_key = os.getenv("EXA_API_KEY")
    return exa_api_key


def get_serper_api_key():
    load_env()
    serper_api_key = os.getenv("SERPER_API_KEY")
    return serper_api_key


def get_dict_keys(task_output):
    """
    Extracts the keys from a dictionary-like string.
    """
    # Check if task outputs are dictionaries and show their keys
    if isinstance(task_output, str):
        try:

            parsed = json.loads(task_output)
            if isinstance(parsed, dict):
                print("Can be parsed as JSON dictionary")
                print("  Keys: {list(parsed.keys())}")
            else:
                print("JSON parses but not as dictionary")
        except json.JSONDecodeError:
            print("Cannot parse as JSON")
    print()
