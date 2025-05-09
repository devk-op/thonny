from typing import Generic, Iterable, MutableSequence, TypeVar, Union, overload

from typing_extensions import Literal

_IntTypeCode = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
_FloatTypeCode = Literal["f", "d"]
_TypeCode = Union[_IntTypeCode, _FloatTypeCode]

_T = TypeVar("_T", int, float)

class array(MutableSequence[_T], Generic[_T]):
    @overload
    def __init__(
        self: array[int],
        typecode: _IntTypeCode,
        __initializer: Union[bytes, Iterable[_T]] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: array[float],
        typecode: _FloatTypeCode,
        __initializer: Union[bytes, Iterable[_T]] = ...,
    ) -> None: ...
    @overload
    def __init__(self, typecode: str, __initializer: Union[bytes, Iterable[_T]] = ...) -> None: ...
    def append(self, __v: _T) -> None: ...
    def decode(self) -> str: ...
    def extend(self, __bb: Iterable[_T]) -> None: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, i: int) -> _T: ...
    @overload
    def __getitem__(self, s: slice) -> array[_T]: ...
    @overload  # type: ignore  # Overrides MutableSequence
    def __setitem__(self, i: int, o: _T) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: array[_T]) -> None: ...
    def __add__(self, x: array[_T]) -> array[_T]: ...
    def __iadd__(self, x: array[_T]) -> array[_T]: ...  # type: ignore  # Overrides MutableSequence

ArrayType = array
