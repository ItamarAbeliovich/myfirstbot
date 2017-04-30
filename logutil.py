import logging

def get_logger(name, log_file=None, stream_level=logging.DEBUG, file_level=logging.DEBUG):
    """
    :param name: Logger name
    :param log_file: Optional - File path for log storage
    :param stream_level: Logging level for console logging
    :param file_level: Logging level for file logging
    :return: Logger instance with the specified settings
    """

    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add console handler
    ch = logging.StreamHandler()
    ch.setLevel(stream_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if log_file:
        # Add file handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(file_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger