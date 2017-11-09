import logging,logging.handlers

def WriteLog(log_name):
    log_filename = "/tmp/test.log"
    log_level = logging.DEBUG
    format = logging.Formatter('%(asctime)s %(filename)s - [line:%(lineno)2d] - %(funcName)s  %(levelname)s - %(name)s %(message)s')
    handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(format)
    logger = logging.getLogger(log_name)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger

