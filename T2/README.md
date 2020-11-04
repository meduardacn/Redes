Trabalho 2 - Descrição
Este trabalho consiste em implementar codificadores e decodificadores para detecção e correção de erros usando as técnicas de redundância de bloco, CRC e código de Hamming.<br />
Os detalhes sobre a entrada e saída para cada técnica estão apresentados abaixo:<br />

Os códigos devem ser executado da seguinte forma: <br />
1. Redundância de bloco
Codificador: <br />
$ python3 bcc_encoder.py [string em ASCII]  =>  [string codificada em formato hexadecimal]<br />
Decodificador: <br />
$ python3 bcc_decoder.py [código em hexadecimal] => [string em ASCII] ou "ERRO"

2. CRC
Codificador: <br />
$ python3 crc_encoder.py [string em ASCII] [polinômio gerador de ordem 5 expresso em binário] => [string codificada em formato hexadecimal]
Decodificador: <br />
$ python3 crc_decoder.py [string codificada em formato hexadecimal] [polinômio gerador de ordem 5 expresso em binário] => [string em ASCII] e/ou "ERRO" <br />
(OBS. São indicados os caracteres que tiveram erro na transmissão)

3. Código de Hamming
Codificador: <br />
$ python3 ham_encoder.py [string em ASCII] => [string codificada em formato hexadecimal]
Decodificador: <br />
$ python3 ham_decoder.py [código em hexadecimal] => [string em ASCII] <br />
(OBS. os caracteres que apresentaram foram corrigidos e sua correção esta indicada na saída)