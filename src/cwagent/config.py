import os
import dotenv

dotenv.load_dotenv()


def get_cwa_uri():
    return os.getenv("CWA_API_HOST_URI", "https://opendata.cwa.gov.tw/api")


def get_api_ssl_check_flag():
    return True if os.getenv("CWA_API_SSL_CHECK_FLAG") != '0' else False


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
        "api_timer": {
            'format': '%(asctime)s, %(message)s'
        },
        "api_response": {
            'format': '%(message)s'
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
        "api_timer": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "api_timer",
            "filename": "cwa-api-timer.log",
            "maxBytes": 5 * 1024 * 1024,  # 5 MB
            "backupCount": 3,
            "level": "INFO",
            # "stream": "ext://sys.stdout"
        },
        "O-A0001-001": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "api_response",
            "filename": "O-A0001-001.log",
            "maxBytes": 5 * 1024 * 1024,  # 5 MB
            "backupCount": 5,
            "level": "INFO",
            # "stream": "ext://sys.stdout"
        },
        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "filename": "cwagent.log",
            "maxBytes": 5 * 1024 * 1024,  # 5 MB
            "backupCount": 3,
            "level": "INFO"
        },
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
        "api_timer": {
            "handlers": ["api_timer", "console"],
            "level": "INFO",
            "propagate": False
        },
        "O-A0001-001": {
            "handlers": ["O-A0001-001"],
            "level": "INFO",
            "propagate": False
        },
        "cwagent": {
            "handlers": ["console", "default"],
            "level": "INFO",
            "propagate": False
        },
        "cwagent.entrypoints.cli": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "tests": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}
