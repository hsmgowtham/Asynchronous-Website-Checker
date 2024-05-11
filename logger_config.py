import logging

def get_logger(logger_name):
    # Set up logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Create file handler
    handler = logging.FileHandler('site_status.log')
    handler.setLevel(logging.INFO)

    # Create console handler
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(handler)
    logger.addHandler(console)

    return logger
