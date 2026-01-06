class Solution(object):
    def convertTemperature(self, celsius):
        kelvin=celsius+273.15
        fahrenheit=celsius*1.80+32
        return [kelvin,fahrenheit]






Answer=Solution()
print(Answer.convertTemperature(34.5))
