import os
import numpy as np

src = 'D:/Ku/2.0/2.10/duLieu'
# 1. Lấy danh sách tên file
fileS_List = os.listdir(src) 
# 2. Kiểm tra file Profit.txt có tồn tại không và xoá nó để chuẩn bị ghi thông tin
if os.path.exists("Profit.txt"):
    os.remove("Profit.txt")
tongTien = 0  # Tính tổng tiền trong tháng

# 3. Hàm tính toán trả về list các số để chơi
def tinhSo(motTramSo):
    mang = np.array([x for x in range(100)])
    count = np.zeros(100, dtype=int)
    for y in range(100):
        count[y] = motTramSo.count(y)
    for a in range(100):
        for b in range(0, a):
            if count[a] < count[b]:
                temp = count[b]
                count[b] = count[a]
                count[a] = temp
                temp = mang[b]
                mang[b] = mang[a]
                mang[a] = temp
    goiY = sorted(mang[17:82])
    return goiY

# 4. Duyệt từng ngày trong list file dữ liệu
for day in fileS_List:
    # 4.1. Tách lấy ngày đang duyệt
    toDay = day.split(".")
    toDay = toDay[0]

    # 4.2. Khai báo các biến cần thiết
    motTramSo = []
    # mang = np.array([x for x in range(100)])
    # count = np.zeros(100, dtype=int)
    danhSach = [] # Chứa các giải đặc biệt
    ketQua = [] # Lưu kết quả một ngày chơi
    luotDanh = 0 # Lưu số lần chơi
    time = 0.0
    profit = 0
    maxProfit = 0
    timeMaxProfit = 0
    minProfit = 0
    timeMinProfit = 0
    phut120 = 0
    phut280 = 0
    heSo = 1
    maxHeSo = 1
    timeHeSo = 0

    # 4.3. Mở file ngày hôm nay ra để chơi
    read = open(src + '/' + day, 'r')
    # 4.4. Tạo file ttNgay để lưu lại kết quả của ngày
    ghittngay = open('D:/Ku/2.0/2.10/ketqua/' + 'ttNgay' + toDay + '.txt', 'w')
    # 4.5. Duyệt qua từng số trong danh sách giải đặc biệt
    for x in range(960): # Một ngày quay 960 giải đặc biệt
        so = int(read.readline())
        luotDanh += 1

        # 4.5.1 Sử dụng 100 giải đầu tiên để Training
        if luotDanh <= 100:
            motTramSo.append(so)
        # 4.5.2 Sau khi có 100 số để training rồi bắt đầu chơi
        if luotDanh > 100:
            goiY = tinhSo(motTramSo)
            ghittngay.write(str(goiY))
            ghittngay.write("\nSo tiep theo la: "+ str(so))
            motTramSo.pop(0)
            motTramSo.append(so)

            # Chiến thuật chơi
            if heSo > 81:
                ghittngay.write("\nRefresh lai he so = 1")
                heSo = 1
            if goiY.count(so) > 0:
                profit += 33 * heSo
                ketQua.append('0') 
                ghittngay.write("\nHe so la: " + str(heSo))
                heSo = 1
            else:
                profit -= 65 * heSo
                ketQua.append('x')
                ghittngay.write("\nHe so la: " + str(heSo))
                heSo *= 3
            
            # Lưu lại kết quả của ngày
            ghittngay.write("\nket qua: " + str(ketQua))
            ghittngay.write("\nTien lai: " + str(profit))
            time += 90.0
            ghittngay.write("\nDa choi duoc: "+ str(time/60) + " phut" + "\n---------------------------------------------------\n")
        
        # 4.5.3. Lấy các mốc đặc biệt, dừng khi chơi được 280 phút một ngày
        if profit > maxProfit:
            maxProfit = profit
            timeMaxProfit = time / 60
        else:
            if profit < minProfit:
                minProfit = profit
                timeMinProfit = time / 60
        if (time / 60) == 120:
            phut120 = profit
        if (time / 60) > 280:
            phut280 = profit
            break

    read.close()
    ghittngay.close()

    # 4.6. Tổng hợp các ngày trong tháng ra file Profit.txt
    tongTien += profit
    ghi = open("Profit.txt", 'a')
    ghi.write("\n______________________________________________________")
    ghi.write("\nTien lai: " + str(profit))
    ghi.write("\nNgay: " + str(toDay))
    ghi.write("\nMax: " + str(maxProfit) + " Time: " + str(timeMaxProfit) + " Phut")
    ghi.write("\nMin: " + str(minProfit) + " Time: " + str(timeMinProfit) + " Phut")
    ghi.write("\n120p: " + str(phut120) + "          280p: " + str(phut280))
    ghi.close()

ghi = open("Profit.txt", 'a')
ghi.write("\n\nTong tien: " + str(tongTien))
ghi.close()
print("Dừng chương trình !!")