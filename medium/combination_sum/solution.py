from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def _combinations(acc, t):
            result = []
            for candidate in candidates:
                if t < candidate: break
                if not acc or candidate >= acc[-1]:
                    if t > candidate:
                        res = _combinations(acc + [candidate], t - candidate)
                        for r in res:
                            result.append(r)
                    elif t == candidate:
                        result.append(acc + [candidate])

            return result

        candidates.sort()
        return _combinations([], target)


if __name__ == '__main__':
    s = Solution()
    assert set(tuple(i) for i in s.combinationSum([2, 3, 6, 7], 7)) == {(7,), (2, 2, 3)}
    assert set(tuple(i) for i in s.combinationSum([2, 3, 5], 8)) == {(2, 2, 2, 2), (2, 3, 3), (3, 5)}
