# loguru-logging-template

基于 Loguru 的 Python 日志配置模板项目。

## 功能特性

- ✅ 统一的日志格式配置
- ✅ 控制台彩色输出
- ✅ 文件日志自动轮转（按天）
- ✅ 错误日志单独记录
- ✅ 自动压缩和清理旧日志
- ✅ 完整的异常堆栈跟踪

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本使用

```python
from core.logger import logger

logger.info("这是一条信息日志")
logger.debug("调试信息")
logger.warning("警告信息")
logger.error("错误信息")
logger.success("成功信息")
```

### 异常记录

```python
try:
    # 你的代码
    pass
except Exception as e:
    logger.exception("捕获到异常")
```

### 结构化日志

```python
logger.bind(user_id=123, action="login").info("用户登录")
```

## 日志配置

日志配置位于 `core/logger.py`，包含以下特性：

- **控制台输出**: 彩色日志，INFO 级别及以上
- **文件输出**: 
  - `logs/app_YYYY-MM-DD.log`: 所有日志（DEBUG 级别及以上）
  - `logs/error_YYYY-MM-DD.log`: 仅错误日志（ERROR 级别及以上）
- **日志轮转**: 每天午夜自动轮转
- **日志保留**: 
  - 普通日志保留 30 天
  - 错误日志保留 60 天
- **自动压缩**: 旧日志自动压缩为 zip 格式

## 运行测试

```bash
python main.py
```

运行后会在控制台看到彩色日志输出，同时在 `logs/` 目录下生成日志文件。

## 日志格式

```
YYYY-MM-DD HH:mm:ss.SSS | LEVEL    | name:function:line | message
```

## 项目结构

```
.
├── core/
│   └── logger.py      # 日志配置模块
├── main.py            # 主程序（包含测试示例）
├── requirements.txt   # 项目依赖
└── README.md         # 项目说明
```
