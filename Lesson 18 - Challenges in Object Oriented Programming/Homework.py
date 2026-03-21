class RomanConverter:
    def int_to_roman(self, num):
        values = [1000, 500, 100, 50, 10, 5, 1]
        symbols = ["M", "D", "C", "L", "X", "V", "I"]

        result = ""

        for i in range(len(values)):
            while num >= values[i]:
                result = result + symbols[i]
                num = num - values[i]

        return result

obj = RomanConverter()
print(obj.int_to_roman(23))  
print(obj.int_to_roman(47))   