"""
logger config file
"""
import os
import logging


class Log:
    """
    logging instance
    """

    @classmethod
    def base_config(cls, level=logging.INFO):
        """
        setup config for logger if verbose set to debug
        :param name:
        :param level:
        """
        logPath = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "log")
        fileName = "log"
        fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))

        logging.basicConfig(
            level=level,
            format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
            handlers=[logging.StreamHandler(), fileHandler,],
        )
