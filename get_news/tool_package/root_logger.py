import logging
root_logger = logging.getLogger('root')
# 清除原有的处理器配置
for handler in root_logger.handlers[:]:
    root_logger.removeHandler(handler)
# 配置日志
root_logger.setLevel(logging.INFO)
#创建格式化器,准备被日志处理器使用
formatter = logging.Formatter(
    fmt='[%(name)s][%(levelname)s][%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# 创建文件处理器，将日志写入 working.log 文件，写入模式为追加，编码使用utf-8
file_handler = logging.FileHandler('./working.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)
# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)
