#1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
lista_livros = ["Duna 1", "Duna 2", "Duna 3"]
print(lista_livros)

print("------------------------------")
#Usando a lista livros, exiba apenas o primeiro e o último elemento.
print(lista_livros[0], lista_livros[2])
print("------------------------------")
#3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.

lista_livros.append("Duna 4")
lista_livros.append("Duna 5")
print(lista_livros)

print("------------------------------")

#4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
lista_livros.insert(1, "Duna")
print(lista_livros)

print("------------------------------")

#5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".

if "silencio dos inocentes" in lista_livros:
    lista_livros.remove("silencio dos inocentes")
else:
    print("O livro 'silencio dos inocentes' não está na lista.")
print(lista_livros)

print("------------------------------")

#6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.

lista_numeros = [1, 2, 3, 2, 4, 2, 5]
print(lista_numeros.count(2))

print("------------------------------")

#7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"

for livro in lista_livros:
    print(f"O livro {livro} é interessante")

print("------------------------------")
#8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.

lista_idades = [12, 18, 25, 14, 30]
for idade in lista_idades:
    if idade >= 18:
        print(f"A idade {idade} é maior ou igual a 18")


print("------------------------------")
#9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.

lista_valores = [10, 20, 30, 40]
soma = 0
for valor in lista_valores:
    soma += valor
print(f"A soma dos valores é: {soma}")

print("------------------------------")

#10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
#notas = [[7, 8, 9], [6, 5, 7]] #No fim, imprima a média de cada aluno.

print("Digite as notas do primeiro aluno:")
aluno1 = []
aluno2 = []
for n in range(3):
    nota = float(input(f"Nota :"))
    aluno1.append(nota)
notas = []
notas.append(aluno1)
print(notas)
print("Digite as notas do segundo aluno:")
for n in range(3):
    nota = float(input(f"Nota :"))
    aluno2.append(nota)
notas.append(aluno2)
print(notas)

