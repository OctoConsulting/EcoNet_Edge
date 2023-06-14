import logging
import logging.config


def configure_logger(name, logger="baseLogger"):
    """
    @param name: name of the logger to be created. Can be an absolute path with the name
    @param logger: optional - select specific logger class
    @return: a logger outputting to the name file
    """
    config = {
        "version": 1,
        "formatters": {
            "simple": {
                "format": '%(asctime)s-%(levelname)s - %(message)s',
                "datefmt": '%Y-%m-%d %H:%M:%S',
            },
            "error": {
                "format": "%(asctime)s-%(levelname)s-%(module)s-%(thread)d %(message)s",
                "datefmt": '%Y-%m-%d %H:%M:%S'
            }
         },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "ERROR",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },

            "file_debug": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": name+".log"
             },

            "file_error": {
                "class": "logging.FileHandler",
                "level": "ERROR",
                "formatter": "error",
                "filename": name+".error.log"
            },
        },
        "loggers": {
            "baseLogger": {
                 "level": "DEBUG",
                 "handlers": ["file_debug", "file_error"],
                 "propagate": "yes"
            },
            "errorLogger": {
                 "level": "ERROR",
                 "handlers": ["file_error"],
                 "propagate": "no"
            },
            "root":
                {
                 "level": "DEBUG",
                 "handlers": ["console"]
                }
        }
    }
    logging.config.dictConfig(config)
    return logging.getLogger(logger)
