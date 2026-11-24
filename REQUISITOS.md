1. Requisitos Funcionais (RF) — O que o sistema faz:
RF01 - Cadastro de Demandas: O sistema deve permitir o registo de novas demandas, solicitando ID único, título, solicitante, prioridade, CEP, cidade e status inicial.
RF02 - Listagem de Demandas: O sistema deve exibir uma lista organizada de todas as demandas registadas no terminal.   
RF03 - Busca de Demandas: O sistema deve permitir procurar uma demanda específica com base no seu ID ou título.
RF04 - Atualização de Status: O sistema deve permitir alterar o status de uma demanda existente (por exemplo, de "Pendente" para "Em Andamento" ou "Concluído").   
RF05 - Exclusão de Demandas: O sistema deve permitir remover uma demanda do sistema através do seu ID.
RF06 - Consulta de APIs Externas: O sistema deve permitir consultar automaticamente dados de endereço através do ViaCEP e cotações de moedas via AwesomeAPI.   
2. Requisitos Não Funcionais (RNF) — Como o sistema opera (qualidade):
RNF01 - Usabilidade (CLI): O sistema deve possuir uma interface de linha de comando (CLI) intuitiva, com menus claros e fáceis de navegar.   
RNF02 - Integridade de Dados: O sistema deve impedir o registo de demandas com IDs duplicados ou com campos obrigatórios vazios.   
RNF03 - Segurança e Resiliência: O sistema deve tratar erros de digitação e falhas de conexão de rede através de blocos de exceção, garantindo que o programa nunca encerre abruptamente.   
RNF04 - Restrição de Ambiente: O sistema deve ser executado inteiramente com recursos nativos do Python, sem exigir privilégios de administrador ou instalação global de pacotes.   
RNF05 - Desempenho: O sistema deve responder às operações CRUD em memória de forma instantânea (menos de 1 segundo).