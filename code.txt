def xor(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))

def crc(data, key):
    n = len(key)
    temp = data[:n]

    for i in range(n, len(data)):
        if temp[0] == '1':
            temp = xor(key, temp) + data[i]
        else:
            temp = xor('0' * n, temp) + data[i]

    if temp[0] == '1':
        temp = xor(key, temp)
    else:
        temp = xor('0' * n, temp)

    return temp

data = input("Enter data bits: ")
key = input("Enter divisor/key: ")

sender_data = data + '0' * (len(key) - 1)
remainder = crc(sender_data, key)
codeword = data + remainder

print("CRC Remainder:", remainder)
print("Transmitted Codeword:", codeword)

received = input("Enter received codeword: ")
check = crc(received, key)

if '1' in check:
    print("Error detected")
else:
    print("No error")