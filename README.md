# ImersaoIA

Supervisionar uma central de atendimento "Call Center" Automatizando e Gerenciando 100% das ligações.

Hoje em um Call center, é humanamente impossível ouvir e Supervisionar 100% das ligações.

A ideia é ter o retorno de todos os pontos de atendimento, PAs, para saber se estão realmente atendendo as expectivas e ter o controle de qualidade.
Ter o controle das reclamações e Cancelamentos e seus respectivos motivos.

Esse é apenas um protótipo devido ao tempo. Nesse primeiro momento foi feito um script para extração das informações em audio transcrevendo-as para uma base temporaria em JSON.
Como nao tive tempo hábil para estudar a fundo o Gemini, usei uma outra plataforma para extrair essas informações de audio, mas a ideia é deixar tudo dentro do ecosistema do Google.

O segundo Script consome esse JSON e gera um Segundo JSON com os resultados obtidos. 

A principio estou trabalhando com esse tipo de extrutura, mas já estudando outras formas como Dataframe para melhorar performance, mas isso vai ficar para as proximas versões.

## Apêndice

A extrura atual esta com as seguintes informações
data da ligacao
codigo da ligacao
texto da ligacao

com o codigo é possivel conectar com as informações do CRM para linkar com os dados dos clientes e dos ramais e seus respectivos atendentes.

## Roadmap

- Usar o Gemini para trasncrever os audios.

- Integrar com DataFrame.
