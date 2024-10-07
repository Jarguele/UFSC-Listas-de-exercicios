def binario_para_decimal(binario):
    decimal = 0
    pot = 0
    
    # Iterar sobre os dígitos da direita para a esquerda
    for digito in binario[::-1]:
        decimal += int(digito) * (2 ** pot)
        pot += 1
    
    return decimal

# Teste
binario = "10"
decimal = binario_para_decimal(binario)
print(decimal)  # Saída: 11