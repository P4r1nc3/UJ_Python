def roman2int(num):
        values = {'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}   
        result = 0
        for i in range(len(num)):
            if i + 1 < len(num) and values[num[i]] < values[num[i + 1]] :                  
                result = result - values[num[i]]                      
            else:
                result = result + values[num[i]]
        return result

x = input("Enter a Roman numeral: " )
print(roman2int(x))
