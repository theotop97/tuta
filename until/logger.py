import logging
import os

log_path = os.path.abspath(".") + r"/logs/"


class Logger:
    def __init__(self, loggerName, logName: str):
        # 创建一个logger
        self.logger = logging.getLogger(loggerName)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        logname = log_path + r'/' + logName
        fh = logging.FileHandler(logname, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger

# if __name__ == '__main__':
#     t = Logger("hmk").get_log().debug("User %s is loging" % 'jeck')