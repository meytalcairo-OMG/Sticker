from utils.logger import get_logger


class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.logger = get_logger(name)

    def log(self, message: str) -> None:
        self.logger.info(message)

    def run(self, *args, **kwargs):
        # כל סוכן ירשת ויממש את run() בעצמו
        raise NotImplementedError("run() must be implemented by subclasses")
