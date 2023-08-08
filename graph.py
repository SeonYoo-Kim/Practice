import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/tjdn9/OneDrive/바탕 화면/graph1.csv")
pix = df['Resolution']
x = list(pix)
L1 = df['SUFBNx2_123_SRFBNx2_4']
L2 = df['SUFBNx4_1_x2_3_SRFBNx2_4']
L3 = df['SRFBNx4_12']
L4 = df['SRFBN_1234']
y1 = list(L1)
y2 = list(L2)
y3 = list(L3)
y4 = list(L4)

plt.plot(x, y1, label="SUFBNx2_123_SRFBNx2_4")
plt.plot(x, y2, label="SUFBNx4_1_x2_3_SRFBNx2_4")
plt.plot(x, y3, label="SRFBNx4_12")
plt.plot(x, y4, label="SRFBN_1234")
plt.xlabel("Resolution", fontsize=12)
plt.ylabel("PSNR(dB)", fontsize=12)
plt.title("Analysis of Resoluion", fontsize=16)

# plt.plot(x, y1, label="a")
# plt.plot(x, y2, label="b")
# plt.plot(x, y3, label="c")
# plt.plot(x, y4, label="d")
plt.legend(fontsize=12)
plt.xticks(rotation = 25)

plt.show()