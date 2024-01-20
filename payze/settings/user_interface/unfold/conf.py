"""
unfold ui settings.
"""
from payze.settings import default
from payze.settings.user_interface.unfold import site
from payze.settings.user_interface.unfold import sidebar

IS_UNFOLD_UI_ENABLED = default.env.bool("IS_UNFOLD_UI_ENABLED", True)

if IS_UNFOLD_UI_ENABLED:
    for index, app in enumerate([
        'unfold',
        'unfold.contrib.forms',
        'unfold.contrib.filters',
        'unfold.contrib.import_export',
        'unfold.contrib.guardian',
        'unfold.contrib.simple_history',
    ]):
        default.INSTALLED_APPS.insert(
            index, app,
        )

    UNFOLD = {}

    UNFOLD.update(
        site.SITE,
    )
    UNFOLD.update(
        sidebar.SIDEBAR
    )
