import json
import csv
import time
import timeit

def lerJSON(file): #lê o arquivo json e armazena em "automato" retornando o mesmo
    with open(file) as file:
        automato = json.load(file)
        return automato
    
    # dicionário: vetor numeros[1, 2, 3] ao inves de usar o indice numero, é usado um "simbolo" para acessar, como "inicial"  

def lerCSV(file): #lê o arquivo csv de input e armazena em "entradas" retornando o mesmo
    stringsEntrada = [] # array das entradas
    with open(file) as file:
        entradas = csv.reader(file)
        
        for linha in entradas:
            stringsEntrada.append(linha[0])

    return stringsEntrada

def percorrerAutomato(estadoInicial, estadoFinal, transicoes, entrada):
    estadoAtual = estadoInicial
    for caractere in entrada:
        if caractere == ";" or estadoAtual == "-1":
            break
        estadoAtual = proximoEstado(estadoAtual, caractere, transicoes)
    return int(estadoAtual) in estadoFinal

def proximoEstado(estadoAtual, caractere, transicoes):
    if str(caractere) in transicoes[str(estadoAtual)] :
        estadoAtual = transicoes[str(estadoAtual)][str(caractere)]
    else:
        estadoAtual = "-1"
    return estadoAtual

def main():
    automato = lerJSON('C:/Códigos vscodes/Pitao/Teoria da Computacao/automaton.json') 
    entradas = lerCSV('C:/Códigos vscodes/Pitao/Teoria da Computacao/input.csv')

    estadoInicial = automato['initial']
    estadoFinal = automato['final']
    transicoes = {} #dicionário 
    for transicao in automato["transitions"]:
        if transicao["from"] not in transicoes:
            transicoes[transicao["from"]] = {transicao["read"]: transicao["to"]}
        else:
            transicoes[transicao["from"]].update({transicao["read"]: transicao["to"]})
        #transicoes = {(transicao['from'], transicao['read']): transicao['to'] for transicao in automato['transitions']} 

    resultados = []
    for entrada in entradas:
        start_time = timeit.default_timer()
        resultado = percorrerAutomato(estadoInicial, estadoFinal, transicoes, entrada)
        elapsed_time = timeit.default_timer()-start_time
        if resultado:
            resultado = 1
        else:
            resultado = 0
        resultados.append((entrada, resultado, f"{elapsed_time:.8f}"))

    with open('saida_output.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
        for resultado in resultados:
            resultado_final = resultado[0]+";"+str(resultado[1])+";"+str(resultado[2])
            writer.writerow([resultado_final])

if __name__ == "__main__":
    main()
