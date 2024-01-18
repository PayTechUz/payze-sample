"""
payze settings.
"""
from payze.settings.default import env


# all payze credentials are required
PAYZE: dict = {
    "url": env.str("PAYZE_URL"),
    "auth_token": env.str("PAYZE_AUTH_TOKEN"),
    "hooks": {
        "web_hook_gateway": env.str("PAYZE_WEB_HOOK_GATEWAY"),
        "error_redirect_gateway": env.str("ERROR_REDIRECT_GATEWAY"),
        "success_redirect_gateway": env.str("SUCCESS_REDIRECT_GATEWAY"),
    }
}
