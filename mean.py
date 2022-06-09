import jetFunctions as jet

jet.initSpiAdc()
print("got mean value: ", jet.getMeanAdc(20000))
jet.deinitSpiAdc()