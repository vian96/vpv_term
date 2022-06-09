from matplotlib import pyplot as plt
import numpy as np

# dp = ro v^2/2 <=> v = sqrt(2 dp/ro)

ro = 1.2754
coeff_p = 0.1499
coeff_r = 2*0.0058/100

def get_u_arr(f_name, p0):
    with open(f_name, 'r') as f_read:
        s = [int(i)-p0 for i in f_read.read().split('\n')[3:-1]]
        s = [i if i > 0 else 0 for i in s]

    return [(2*p/ro)**0.5 for p in s]

# int(2pi u r dr)
def get_q(u_arr, r0):
    sum = 0 
    for r in range(len(u_arr)):
        sum += abs(r-r0) * coeff_r**2 * u_arr[r]

    return sum*3.1416

# f_name - name of file
# r0 - r of center
# p0 - p of zero
def calc_file(f_name, r0, p0, name):
    print(f"{name}: ", end='')
    u_arr =  get_u_arr(f_name, p0)

    r_arr = np.arange(len(u_arr)) * coeff_r * 100

    fig, ax = plt.subplots(figsize = (16,10), dpi = 200)
    
    ax.set_ylim(0, 1.1 * max(u_arr))
    ax.set_xlim(0, 1.1 * len(u_arr) * coeff_r * 100)

    ax.set_xlabel("Координата, см")
    ax.set_ylabel("Скорость, м/с")
    plt.title("Зависимость скорости от координаты", wrap = True)

    ax.minorticks_on()
    ax.grid(True)
    ax.grid(True, 'minor', ls=':')
    ax.plot(r_arr, u_arr, color = 'b', alpha = 0.5, label = "v(x)")
    plt.legend(fontsize = 'x-large')
    fig.savefig(f"{name}_graph.png")

    # plt.plot(u_arr)
    plt.show()
    print(get_q(u_arr, r0) * 1000, "g/c")

name_0cm = "jet-data 2022-06-09 0 cm 14_02_29.txt"
calc_file(name_0cm, 52, -69, "0cm")

name_3cm = "jet-data 2022-06-09 3 cm13_57_26.txt"
calc_file(name_3cm, 109, -65, "3cm")

exit()

name_6cm = "jet-data 2022-06-09 14_20_17 6cm.txt"
calc_file(name_6cm, 131, -70, "6cm")

name_sprite = "jet-data 2022-06-09 14_19_33 sprite2.txt"
calc_file(name_sprite, 107, -76, "sprite")

name_shw = "jet-data 2022-06-09 shweps16_51_25.txt"
calc_file(name_shw, 113, -71, "shweps")

name_kvas = "jet-data 2022-06-09 KVAS 17_03_07.txt"
calc_file(name_kvas, 110, -68, "kvas")

name_baklashka = "jet-data 2022-06-09 17_14_46 norm_bakl.txt"
calc_file(name_baklashka, 126, -72, "baklashka")

name_cut = "jet-data 2022-06-09 17_24_01 cut_bakl.txt"
calc_file(name_cut, 148, -69, "cut baklashka")

