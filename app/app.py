import logging, os, sys

def main():
    pass

def resource_path(relative_path):
    """returns absolute path for source and binary

    :param relative_path: path relative to main file(?)
    :type relative_path: str
    :return: absolute path
    :rtype: str
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    # make logger
    logger = logging.Logger(__name__)
    logger.setLevel(logging.DEBUG)
    # make formatter
    formatter = logging.Formatter("(%(asctime)s) %(name)s @ %(lineno)d [%(levelname)s]: %(message)s")
    # make stream handler
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    # file handler
    fileHandler = logging.FileHandler(resource_path("log.log"))
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    # done!
    logger.debug("pre-initialization complete")
    main()