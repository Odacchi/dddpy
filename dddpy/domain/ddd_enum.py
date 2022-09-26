import enum
from abc import ABCMeta
from enum import Enum
from typing import List, Type, TypeVar, Dict

T = TypeVar('T', bound='DddEnum')


class DddEnum(Enum):
    """IntEnum

    TODO presentation層かも

    """

    def __new__(cls, value: int, display_name: str) -> T:
        if type(value) is not int:
            raise ValueError(f'value must be int. {value=}')
        if type(display_name) is not str:
            raise ValueError(f'display_name must be str. {display_name=}')

        obj: T = object.__new__(cls)
        obj._value_ = value
        obj.__display_name = display_name
        return obj

    @classmethod
    def __modify_schema__(cls, field_schema: Dict):
        """OpenApi用"""
        keynames = [member.name for member in cls.members()]
        field_schema.update(
            {'x-enum-varnames': keynames}
        )

    @classmethod
    def members(cls: Type[T]) -> List[T]:
        """
        全メンバーを取得する。
        """
        return [*cls.__members__.values()]

    @property
    def display_name(self) -> str:
        return self.__display_name

    @classmethod
    def get(cls: Type[T], value: int) -> T:
        for c in cls.members():
            if value == c.value:
                return c

        raise ValueError(f'{cls.__name__} {value=} is invalid value')
