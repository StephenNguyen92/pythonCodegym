usd = float(input("Nhập số tiền usd: "))
rate = float(input("Nhập tỷ giá chênh lệch với Việt Nam đồng: "))
vnd = usd * rate
print("Giá trị của {usd} usd là {vnd} Việt Nam đồng".format(usd = usd,vnd = vnd))