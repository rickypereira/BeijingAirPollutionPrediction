import time
import logging


class Timer(object):

    def __init__(self, logger, message, level=logging.INFO):
        """Context timer

        with Timer(mylogger, 'downloading 4000 files from bucket'):
            do_long_download()


        Will log 'Started downloading 4000 files from bucket' on start of block
        And 'Finished downloading 4000 files from bucket in xyz.qtz seconds'
        at end. If an exception is raised, it will reraise it

        Parameters
        ----------
        logger : logging.Logger
            Logger to use
        message : str
            Message to use at start and end
        level : int, optional
            Log level (the default is logging.INFO)
        """
        self.logger = logger
        self.raw_message = message
        self.level = level

    def __enter__(self):
        self.start = time.perf_counter()
        self.logger.log(self.level, 'Started %s', self.raw_message)

    def __exit__(self, exception_type, exception_value, traceback_val):
        elapsed = time.perf_counter() - self.start
        if exception_type:
            raise exception_value
        self.logger.log(self.level, 'Finished %s in %.2f seconds.',
                        self.raw_message, elapsed)
        return True
