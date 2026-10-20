total_time = (int(input()) * 60 + int(input()) + int(input())) % 1440
print(f"{total_time // 60:0>2}:{total_time % 60:0>2}")