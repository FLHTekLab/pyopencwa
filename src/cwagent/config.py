import os
import dotenv

dotenv.load_dotenv()


def get_cwa_uri():
    return os.getenv("CWA_API_HOST_URI", "https://opendata.cwb.gov.tw/api")


def get_api_uri():
    return os.getenv("API_HOST_URI", "http://127.0.0.1:5000")


def get_cwa_auth_key():
    return os.getenv("CWA_AUTH_KEY", "")


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
        'standard': {
            'format': '[%(levelname)s] %(name)s: %(message)s'
            # 'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "DEBUG",
            # "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "filename": "cwagent.log",
            "maxBytes": 5 * 1024 * 1024,  # 5 MB
            "backupCount": 3,
            "level": "INFO"
        }
    },
    "root": {
        "handlers": ["console"],
    },
    "loggers": {
        "urllib3": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False
        },
        "werkzeug": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "cwagent.entry_points.cli": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        },
        "cwagent": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        },
        "tests": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}
