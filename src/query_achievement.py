from src.api import send_post_request_to_api


def get_params_to_query_achievement(sandbox_id):
    params = {
        "operationName": "Achievement",
        "variables": {"sandboxId": sandbox_id, "locale": "en"},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "7d54399ad8b8b5538bc2d93ee66b07014432b5488945cda35fe0b1fc70eea83a",
            }
        },
    }

    return params


def to_achievement(sandbox_id, verbose=True):
    params = get_params_to_query_achievement(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        achievement = data["data"]["Achievement"]["productAchievementsRecordBySandbox"]
    except (TypeError, KeyError) as e:
        achievement = None
    return achievement
