class Temperature:
    def __init__(self,temp):
        self.temp = temp
        
    def convert_to_celcius(self):
        var = float((self.temp -32) * 5/9)
        return var
    
    def convert_to_farenheit(self):
        var = float((9 * self.temp) /5 + 32)
        return var
    
#object
faren = float(input("Enter temperature in farenheit: "))
temp1 = Temperature(faren)
print(temp1.convert_to_celcius())
celcius = float(input("Enter the temperature in celcius: "))
temp1 = Temperature(celcius)
print(temp1.convert_to_farenheit())