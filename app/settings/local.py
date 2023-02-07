from .base import *  # noqa:F403
from .common import *  # noqa:F403

DEBUG = env.bool("DEBUG", True)  # noqa:F405

DEVELOPMENT_APPS = ["django_extensions"]

INSTALLED_APPS += DEVELOPMENT_APPS  # noqa:F405
