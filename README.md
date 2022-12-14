# <p align=center> PyAnagram </p>
### <p align=center> Checador Avançado de Anagramas em Python </p>

# <p align=center> Funcionalidades </p>

## Acurácia Limiar
### **Sistema de Acurácia** 
<h4> Quanto menor a string, maior a possibilidade de gerar duplicados <br> <i>Também depende da quantidade de testes que o usuário fazer</i> </h4>

### Resumo:
- Quanto menor a string e mais testes o usuário fazer: maior a chance de duplicados 
- Quanto menor a string e menos testes o usuário fazer: uma acurácia melhor 
- Quanto maior a string e mais testes o usuário fazer: maior a acurácia de testes
- Quanto maior a string e menos testes o usuário fazer: menor a chance de exibir resultados fieis 

### Calculo *temporário* de uma Acurácia Limiar recomendada:
```py
possibilidades/testes*len(string)*10
```

Após rodar o programa com uma acurácia "desregulada" o programa irá te avisar a acurácia recomendada para aquela string com base nas possibilidades e na quantidade de testes e irá te perguntar se quer alterar a acurácia para a recomendada, se quer ignorar ou se quer colocar uma nova acurácia customizada


## Para fazer
- [ ] Sistema de Acurácia muito mais rápido
- [ ] Alterar a acurácia conforme o programa roda 
- - Exemplo: Keyframe de acurácia = $-200=300 , 200-340=500 , 350-^=329
- - $ = inicio | ^ = fim | - = até
- [ ] Sugestão aprimorada de acurácias
- [ ] Balanceador de Testes
- - Calcula a quantidade de testes que você colocou e vê se os resultados serão imprimidos mais rapidos
