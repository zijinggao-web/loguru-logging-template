"""
Loguru 日志配置模块

提供统一的日志配置和管理功能，支持控制台和文件输出。
"""
import sys
from pathlib import Path
from loguru import logger


# 移除默认的处理器
logger.remove()

# 配置日志格式
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)

# 添加控制台输出（标准输出）
logger.add(
    sys.stdout,
    format=log_format,
    level="INFO",
    colorize=True,
    backtrace=True,
    diagnose=True,
)

# 创建日志目录
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# 添加文件输出 - 所有日志
logger.add(
    log_dir / "app_{time:YYYY-MM-DD}.log",
    format=log_format,
    level="DEBUG",
    rotation="00:00",  # 每天午夜轮转
    retention="30 days",  # 保留30天
    compression="zip",  # 压缩旧日志
    encoding="utf-8",
    backtrace=True,
    diagnose=True,
)

# 添加文件输出 - 错误日志
logger.add(
    log_dir / "error_{time:YYYY-MM-DD}.log",
    format=log_format,
    level="ERROR",
    rotation="00:00",
    retention="60 days",  # 错误日志保留更长时间
    compression="zip",
    encoding="utf-8",
    backtrace=True,
    diagnose=True,
)

# 导出 logger 供其他模块使用
__all__ = ["logger"]
