# interface

## Objetivo

criar uma interface que exiba os dados dos candidatos em uma tela. Funcionará como uma espécie de slide, e, em cada tela, haverá uma seta para avançar ou retroceder. Esses dados devem ser separados por curso.
- Questão de otimização: abrir com um menu pedindo para o recrutador escolher o curso, e, após a escolha, buscar na lista todos os candidatos que atendam, independente do curso, ou automaticamente deixar candidatos de curso x agrupados?
Cada tela deverá conter os dados dos candidatos e um campo para que o recrutador possa inserir sua avaliação
  - essa avaliação pode ser por nota, por estrela (esta acho criativa, dava até pra ser foguete pra combinar kkkk), texto, etc. É bom tirar essa dúvida quando chegar neste etapa

Existem algumas detalhes simples, como:
- para o primeiro candidato, so haverá seta para frente
- para o último, só para trás

## Semana 1:
### Gerar dados artificialmente

#### Organização dos dados
- alguma variável composta, como lista ou dicionário
- levar para algum arquivo externo

#### Nome
- listar nomes manualmente
- utilizar alguma API web

#### E-mail
- tornar os nomes em lowercase
- concatenar nome + sobrenome + @alunos.utfpr.edu.br

#### WhatsApp
- gerar um inteiro de 2 digitos de 1 a 9 para o DDD
- gerar dois inteiros no intervalo
  - o primeiro bloco deve ser somado a 90000
- concatenar '(' + '15' + ') ' + '98765' + '-' + '1234'
- percorrer os outros telefones e garantir que não exista outro igual

#### RA
- gerar um inteiro de 7 digitos superior a 1000000
- garantir que não exista repetição de RA entre candidatos

#### Campus
- criar uma lista com todos os campus, para que este seja selecionado aleatoriamente

#### Curso
- em cada campus, criar uma lista com os cursos ofertados
- sortear o curso de acordo com o campus

#### Período
- sortear um valor entre [1, 10]

#### Área
- em cada curso, criar uma variavel composta com as áreas de atuação dentro da Orion
- sortear a área de acordo com o curso
> PS: antes, checar se existe este tipo de restrição para atuação ou se é de livre escolha independente do curso

#### Subárea
- em cada área, criar uma variável composta com as subáreas
- sortear a subárea de acordo com a área

#### Defeitos
?

#### Qualidades
?
