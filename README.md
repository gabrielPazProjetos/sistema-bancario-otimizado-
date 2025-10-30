# Sistema Bancário em Python

Este projeto é um sistema bancário funcional desenvolvido em Python, com foco em modularização, validação de dados e uso correto de argumentos em funções. Ele permite o gerenciamento de usuários, contas correntes e operações bancárias básicas via terminal.

## Funcionalidades

- Cadastro de usuários com validação de CPF
- Criação de contas correntes vinculadas a usuários existentes
- Depósitos com argumentos posicionais
- Saques com argumentos nomeados e controle de limite
- Geração de extrato com data e hora das transações
- Listagem de contas cadastradas
- Interface interativa via terminal

## Regras de Argumentos

- deposito(saldo, valor, extrato, /) → argumentos por posição
- saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques) → argumentos por nome
- extrato_bancario(saldo, /, *, extrato) → mistura de posição e nome

## Exemplo de Uso
- Criar um usuário com CPF único
- Criar uma conta vinculada a esse CPF
- Realizar depósitos e saques com validações
- Consultar o extrato da conta

## Aprendizados Aplicados
- Organização de dados com listas e dicionários
- Separação de responsabilidades por funções
- Validação de entrada e lógica de negócio
- Uso de argumentos em funções
- Interface de linha de comando clara e funcional


## Nota
Projeto puramente feito para fins academicos.
