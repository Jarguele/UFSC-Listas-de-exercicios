def binario_para_decimal(binario):
    decimal = 0
    pot = 0
    
    # Iterar sobre os dígitos da direita para a esquerda
    for digito in binario[::-1]:
        decimal += int(digito) * (2 ** pot)
        pot += 1
    
    return decimal

# Solicitar ao usuário que insira o número binário
binario = input("Digite um número binário: ")

# Converter o número binário para decimal
decimal = binario_para_decimal(binario)

# Exibir o resultado
print(f"O número binário {binario} em decimal é {decimal}.")

