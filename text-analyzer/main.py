from collections import Counter

def contar_palavras(texto):
    # responsabilidade: só contar palavras
    return len(texto.split())

def contar_frases(texto):
    count = 0
    for caractere in texto:
        if caractere in ".!?":
            count += 1
    return count


def palavras_mais_frequentes(texto):
    # responsabilidade: só encontrar as três mais repetidas
    palavras = [p.strip(".,!?;:") for p in texto.lower().split()]
    freq = Counter(palavras)
    return [palavra for palavra, _ in freq.most_common(3)]


def analisar(texto):
    # responsabilidade: chamar as outras e mostrar resultados
    if not texto.strip():
        print("Texto vazio. Escreve alguma coisa.")
        return
    n_palavras = contar_palavras(texto)
    n_frases = contar_frases(texto)
    
    n_caracteres = len(texto)
    n_caracteres_sem_espacos = len(texto.replace(" ", ""))


    palavras_freq = palavras_mais_frequentes(texto)

    print(f"Número de palavras: {n_palavras}")
    print(f"Número de frases: {n_frases}")
    print(f"Número de caracteres: {n_caracteres}")
    print(f"Sem espaços: {n_caracteres_sem_espacos}")
    print(f"Palavras mais frequentes: {palavras_freq}")



texto = input("Escreve um texto: ")
analisar(texto)