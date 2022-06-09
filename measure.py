import jetFunctions as jet

from matplotlib import pyplot as plt

p0 = 883 
coeff_p = 0.1499
coeff_len = 0.0058 # len of step of dvigatel in cm
step_len = 2*coeff_len # len of step of measure in cm
len = 5 # full movement in cm
steps = int(len/step_len)

jet.initSpiAdc()
jet.initStepMotorGpio()

s = input("Move forward or backward?")

try:
    samples = []

    for i in range(steps):
        data = jet.getMeanAdc(500) - p0
        samples.append(data)
        if s[0] == "f":
            jet.stepForward(2)
        else:
            jet.stepBackward(2)

    plt.plot(samples)
    plt.show()

    jet.save(samples, steps)

except Exception as e:
    print(e)

finally:
    jet.deinitSpiAdc()
    jet.deinitStepMotorGpio()