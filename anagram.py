import random 
string = input("Digite uma string: ")

anagramas_finais = []

# Sem repetidos
# ! (fatorial) = 7! = 7*6*5*4*3*2*1 = 5040 (exemplo) 

fator = ''
count = 0
repetidos = {}

def fatoriar(str):
    tmp = []
    for i in str:
        tmp.append(i)
    tmp = '*'.join(tmp)
    tmp = tmp[::-1]
    return tmp

def inverter(str):
    return str[::-1]

def sequenciar(num):
    tmp = ''
    count = 0
    for i in range(int(num)):
        tmp += str(int(count)+1)
        count += 1
    
    return tmp

sum = []
ha_repeticao = False

# Verificar repetidos e contar quantos tem de repetidos
for i in string:
    if string.count(i) > 1: 
        ha_repeticao = True
        repetidos[i] = string.count(i)
    count += 1
    fator += str(count)
    sum.append(str(count))

p = []

# Fatoriar a sequencia de repetidos (repetidos fica por exemplo 'e': 2)
# 2*1
for i in repetidos:
    p.append(fatoriar(sequenciar(repetidos[i])))

div = '(' + ' * '.join(p) + ')'

# Colocar * entre todos e inverter
summarize = '*'.join(sum)
summarize = summarize[::-1]

corrigir = []
# summarize.split('*') separa tudo que está entre os '*'

for i in summarize.split('*'):
    corrigir.append(i)

for i in corrigir:
    if len(i) > 1:
        corrigir[corrigir.index(i)] = inverter(i)

summarize = '*'.join(corrigir)

if ha_repeticao:    
    possibilidades = eval(summarize + '/' + div)
else:
    possibilidades = eval(summarize)

print('Possibilidades: ', possibilidades)

acuracia_limiar = 200 # MUITO IMPORTANTE PARA RESULTADOS REAIS
# acuracia_limiar = int(input('Acurácia Limiar: '))

# Agora o programa começa...
def programa():
    global anagramas_finais

    # Setar variaveis vazias
    anagramas_finais = []
    d = []
    possiveis = {}
    tmp = ''
    count = 1

    # Colocar todas as letras da string numa lista
    for i in string: d.append(i)

    for i in range(int(possibilidades)**acuracia_limiar):
        random.shuffle(d) # embaralhar
        tmp = ''.join(d) # setar tmp como a lista convertida em string

        # apenas colocar se a string embaralhada não está na lista (evitar duplicados)
        if tmp in possiveis: count += 1
        else: count = 1

        possiveis[tmp] = count 

        # checagem de acurácia
        # a acuracia limiar recomendada varia dependendo do tamanho da string, 
        # quanto menor, mais chances de gerar duplicados
        if possiveis[tmp] > acuracia_limiar: break
        else: continue 

    # resetar o contador
    count = 0
    s = []

    # adicionar todos os anagramas possíveis e aumentar 1 no contador
    for i in possiveis:
        s.append(i)
        count += 1

    # retornar todas as possibilidades
    possiveis.clear()
    count = 0
    return s

testes = int(input('Quantos testes deseja fazer: '))
acuracia_recomendada = possibilidades/testes*len(string)*5
print(f'\nAcurácia Limiar recomendada: {acuracia_recomendada}')
print(f'Acurácia Limiar em uso: {acuracia_limiar}')
print(f'Diferença Limiar entre Acurácias: {acuracia_recomendada-acuracia_limiar}')

# Regular Acurácia
def regular():
    global acuracia_limiar

    op = input('\n\tDigite "a" para regular sua acurácia para a recomendada\n\tDigite "n" para colocar uma nova acurácia\n\tDigite "k" ou deixe em branco para manter a acurácia atual\n\t> ')
    if op == 'a':
        acuracia_limiar = int(acuracia_recomendada)
    elif op == 'n':
        acuracia_limiar = int(input('Acurácia Limiar: '))
    elif op == 'k' or op == '':
        pass
    else:
        print('não reconheci esta opção')
        regular()
regular()

for i in range(testes):
    out = programa()
    if len(out) == possibilidades:
        print(out)
        print(f'Tamanho: {len(out)}')
        if len(out) == possibilidades:
            print('Match PERFEITO')
        break 
else:
    print(f'Não foi possível achar a quantidade de anagramas possíveis\nRevise seu valor de acurácia ou a quantidade de testes a ser feitos')
