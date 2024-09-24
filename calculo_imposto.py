print("Iniciando o cálculo do imposto...")
def calcular_imposto_renda(renda_anual):
    # Faixas de rendimento e suas respectivas alíquotas
    faixas = [
        (22847.76, 0.0),   # Isento até R$ 22.847,76
        (33919.80, 0.15),  # 15% de 22.847,77 até 33.919,80
        (45012.60, 0.225), # 22,5% de 33.919,81 até 45.012,60
        (inf, 0.275)       # 27,5% acima de 45.012,60
    ]

    imposto = 0.0
    base_anterior = 0.0

    for limite, aliquota in faixas:
        if renda_anual > limite:
            imposto += (limite - base_anterior) * aliquota
            base_anterior = limite
        else:
            imposto += (renda_anual - base_anterior) * aliquota
            break

    return imposto

# Exemplo de uso
renda = float(input("Digite sua renda anual: "))
imposto_devido = calcular_imposto_renda(renda)
print(f"O imposto de renda devido é: R$ {imposto_devido:.2f}")

