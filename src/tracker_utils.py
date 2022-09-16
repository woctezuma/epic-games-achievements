from src.disk_utils import get_tracker_export_fname, save_json


def intersect_sandbox_ids(sandbox_ids_dict, achievements):
    filtered_sandbox_ids_dict = {k: v for k, v in sandbox_ids_dict.items() if v in achievements}
    return filtered_sandbox_ids_dict


def export_sandbox_ids_for_tracker(sandbox_ids_dict, achievements):
    filtered_sandbox_ids_dict = intersect_sandbox_ids(sandbox_ids_dict, achievements)
    save_json(filtered_sandbox_ids_dict, get_tracker_export_fname(), prettify=True)
    return
