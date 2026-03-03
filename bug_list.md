# Bug List

## Seeker Writer pattern

```
seeker, writer = 0, 0
while seeker < len(arr):
    if we need to keep arr[seeker]:
        arr[writer] = arr[seeker]
        advance writer and seeker
    else
        advance seeker
```

## Hashmaps

- Hashing algorithms take time, which means if the keys don't have a fixed
maximum length you must incorporate the hashing algorithm in your complexity
analysis

