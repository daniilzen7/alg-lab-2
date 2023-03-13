t = 'Hello, world!'

def multiplication(text): #хеширование методом умножения по формуле
    hash = ''
    M = len(text) #длина массива
    C = 0.5 #случайное число из интервала [0,1]
    for i in text:
        if type(i) == str:
            K = ord(i) #переводим символ Unicode в число если необходимо
            hash += str((int(((K * C) % 1) * M)//1)) #считаем по формуле, записываем целочисленные значения
        else:
            hash += str((int(((i * C) % 1) * M)//1))
    return hash

def CRC(text):
    G = 0x04C11DB7 #нормальное представление из таблицы
    R = 0xFFFFFFFF
    bytes = bytearray(text, 'utf-8')
    
    for byte in bytes:
        for bit in range(8):
            if (R ^ (byte >> bit)) & 0x00000001:
                R = (R >> 1) ^ G
            else:
                R = R >> 1
    return '{:08X}'.format(R) #и вывод
    
print(multiplication('Hello, world!'))
print(CRC('Hello, world!'))