Este trabalho consiste em implementar codificadores e decodificadores de sinal para as técnicas:
1) NRZ-I 
2) Manchester Diferencial 
3) HDB3
4) 8B/6T
5) 6B/8B 

O decodificador indica a existência de erros, quando permitir sua detecção.
O sinal no NRZ-I e do Manchester Diferencial começa em negativo (-).
No HDB3 é considerado que o próximo sinal a ser enviado é positivo (+) (pulso anterior é negativo) e a diferença entre positivos e negativos inicial é igual a 0.
A técnica 6B/8B utiliza o codificador NRZ-I após a conversão de 6 para 8 bits

O codificador deve ser executado da seguinte forma:
$ python3 encode.py <técnica> <dados_hexa>
Onde:
<técnica> pode ser nrzi, mdif, hdb3, 8b6t ou 6b8b
<dados_hexa> são os dados de entrada em formato hexa que devem ser codificados

O Decodificador deve ser executado da seguinte forma:
$ python3 encode.py <técnica> <sinal>
Onde:
<técnica> pode ser nrzi, mdif, hdb3, 8b6t ou 6b8b
<sinal> é o sinal que devem ser decodificado
