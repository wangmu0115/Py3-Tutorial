class MyContextManager:
    def __enter__(self):
        """进入 `with` 语句时调用，返回资源对象。
        返回的资源对象可以被绑定到 `as` 子句中的目标变量上。
        """

    def __exit__(self, exc_type, exc_value, traceback):
        """退出 `with` 语句时调用，执行清理。

        Args:
            exc_type: 异常类，例如 `ZeroDivisionError`
            exc_value: 异常实例
            traceback: traceback 对象

        Returns:
            如果返回 `True`，即使 `exc_type` 不为空也表示异常被正常处理；
            如果返回 `None` 或其他假值，则当 `exc_type` 不为空时，异常会向上冒泡。
        """
