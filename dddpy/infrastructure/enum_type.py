from typing import Type

import sqlalchemy as sa

from regi.utils.enum_meta import OpenapiEnum


class EnumType(sa.types.TypeDecorator):
    """ PythonでのEnum ⇔ DBでのInt を相互接続するためのデコレーター"""
    cache_ok = True

    impl = sa.Integer

    def __init__(self, enum_class: Type[OpenapiEnum], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._enum_class = enum_class

    def process_bind_param(self, value: OpenapiEnum, dialect) -> int:
        if value is not None:
            if not isinstance(value, self._enum_class):
                raise TypeError("Value should %s type" % self._enum_class)
            return value.value

    def process_result_value(self, value: int, dialect):
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("value should have int type")
            return self._enum_class.get(value)

    def process_literal_param(self, value, dialect):
        if value is not None:
            if not isinstance(value, self._enum_class):
                raise TypeError("Value should %s type" % self._enum_class)
            return value.value

    @property
    def python_type(self):
        return self._enum_class

