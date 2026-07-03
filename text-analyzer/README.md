# Text Analyzer

A command-line tool that analyzes a text and returns statistics about it.

## What it does
- Counts words, sentences and characters
- Shows the 3 most frequent words
- Handles empty input gracefully

## How to run
```bash
python main.py
```

## Example output
Escreve um texto: O gato comeu o peixe. O gato ficou feliz!
Número de palavras: 9
Número de frases: 2
Número de caracteres: 46
Sem espaços: 38
Palavras mais frequentes: ['o', 'gato', 'peixe']

## What I learned
- How to structure code into functions with single responsibilities
- Using Python's `Counter` from `collections` to count efficiently
- Handling edge cases like empty input and punctuation attached to words
- Git workflow: staging, committing and pushing to GitHub
