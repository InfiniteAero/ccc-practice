# CCC '23 S2
import math

n = int(input())
mountains = list(map(int, input().split()))
crop_size = 1
asym_vals = []

while crop_size <= n:
    slice_count = (n - crop_size) + 1
    slice = 0
    while slice < slice_count:
        crop = mountains[slice:crop_size + 1]

        large_asym = -1

        small_slice_count = math.floor(len(crop) / 2)
        small_slice = 0
        while small_slice < small_slice_count:
            asym = abs(crop[small_slice] - crop[-small_slice - 1])
            if large_asym < asym:
                large_asym = asym
            
            small_slice += 1

        slice += 1
    
    asym_vals.append(large_asym)

    crop_size += 1

print(asym_vals)