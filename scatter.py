import random
import csv

# 0~1000の範囲で300個のランダムな座標を生成
coordinates = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(300)]

# CSVファイルに保存
with open('coordinates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])  # ヘッダーを書き込み
    writer.writerows(coordinates)  # 座標を書き込み

print("Coordinates saved to coordinates.csv")
