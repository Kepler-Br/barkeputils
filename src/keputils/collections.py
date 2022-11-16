from typing import List, TypeVar

_T = TypeVar("_T")


class RoundRobinArray:
    def __init__(self, collection: List[_T]):
        self.collection = collection
        self.set_collection = set(self.collection)
        self.idx = 0

    def get(self) -> _T:
        self.idx += 1
        return self.collection[self.idx % len(self.collection)]

    def discard(self, value: _T):
        if value in self.set_collection:
            self.set_collection.discard(value)
            self.collection = list(self.set_collection)
            if len(self.collection) == 0:
                raise RuntimeError('No elements left')
            self.idx = 0

    def __len__(self) -> int:
        return len(self.collection)
