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