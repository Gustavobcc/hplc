# LEIA-ME

## Introdução
`process.py` é o script em python que irá transformar as dezenas de arquivos que o HPLC te forneceu em apenas alguns arquivos prontos para serem inseridos no Excel, Origin etc.

Este script irá analisar cada arquivo, obter a data e hora da análise e procurar o valor mais alto de absorbância fornecido pelo cromatograma.

Será produzido um arquivo para cada vial com duas colunas, a primeira correspondente ao tempo da análise e a segunda correspondente à absorbância, a partir daí sendo possível gerar o gráfico da cinética.

## Passo-a-passo
### Informações preliminares
Caso múltiplos métodos tenham sido usados no HPLC (p.ex. um pra fazer pontos a cada 10 min e outro pra fazer a cada 30 min), confira se todos estão salvando os cromatogramas no mesmo comprimento de onda. Isto pode ser verificado na janela principal do software do HPLC, no botão "Data processing parameters", na aba "Multichrom". Isso não é obrigatório, mas vai facilitar a vida mais pra frente. Depois que todos os resultados foram obtidos e exportados em ASCII, coloque todos os arquivos do **mesmo experimento na mesma pasta**, mas separe **experimentos distintos em pastas distintas**.

Este script presume que os arquivos do HPLC (arquivos de entrada) foram salvos com os nomes no formato `prefixo_IDXXX_YYY.txt`, onde `prefixo` é customizável e definido antes de iniciar a corrida no HPLC, `ID` é a "Sample ID" definida também antes da corrida, `XXX` se refere aos diferentes vials, e `YYY` aumenta sequencialmente com cada arquivo. Por exemplo, suponha um experimento em que Paraoxon foi reagido com hidroxilamina em dois vials: Vial 1 com NH2OH a 0,5 M e Vial 2 com NH2OH a 1,0 M, sendo feitas 50 corridas para cada vial. Os arquivos poderão ter nomes como:

```
POX_HAm_conc_POX001_001.txt
POX_HAm_conc_POX002_002.txt
POX_HAm_conc_POX001_003.txt
POX_HAm_conc_POX002_004.txt
...
POX_HAm_conc_POX001_099.txt
POX_HAm_conc_POX002_100.txt
```

Neste exemplo, o script produzirá dois arquivos de saída, nomeados `nome_saida001_compil.txt` e `nome_saida002_compil.txt`, referentes aos vials 1 e 2, respectivamente, onde `nome_saida` é um nome escolhido por você durante a execução do script ([ver abaixo](#executando-o-script)). Os arquivos de saída ficarão em uma subpasta `\proc\`, localizada na pasta onde estão os arquivos de entrada.

**Faça um backup (cópia) dos arquivos de entrada.** O script não deve apagar nem sobrescrever nada neles, mas é sempre bom ter uma cópia por segurança. 

### Instalando o Python (Windows)
Procure [no site do Python](https://www.python.org/downloads/windows/) a versão mais recente do Python 3 ("Latest Python 3 release", atualmente é a 3.8.1). No final da página, procure `Windows x86-64 executable installer`, baixe, abra e siga as instruções do instalador.

### Baixando e iniciando o script
Clique no botão verde acima escrito "Clone or download", e então clique em "Download ZIP". Baixe e abra o arquivo `hplc-master.zip`. A partir daí, você pode extrair todo o conteúdo do zip ou, alternativamente, abrir a pasta `hplc-master` dentro do mesmo e extrair apenas o arquivo `process.py`. Preferencialmente, faça isto em alguma pasta fácil de encontrar.

Abra a pasta onde o `process.py` foi extraído, segure `Shift` e clique com o botão direito. No menu, procure por "Abrir janela de comando aqui" e clique. Será aberta uma janela do Prompt de Comando. Nesta janela, digite `python process.py`. O script se iniciará, pedindo para que digite algumas informações.

### Executando o script
A primeira informação solicidada será a **pasta** onde se encontram todos os arquivos que o HPLC forneceu. Digite o caminho **completo** da pasta, omitindo a barra invertida do final, por exemplo: `D:\HPLC\Paration` ou `C:\Users\MeuNome\HPLC`. **NÃO** digite apenas `Paration`, nem insira o nome dos arquivos, como `D:\HPLC\Paration\POX_HAm_conc_POX001_001.txt`. Aperte `Enter`.

Em seguida, o script pedirá o **número de vials distintos** analisados no experimento, por exemplo cada concentração ou cada pH diferente. Não é a quantidade total de pontos nem o número de pontos por vial. Seguindo com o [exemplo acima](#informações-preliminares), você digitaria `2` &mdash; **não digite** `dois`, nem `100` e nem `50`. Aperte `Enter`.

Na sequência, será solicitado o comprimento de onda que foi salvo no cromatograma. Se houver dúvida, abra algum dos arquivos de entrada e procure (`Ctrl+F`) por `Wavelength (nm)` (ou apenas por `nm`). É possível que o arquivo possua mais de um cromatograma: confira se o comprimento de onda encontrado faz sentido dentro do experimento (p.ex. experimentos com paraoxon, paration e fenitrotion deverão ter cromatogramas com &lambda; próximo a 400). Se não for o caso, continue buscando dentro do arquivo por `Wavelength (nm)` até encontrar o cromatograma correto. Encontrando, digite o valor do &lambda; na janela do prompt **numericamente e sem unidade**: `405`, não `405 nm` nem `quatrocentos e cinco`. Caso tenham sido usados múltiplos métodos com &lambda; relevantes distintos (p.ex. 400, 405 e 410), será necessário executar o script uma vez para cada &lambda; com todos os mesmos parâmetros, alterando-se apenas este aqui. Após inserir o valor, aperte `Enter`.

Por fim, você deverá inserir o nome base dos arquivos de saída. Este é o `nome_saída` mencionado anteriormente nas [Informações preliminares](#informações-preliminares), e é equivalente ao "prefixo" dos nomes dos arquivos do HPLC. Novamente usando o exemplo acima, se você digitar `POX_HAm_conc_vial` na janela nesta etapa, os arquivos de saída serão salvos como `POX_HAm_conc_vial001_compil.txt` e `POX_HAm_conc_vial002_compil.txt`. Aperte `Enter` após digitar o nome base desejado.

O script começará a rodar, buscando os arquivos de texto referentes a cada vial, iniciando no vial 001. Aparecerão na janela algumas mensagens descrevendo o progresso do script. Seguindo o exemplo acima, a janela mostraria:

```
ANALISANDO VIAL: 001
Analisando arquivo 1 de 50 (0%)
Cromatograma encontrado. Analisando...
Sucesso!
Analisando arquivo 2 de 50 (2%)
Cromatograma encontrado. Analisando...
Sucesso!

[...]

Analisando arquivo 50 de 50 (98%)
Cromatograma encontrado. Analisando...
Sucesso!
Vial 001 terminado!
ANALISANDO VIAL: 002
Analisando arquivo 1 de 50 (0%)
Cromatograma encontrado. Analisando...
Sucesso!

[...]

Analisando arquivo 50 de 50 (98%)
Cromatograma encontrado. Analisando...
Sucesso!
Vial 002 terminado!
```

**Caso algum(ns) dos arquivos analisados não seja(m) seguido(s) das mensagens de "Cromatograma encontrado" e "Sucesso!", isso significa que este(s) arquivo(s) não possuem cromatograma no &lambda; especificado.** Procure algum arquivo de entrada em que o cromatograma tenha outro &lambda; e reexecute o script com este novo valor, mantendo todos os outros parâmetros. Precisando de ajuda entrar em contato comigo ou com o professor.

Caso seja necessário interromper o script em qualquer momento de sua execução, aperte `Ctrl+C`.

### Processamento posterior
Os arquivos de saída são gerados num formato parecido com este:

```
1578595541	208.993
1578596289	249.120
1578597037	251.326
1578597785	264.352
[...]
```

Como mencionado anteriormente, são duas colunas: uma referente ao horário da análise e outra ao valor da absorbância.

A coluna do tempo (à esquerda) registra o mesmo no formato de [marca temporal UNIX](https://pt.wikipedia.org/wiki/Era_Unix#Marca_temporal_UNIX), ou seja, quantos segundos se passaram desde 01/01/1970 à meia noite, horário de Greenwich. O importante de se notar aqui é que é obtido um **tempo relativo em segundos**. Este número pode ser transformado em segundos relativos ao início da primeira corrida do vial (para obter um tempo iniciando em 0 segundos para gerar o gráfico) fazendo uso do Excel, Planilhas Google, LibreOffice Calc ou qualquer outro software de planilhas.

Para fazer essa transformação, comece copiando todo o conteúdo do arquivo de saída e colando em uma planilha vazia. Primeiro, confira se os valores de absorbância fazem sentido &mdash; o script usa `.` (ponto) para separar o decimal, pode ser que sua planilha use `,` (vírgula); se for o caso, use a função "localizar e substituir" e substitua todos os `.` por uma `,`.

Depois de verificar se está tudo certo, insira uma coluna vazia entre as duas já existentes (1). Na linha 1 desta nova coluna, digite a fórmula `=$A1-MÍNIMO($A:$A)` (2) e clique duas vezes no quadrado no canto inferior direito da célula (3) para preencher automaticamente o resto da coluna (4).

![Imagem descritiva do procedimento acima](https://i.imgur.com/JP0o4nz.png)

Pronto! Use as colunas B e C para gerar o gráfico, seja na própria planilha ou no Origin, por exemplo. O Origin possui funções mais poderosas para fazer a regressão não-linear destes gráficos para obter o *k*\_obs. Note que provavelmente alguns pontos precisarão ser eliminados devido a alguns problemas de incerteza gerados pelo cromatógrafo durante as corridas mas, em geral, haverão pontos de sobra para que isso não seja um problema.
