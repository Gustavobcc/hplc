# LEIA-ME

## Introdução
`process.py` é o script em python que irá transformar as dezenas de arquivos que o HPLC te forneceu em apenas alguns arquivos prontos para serem inseridos no Excel, Origin etc.

Este programa irá analisar cada arquivo, obter a data e hora da análise e procurar o valor mais alto de absorbância fornecido pelo cromatograma.

Será produzido um arquivo para cada vial com duas colunas, a primeira correspondente ao tempo da análise e a segunda correspondente à absorbância, a partir daí sendo possível plotar o gráfico da cinética.

## Passo-a-passo
### Informações preliminares
Caso múltiplos métodos tenham sido usados no HPLC (p.ex. um pra fazer pontos a cada 10 min e outro pra fazer a cada 30 min), confira se todos estão salvando os cromatogramas com o mesmo comprimento de onda. Isto pode ser verificado na janela principal do software do HPLC, no botão "Data processing parameters", na aba "Multichrom". Isso não é obrigatório, mas vai facilitar a vida mais pra frente. Depois de obtidos todos os resultados, coloque todos os arquivos do **mesmo experimento na mesma pasta**, mas separe **experimentos distintos em pastas distintas**.

Este software presume que os arquivos do HPLC (arquivos de entrada) foram salvos com os nomes no formato `prefixo_IDXXX_YYY.txt`, onde `prefixo` é variável e definido antes de iniciar o HPLC, `ID` é a "Sample ID" definida no cromatógrafo, `XXX` se refere aos diferentes vials, e `YYY` aumenta com cada arquivo. Por exemplo, suponha um experimento em que Paraoxon foi reagido com hidroxilamina em dois vials: Vial 1 com NH2OH a 0,5 M e Vial 2 com NH2OH a 1,0 M, sendo feitas 50 corridas para cada vial. Os arquivos podem ter nome no formato:

```
POX_HAm_conc_POX001_001.txt
POX_HAm_conc_POX002_002.txt
POX_HAm_conc_POX001_003.txt
...
POX_HAm_conc_POX001_099.txt
POX_HAm_conc_POX002_100.txt
```

Neste exemplo, o script produzirá dois arquivos de saída, nomeados `nome_saida001_compil.txt` e `nome_saida002_compil.txt`, referentes aos vials 1 e 2, respectivamente, onde `nome_saida` é um nome escolhido por você durante a execução do script ([ver abaixo](#executando-o-script)). Os arquivos de saída ficarão em uma subpasta `/proc/`, que estará na pasta onde estão os arquivos de entrada.

**Faça um backup (cópia) dos arquivos de entrada.** O script não deve apagar nem sobrescrever nada neles, mas é sempre bom ter uma cópia por segurança. 

### Instalando o Python (Windows)
Procure [no site do Python](https://www.python.org/downloads/windows/) a versão mais recente do Python 3. No final da página, procure `Windows x86-64 executable installer`, baixe, abra e siga as instruções do instalador.

### Baixando e iniciando o script
Clique no botão verde acima escrito "Clone or download", e então clique em "Download ZIP". Baixe e abra o arquivo ZIP, e então extraia o arquivo `process.py` em uma pasta fácil de encontrar.

Abra a pasta onde o `process.py` foi extraído, segure `Shift` e clique com o botão direito. No menu, procure por "Abrir janela de comando aqui" e clique. Será aberta uma janela do Prompt de Comando. Nesta janela, digite `python process.py`. O script se iniciará, pedindo para que digite informações.

### Executando o script
A primeira informação solicidada será a **pasta** onde se encontram todos os arquivos que o HPLC forneceu. Digite o caminho **completo** da pasta, omitindo a barra invertida do final, por exemplo: `D:\HPLC\Paration` ou `C:\Users\MeuNome\HPLC`. **NÃO** digite apenas `Paration`, nem insira o nome dos arquivos, como `D:\HPLC\Paration\POX_HAm_conc_POX001_001.txt`. Aperte `Enter`.

Em seguida, o script pedirá o **número de vials distintos** analisados no experimento, por exemplo cada concentração ou cada pH diferente. Não é a quantidade total de pontos nem o número de pontos por vial. Seguindo com o [exemplo acima](#informações-preliminares), você digitaria `2` &mdash; **não digite** `dois`, nem `100` e nem `50`. Aperte `Enter`.

Na sequência, será solicitado o comprimento de onda que foi salvo no cromatograma. Se houver dúvida, abra algum dos arquivos de entrada e procure (`Ctrl+F`) por `Wavelength (nm)` (ou apenas por `nm`). É possível que o arquivo possua mais de um cromatograma: confira se o comprimento de onda encontrado faz sentido dentro do experimento (p.ex. experimentos com paraoxon, paration e fenitrotion deverão ter cromatogramas com &lambda; próximo a 400). Se não for o caso, continue buscando dentro do arquivo por `Wavelength (nm)` até encontrar o cromatograma correto. Encontrando, digite o valor do &lambda; no script **numericamente e sem unidade**: `405`, não `405 nm` nem `quatrocentos e cinco`. Caso tenham sido usados múltiplos métodos com &lambda; relevantes distintos (p.ex. 400, 405 e 410), será necessário executar o script uma vez para cada &lambda; com todos os mesmos parâmetros, alterando-se apenas este aqui. Aperte `Enter`.

Por fim, você deverá inserir o nome base dos arquivos de saída. Este é o `nome_saída` mencionado anteriormente nas [Informações preliminares](#informações-preliminares), e é equivalente ao "prefixo" dos nomes dos arquivos do HPLC. Novamente no exemplo acima, se você digitar `POX_HAm_conc_vial` nesta etapa na janela, os arquivos de saída serão salvos como `POX_HAm_conc_vial001_compil.txt` e `POX_HAm_conc_vial002_compil.txt`. Aperte `Enter`.

O script começará a rodar, buscando os arquivos de texto de cada vial, iniciando no 001. Aparecerão na janela algumas mensagens descrevendo o progresso do script. Seguindo o exemplo acima, a janela mostraria:

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

**Caso algum dos arquivos analisados não seja sucedido das mensagens de "Cromatograma encontrado" e "Sucesso!", isso significa que algum(ns) arquivo(s) não possuem cromatograma no &lambda; especificado.** Procure algum arquivo de entrada em que o cromatograma tenha outro &lambda; e reexecute o script com este novo valor, mantendo todos os outros parâmetros. Precisando de ajuda entrar em contato comigo ou com o professor.
