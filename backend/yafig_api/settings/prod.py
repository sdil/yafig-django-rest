from .base import *
import os

ALLOWED_HOSTS = [os.environ.get("HOST", "localhost")]
