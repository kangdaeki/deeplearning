import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

X=["월", "화", "수", "목", "금", "토", "일"]
Y1=[15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2=[20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]
plt.plot(X,Y1, label="서울")
plt.plot(X,Y2, label="부산")
plt.xlabel("일 (Day)")
plt.ylabel("온도")
plt.legend(loc="upper left")
plt.title("도시 별 온도")
plt.show()