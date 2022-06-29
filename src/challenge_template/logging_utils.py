import importlib
import logging


def get_jupyter_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """creates a logger object for jupyter notebooks using basic config

    Basic logger doesn't play nice with Jupyter

    This wrapper fixes the logging startup configuration in iPython/Jupyter
    See: https://stackoverflow.com/a/21475297

    Parameters
    ----------
    name : str
        name of the logger
    level : int, optional
        logger level, by default logging.INFO
    Returns
    -------
    logging.Logger
        logger object set for Jupyter notebooks
    """
    importlib.reload(logging)
    logging.basicConfig(level=level)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger
