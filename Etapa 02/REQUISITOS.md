# Documentação do Projeto - TechFlow Core

## 📋 Visão Geral
O **TechFlow Core** é um sistema de gestão de demandas desenvolvido em Python para o ambiente CLI (Linha de Comandos), aplicando conceitos de Clean Code, modularização e consumo de API externa.

---

## ⚙️ Requisitos Funcionais (RF)
* **RF01 - Cadastro de Demandas:** O sistema deve permitir o registo de novas demandas contendo ID único, título, solicitante, prioridade, CEP e cidade.
* **RF02 - Validação de Dados:** O sistema deve validar se os campos obrigatórios estão preenchidos e impedir IDs duplicados.
* **RF03 - Consulta de API (ViaCEP):** O sistema deve consultar automaticamente a API pública do ViaCEP a partir do CEP informado para preencher o campo da cidade de forma dinâmica.
* **RF04 - Listagem de Demandas:** O sistema deve listar todas as demandas registadas em memória.
* **RF05 - Busca de Demandas:** O sistema deve permitir a procura de demandas por ID ou título.
* **RF06 - Atualização de Status:** O sistema deve permitir alterar o status de uma demanda existente (ex: Pendente para Concluído).
* **RF07 - Exclusão de Demandas:** O sistema deve permitir remover uma demanda com base no seu ID único.

---

## 🛠️ Requisitos Não Funcionais (RNF)
* **RNF01 - Linguagem:** Desenvolvido em **Python** (versão 3.13 ou superior), utilizando apenas bibliotecas nativas (`json`, `urllib`).
* **RNF02 - Arquitetura Modular:** O código deve estar separado entre o script principal (`gerenciador_demandas.py`) e o módulo de funções auxiliares (`utils.py`).
* **RNF03 - Tratamento de Erros:** O sistema deve ser resiliente a falhas de rede (na API) e entradas incorretas do utilizador através de blocos `try-except` e validações.
* **RNF04 - Interface:** Interface textual limpa e interativa executada via terminal/CLI.
