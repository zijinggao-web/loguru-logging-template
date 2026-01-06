"""
主程序入口 - 日志测试示例
"""
from core.logger import logger


def test_basic_logging():
    """测试基础日志功能"""
    logger.info("这是一条信息日志")
    logger.debug("这是一条调试日志")
    logger.warning("这是一条警告日志")
    logger.error("这是一条错误日志")
    logger.success("这是一条成功日志")


def test_logging_with_context():
    """测试带上下文的日志"""
    user_id = 12345
    action = "登录"
    logger.info(f"用户 {user_id} 执行了 {action} 操作")


def test_exception_logging():
    """测试异常日志记录"""
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.exception("捕获到除零错误")
        logger.error(f"错误详情: {e}")


def test_structured_logging():
    """测试结构化日志"""
    logger.bind(user_id=12345, action="purchase").info("用户执行了购买操作")
    logger.bind(ip="192.168.1.1", status_code=200).info("API 请求成功")


def main():
    """主函数"""
    logger.info("=" * 50)
    logger.info("开始日志测试")
    logger.info("=" * 50)
    
    # 基础日志测试
    logger.info("测试 1: 基础日志级别")
    test_basic_logging()
    
    logger.info("")
    logger.info("测试 2: 带上下文的日志")
    test_logging_with_context()
    
    logger.info("")
    logger.info("测试 3: 异常日志记录")
    test_exception_logging()
    
    logger.info("")
    logger.info("测试 4: 结构化日志")
    test_structured_logging()
    
    logger.info("")
    logger.info("=" * 50)
    logger.success("所有日志测试完成！")
    logger.info("=" * 50)
    logger.info(f"日志文件保存在 logs/ 目录下")


if __name__ == "__main__":
    main()
