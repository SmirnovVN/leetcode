from bisect import bisect_right
from collections import defaultdict


class SnapshotArray:

    def __init__(self, length: int):
        self.last_updated = [[0] for _ in range(length)]
        self.snap_id = 0
        self.increment = defaultdict(dict)

    def set(self, index: int, val: int) -> None:
        self.increment[self.snap_id][index] = val
        self.last_updated[index].append(self.snap_id)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_right(self.last_updated[index], snap_id)
        snap_id = self.last_updated[index][i - 1]
        if index in self.increment[snap_id]:
            return self.increment[snap_id][index]

        return 0


if __name__ == '__main__':
    s = SnapshotArray(1)
    print(s.snap())
    print(s.snap())
    print(s.set(0, 4))
    print(s.snap())
    print(s.get(0, 1))
    print(s.set(0, 12))
    print(s.get(0, 1))
    print(s.snap())
    print(s.get(0, 3))
