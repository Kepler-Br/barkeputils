from typing import TypeVar, Collection, List

_T = TypeVar("_T")


class RoundRobinArray:
    def __init__(self, collection: Collection[_T]):
        if len(collection) == 0:
            raise RuntimeError('collection cannot be 0 length')
        self.collection: List = list(collection)
        self.set_collection = set(self.collection)
        self.idx = 0

    def get(self) -> _T:
        out = self.collection[self.idx]
        self.idx = (self.idx + 1) % len(self.collection)

        return out

    def discard(self, value: _T):
        if value in self.set_collection:
            self.set_collection.discard(value)
            self.collection = list(self.set_collection)
            if len(self.collection) == 0:
                raise RuntimeError('No elements left')
            self.idx = 0

    def __len__(self) -> int:
        return len(self.collection)
