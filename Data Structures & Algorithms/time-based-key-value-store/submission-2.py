class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:

        bucket = self.store[key]
        result = ""

        l, r = 0, len(bucket) - 1

        while l <= r:
            mid = (l + r) // 2

            store_val, store_timestamp = bucket[mid]

            if store_timestamp <= timestamp:
                l = mid + 1
                result = store_val
            else:
                r = mid - 1
        
        return result
        
