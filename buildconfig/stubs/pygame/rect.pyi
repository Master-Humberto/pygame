from collections.abc import Collection
from typing import Any, Dict, Iterator, List, Sequence, Tuple, TypeVar, Union, overload

from ._common import Coordinate, Literal, RectValue

_K = TypeVar("_K")
_V = TypeVar("_V")

# Rect confirms to the Collection ABC, since it also confirms to
# Sized, Iterable and Container ABCs
class Rect(Collection):
    x: int
    y: int
    top: int
    left: int
    bottom: int
    right: int
    topleft: Tuple[int, int]
    bottomleft: Tuple[int, int]
    topright: Tuple[int, int]
    bottomright: Tuple[int, int]
    midtop: Tuple[int, int]
    midleft: Tuple[int, int]
    midbottom: Tuple[int, int]
    midright: Tuple[int, int]
    center: Tuple[int, int]
    centerx: int
    centery: int
    size: Tuple[int, int]
    width: int
    height: int
    w: int
    h: int
    __hash__: None  # type: ignore
    __safe_for_unpickling__: Literal[True]
    @overload
    def __init__(
        self, left: float, top: float, width: float, height: float
    ) -> None: ...
    @overload
    def __init__(self, left_top: Coordinate, width_height: Coordinate) -> None: ...
    @overload
    def __init__(self, single_arg: RectValue) -> None: ...
    def __len__(self) -> Literal[4]: ...
    def __iter__(self) -> Iterator[int]: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, s: slice) -> List[int]: ...
    @overload
    def __setitem__(self, key: int, value: int) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Union[int, Rect]) -> None: ...
    def __copy__(self) -> Rect: ...
    copy = __copy__
    @overload
    def move(self, x: float, y: float) -> Rect: ...
    @overload
    def move(self, move_by: Coordinate) -> Rect: ...
    @overload
    def move_ip(self, x: float, y: float) -> None: ...
    @overload
    def move_ip(self, move_by: Coordinate) -> None: ...
    @overload
    def inflate(self, x: float, y: float) -> Rect: ...
    @overload
    def inflate(self, inflate_by: Coordinate) -> Rect: ...
    @overload
    def inflate_ip(self, x: float, y: float) -> None: ...
    @overload
    def inflate_ip(self, inflate_by: Coordinate) -> None: ...
    @overload
    def update(self, left: float, top: float, width: float, height: float) -> None: ...
    @overload
    def update(self, left_top: Coordinate, width_height: Coordinate) -> None: ...
    @overload
    def update(self, single_arg: RectValue) -> None: ...
    @overload
    def clamp(self, rect: RectValue) -> Rect: ...
    @overload
    def clamp(self, left_top: Coordinate, width_height: Coordinate) -> Rect: ...
    @overload
    def clamp(self, left: float, top: float, width: float, height: float) -> Rect: ...
    @overload
    def clamp_ip(self, rect: RectValue) -> None: ...
    @overload
    def clamp_ip(self, left_top: Coordinate, width_height: Coordinate) -> None: ...
    @overload
    def clamp_ip(
        self, left: float, top: float, width: float, height: float
    ) -> None: ...
    @overload
    def clip(self, rect: RectValue) -> Rect: ...
    @overload
    def clip(self, left_top: Coordinate, width_height: Coordinate) -> Rect: ...
    @overload
    def clip(self, left: float, top: float, width: float, height: float) -> Rect: ...
    @overload
    def clipline(
        self, x1: float, x2: float, x3: float, x4: float
    ) -> Union[Tuple[Tuple[int, int], Tuple[int, int]], Tuple[()]]: ...
    @overload
    def clipline(
        self, first_coordinate: Coordinate, second_coordinate: Coordinate
    ) -> Union[Tuple[Tuple[int, int], Tuple[int, int]], Tuple[()]]: ...
    @overload
    def clipline(
        self, rect_arg: RectValue
    ) -> Union[Tuple[Tuple[int, int], Tuple[int, int]], Tuple[()]]: ...
    @overload
    def union(self, rect: RectValue) -> Rect: ...
    @overload
    def union(self, left_top: Coordinate, width_height: Coordinate) -> Rect: ...
    @overload
    def union(self, left: float, top: float, width: float, height: float) -> Rect: ...
    @overload
    def union_ip(self, rect: RectValue) -> None: ...
    @overload
    def union_ip(self, left_top: Coordinate, width_height: Coordinate) -> None: ...
    @overload
    def union_ip(
        self, left: float, top: float, width: float, height: float
    ) -> None: ...
    def unionall(self, rect: Sequence[RectValue]) -> Rect: ...
    def unionall_ip(self, rect_sequence: Sequence[RectValue]) -> None: ...
    @overload
    def fit(self, rect: RectValue) -> Rect: ...
    @overload
    def fit(self, left_top: Coordinate, width_height: Coordinate) -> Rect: ...
    @overload
    def fit(self, left: float, top: float, width: float, height: float) -> Rect: ...
    def normalize(self) -> None: ...
    def __contains__(self, rect: Any) -> bool: ...
    @overload
    def contains(self, rect: RectValue) -> bool: ...
    @overload
    def contains(self, left_top: Coordinate, width_height: Coordinate) -> bool: ...
    @overload
    def contains(
        self, left: float, top: float, width: float, height: float
    ) -> bool: ...
    @overload
    def collidepoint(self, x: float, y: float) -> bool: ...
    @overload
    def collidepoint(self, x_y: Coordinate) -> bool: ...
    @overload
    def colliderect(self, rect: RectValue) -> bool: ...
    @overload
    def colliderect(self, left_top: Coordinate, width_height: Coordinate) -> bool: ...
    @overload
    def colliderect(
        self, left: float, top: float, width: float, height: float
    ) -> bool: ...
    def collidelist(self, rect_list: Sequence[RectValue]) -> int: ...
    def collidelistall(self, rect_list: Sequence[RectValue]) -> List[int]: ...
    # Also undocumented: the dict collision methods take a 'values' argument
    # that defaults to False. If it is False, the keys in rect_dict must be
    # Rect-like; otherwise, the values must be Rects.
    @overload
    def collidedict(
        self, rect_dict: Dict[RectValue, _V], values: bool = ...
    ) -> Tuple[RectValue, _V]: ...
    @overload
    def collidedict(
        self, rect_dict: Dict[_K, "Rect"], values: bool
    ) -> Tuple[_K, "Rect"]: ...
    @overload
    def collidedictall(
        self, rect_dict: Dict[RectValue, _V], values: bool = ...
    ) -> List[Tuple[RectValue, _V]]: ...
    @overload
    def collidedictall(
        self, rect_dict: Dict[_K, "Rect"], values: bool
    ) -> List[Tuple[_K, "Rect"]]: ...
