# Apresentação no GitHub: Sistema de Integração e Notificação

## Visão Geral
Este projeto envolve a fusão de dados de arquivos CSV e JSON, a importação dos dados mesclados em um banco de dados MySQL usando o XAMPP e a notificação de partes interessadas por e-mail sobre situações críticas de dados. O script em Python fornecido realiza essas tarefas de maneira eficiente.

### Recursos
1. **Mesclar Dados de CSV e JSON**
   - Combinar dados de um arquivo CSV ("user_manager.csv") e de um arquivo JSON ("dblist.json").
   - Organizar e salvar os dados mesclados em um novo arquivo CSV ("dados-mesclados.csv").

2. **Importar Dados para o Banco de Dados MySQL (XAMPP)**
   - Certifique-se de que o XAMPP com o MySQL está em execução.
   - Baixe o XAMPP no [site oficial](https://www.apachefriends.org/index.html).
   - Instale o XAMPP seguindo as instruções do [guia de instalação](https://www.apachefriends.org/download.html).
   - Inicie os serviços Apache e MySQL no painel de controle do XAMPP.
   - Acesse o phpMyAdmin no navegador (geralmente em http://localhost/phpmyadmin/).
   - Crie um novo banco de dados chamado "MercadoLivre".

3. **Notificação por E-mail**
   - Detectar linhas com alta confidencialidade na tabela MySQL.
   - Enviar notificações por e-mail aos gerentes de usuários para ação imediata.

## Instruções

### Requisitos
- Python
- pandas
- mysql-connector
- smtplib (integrado)
- email.mime (integrado)
- XAMPP (com MySQL)

### Uso
1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/viniciussouza23/python-csv-json.git
   cd python-csv-json
