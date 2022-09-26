from dddpy.domain.ddd_enum import DddEnum


class Status(DddEnum):
    """
    本のステータス
    """

    NEW = (1, '新品')
    """新品"""

    USED = (2, '中古')
    """中古"""
