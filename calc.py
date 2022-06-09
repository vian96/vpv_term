from matplotlib import pyplot as plt


# dp = ro v^2/2 <=> v = sqrt(2 dp/ro)

ro = 1.2754
coeff_p = 0.1499
cpeff_r = 2*0.0058/100

def get_u_arr(f_name, p0):
    with open(f_name, 'r') as f_read:
        s = [int(i)-p0 for i in f_read.read().split('\n')[3:-1]]
        s = [i if i > 0 else 0 for i in s]

    return [(2*p/ro)**0.5 for p in s]

# int(2pi u r dr)
def get_q(u_arr):
    if len(u_arr)%2 == 0:
        u_arr.append(0)

    r0 = len(u_arr)//2
    sum = 0 
    for r in range(0, r0):
        sum += r * cpeff_r**2 * (u_arr[r0+r] + u_arr[r0-r])

    return sum*3.1416

# f_name - name of file
# begin - offset 
# dir - 1 or -1, showing direction of tube
def calc_file(f_name, begin, dir, p0):
    u_arr =  get_u_arr(f_name, p0) [::dir] [begin:]
    plt.plot(u_arr)
    plt.show()
    print(get_q(u_arr))

name_6cm = "jet-data 2022-06-09 14:20:17 6cm.txt"
#calc_file(name_6cm, 70, 1, -70)

name_sprite = "jet-data 2022-06-09 14:19:33 sprite2.txt"
#calc_file(name_sprite, 50, -1, -74)

name_0cm = "jet-data 2022-06-09 0 cm 14:02:29.txt"
#calc_file(name_0cm, 105, 1, -69)

name_0cm = "jet-data 2022-06-09 shweps16:51:25.txt"
 #calc_file(name_0cm, 40, -1, -69)

name_0cm = "jet-data 2022-06-09 KVAS 17:03:07.txt"
#calc_file(name_0cm, 15, -1, -69)

name_baklashka = "jet-data 2022-06-09 17:14:46 norm_bakl.txt"
calc_file(name_baklashka, 15, -1, -75)

name_cut = "jet-data 2022-06-09 17:24:01 cut_bakl.txt"
calc_file(name_cut, 70, 1, -69)

