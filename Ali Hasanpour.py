import matplotlib.pyplot as plt
import numpy as np
#----------variables----------
n = int(input("how many sumation of fourier series in the function required? :"))
a = -1 * np.pi
b = np.pi
#----------create fourier series of f(x) value function----------
def sigma(n, x) :
    s = []
    for i in range(1, n+1) :
        s.append((((4)/((np.pi)))*((np.sin((2*i - 1)*(x)))/(2*i - 1))))
    return sum(s)
#----------plot the function----------
label = ""
if n == 1 :
    label = "1st"
elif n== 2 :
    label = "2nd"
else :
    label = "{}th".format(n)
x = np.linspace(a, b, 500)
y = sigma(n,x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, linestyle=':')
ax.tick_params(labelcolor='#112233', labelsize='medium', width=1)
plt.plot(x,y,"#dd2211", label="n = {}".format(n))
plt.title(label="its diagram for {} sumation of fourier series for the function is requested".format(label))
plt.legend()
plt.show()
