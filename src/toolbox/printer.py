import logging.config
import os


LOGGER_CONFIG = {
    "version": 1,
    "formatters": {
        "json": {
            "format": "{asctime: %(asctime)s, %(name)s, levelname: %(levelname)s, message: %(message)s}",
        }
    },
    "handlers": {
        "htest": {
            "class": "logging.FileHandler",
            # "stream": "ext://sys.stdout",
            "formatter": "json",
            "filename": f"{os.environ.get('USERPROFILE')}/test.log",
        }
    },
    "loggers": {"": {"handlers": ["htest"], "level": "DEBUG"}},
}


logging.config.dictConfig(LOGGER_CONFIG)