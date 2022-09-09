from src.disk_utils import get_sandbox_ids_fname, load_json


def load_sandbox_ids_dict():
    try:
        sandbox_ids_dict = load_json(get_sandbox_ids_fname())
    except FileNotFoundError:
        sandbox_ids_dict = dict()
    return sandbox_ids_dict
