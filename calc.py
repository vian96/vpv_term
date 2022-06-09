from matplotlib import pyplot as plt


# dp = ro v^2/2 <=> v = sqrt(2 dp/ro)

p0 = -70
ro = 1.2754
coeff_p = 0.1499
cpeff_r = 2*0.0058/100

def get_u_arr(f_name):
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
def calc_file(f_name, begin, dir):
    u_arr =  get_u_arr(name_6cm) [::dir] [begin:]
    plt.plot(u_arr)
    plt.show()
    print(get_q(u_arr))

name_6cm = "jet-data 2022-06-09 14:20:17 6cm.txt"
calc_file(name_6cm, 70, 1)



