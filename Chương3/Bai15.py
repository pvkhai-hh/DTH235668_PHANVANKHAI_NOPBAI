# range(stop) → bắt đầu từ 0 đến stop-1
(a) = range(5)             # [0, 1, 2, 3, 4]

# range(start, stop) → từ start đến stop-1
(b) = range(5, 10)         # [5, 6, 7, 8, 9]

# range(start, stop, step) → bước nhảy step
(c) = range(5, 20, 3)      # [5, 8, 11, 14, 17]

# bước âm: đếm lùi từ 20 xuống đến >5
(d) = range(20, 5, -1)     # [20, 19, ..., 6]

# bước âm: giảm 3, dừng khi <5
(e) = range(20, 5, -3)     # [20, 17, 14, 11, 8]

# start > stop với step mặc định = +1 → rỗng
(f) = range(10, 5)         # []

# range(0) không có phần tử
(g) = range(0)             # []

# từ 10 đến 100, bước 10
(h) = range(10, 101, 10)   # [10, 20, ..., 100]

# đếm lùi từ 10 đến 0
(i) = range(10, -1, -1)    # [10, 9, ..., 0]

# từ -3 đến 3
(j) = range(-3, 4)         # [-3, -2, -1, 0, 1, 2, 3]

# giống range(10)
(k) = range(0, 10, 1)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]