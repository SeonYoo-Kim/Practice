import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'sans-serif'  # 사용할 글꼴의 패밀리 설정
plt.rcParams['font.sans-serif'] = 'times new roman'   # 사용할 실제 글꼴 이름 설정
#df = pd.read_csv("C:/Users/tjdn9/OneDrive/바탕 화면/fig4.csv")
df = pd.read_csv("C:/Users/tjdn9/OneDrive/바탕 화면/graph1.csv")
#pix = df['opacity']
pix = df['Resolution']
x = list(pix)
L1 = df['SUFBNx2_123_SRFBNx2_4']
L2 = df['SUFBNx4_1_x2_3_SRFBNx2_4']
L3 = df['SRFBNx4_12']
L4 = df['SRFBN_1234']
# L5 = df['HAT']
# L6 = df['DRN']
y1 = list(L1)
y2 = list(L2)
y3 = list(L3)
y4 = list(L4)
# y5 = list(L5)
# y6 = list(L6)

plt.plot(x, y1, label="Exp.1")
plt.plot(x, y2, label="Exp.2")
plt.plot(x, y3, label="Exp.3")
plt.plot(x, y4, label="Exp.4")
# plt.plot(x, y5, label="HAT")
# plt.plot(x, y6, label="DRN")
plt.xlabel("Resolution", fontsize=20)
plt.ylabel("PSNR(dB)", fontsize=20)
#plt.title("Analysis of Resoluion", fontsize=16)

# plt.plot(x, y1, label="a")
# plt.plot(x, y2, label="b")
# plt.plot(x, y3, label="c")
# plt.plot(x, y4, label="d")
plt.grid(True)
plt.legend(fontsize=16)
#plt.xticks(rotation = 25)

plt.show()