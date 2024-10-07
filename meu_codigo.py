class Aluno:
    def __init__(self, nota1, nota2, nota3):
        # Garantir que as notas estejam no intervalo correto
        if all(0 <= nota <= 10 for nota in [nota1, nota2, nota3]):
            self.notas = [nota1, nota2, nota3]
        else:
            raise ValueError("As notas devem estar entre 0 e 10.")

    def media(self):
        """Calcula e retorna a média das três notas."""
        return sum(self.notas) / len(self.notas)

    def maior_nota(self):
        """Retorna a maior nota."""
        return max(self.notas)

    def menor_nota(self):
        """Retorna a menor nota."""
        return min(self.notas)

    def diferenca_maior_menor(self):
        """Retorna a diferença entre a maior e a menor nota."""
        return self.maior_nota() - self.menor_nota()

# Exemplo de uso
try:
    aluno = Aluno(8.5, 7.2, 9.0)
    
    print("Média do aluno:", aluno.media())
    print("Maior nota:", aluno.maior_nota())
    print("Menor nota:", aluno.menor_nota())
    print("Diferença entre a maior e a menor nota:", aluno.diferenca_maior_menor())
    
except ValueError as e:
    print(e)
