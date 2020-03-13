import math
def getTemperature(ADC_value,rref):
    temperature = 1/( (1/(273+25))+(1/(3830))*math.log(((1023/ADC_value - 1) * rref)/5000))-273
    return temperature

print(getTemperature(140,1000))