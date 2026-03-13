# Condicionais: 
# Uma condicional é forma de validar se algo está  certo ou errado. 
# Para isso utilizamos o if, que será executado se a condição for verdadeira.
# Cao tivermos mais de uma condição, utilizamos o elif, que é executado se a condição do if for falsa e a sua condição for verdadeira.
# No final, se ambas condições forem falsas, utilizamos o else, que é executado se a condições if e elif forem falsa..

# Em resumo, se for verdadeiro, executa o if, se for falso, executa o elif, se ambas forem falsas, executa o else.

#Exemplo de condição verdadeira com if: 
idade = 18 
if idade >=18: 
    print('Pode entrar na festa') # Éssa condição sempre ser verdadeira, pois 18 >= 18
else:
    print('Nao pode entrar na festa') 


# Exemplo de condição falsa com if: 
idade = 17 
if idade >=18: 
    print('Pode entrar na festa')
elif idade >=16 and idade <=17:
    print('Voce pode entrar mas sem bebidas alcoólicas') # Vocé pode entrar mas sem bebidas alcoólicas

else:
    print('Nao pode entrar na festa')


# Exemplo de condição falsa com if e elif: 
idade = 15
if idade >=18: 
    print('Pode entrar na festa')
elif idade >=16 and idade <=17:
    print(' Vocé pode entrar mas sem bebidas alcoólicas')
else:
    print('Nao pode entrar na festa') # Não pode entrar na  festa!