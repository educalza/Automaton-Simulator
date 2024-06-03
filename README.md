 ## Simulador automato determinístico finito

 Trabalho de Teoria da Computação - Simulador de AFD

 
 ## Funcionalidades 

    - Leitura de autômatos a partir de um arquivo JSON.
    - Leitura da entraga a partir de um arquivo CSV.
    - Simulação de Autômatos Determinísticos Finitos.
    - Criação de um arquivo output em CSV contendo o resultado e tempo de execução

## Execução do programa & Exemplos

    É necessário o uso de dois arquivos para que o programa funcione

### Arquivo JSON

        {
        "initial": 0,
        "final" : [2],
        "transitions": [
            {
            "from": "0",
            "to": "0",
            "read": "a"
            },
            {
            "from": "2",
            "to": "2",
            "read": "a"
            },
            {
            "from": "1",
            "to": "1",
            "read": "b"
            },
            {
            "from": "1",
            "to": "2",
            "read": "a"
            },
            {
            "from": "0",
            "to": "1",
            "read": "b"
            }
        ]
        }

### Arquivo CVS input

        ba;1
        aaaabbbbbaaaaa;1
        abababab;0
        bbbbbbbb;0
        aaaaaaaaaaaa;0
        aaaaabaaaaa;1

### Arquivo CVS output

    Este arquivo o programa é quem concede

        aa;1;0;0.00001520
        ab;1;0;0.00000690
        ba;1;0;0.00000420
        bb;0;0;0.00000330
        aaa;0;0;0.00000500
        bbb;0;0;0.00000390
