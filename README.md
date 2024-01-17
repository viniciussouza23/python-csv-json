# python-csv-json


Apresentação no GitHub: Sistema de Integração e Notificação
Visão Geral
Este projeto envolve a fusão de dados de arquivos CSV e JSON, a importação dos dados mesclados em um banco de dados MySQL e a notificação de partes interessadas por e-mail sobre situações críticas de dados. O script em Python fornecido realiza essas tarefas de maneira eficiente.

Recursos
Mesclar Dados de CSV e JSON

Combinar dados de um arquivo CSV ("user_manager.csv") e de um arquivo JSON ("dblist.json").
Organizar e salvar os dados mesclados em um novo arquivo CSV ("dados-mesclados.csv").
Importar Dados para o Banco de Dados MySQL

Conectar-se a um banco de dados MySQL ("Mercadolivre").
Criar uma tabela ("challenger") com as colunas necessárias.
Inserir dados mesclados do arquivo CSV na tabela MySQL.
Notificação por E-mail

Detectar linhas com alta confidencialidade na tabela MySQL.
Enviar notificações por e-mail aos gerentes de usuários para ação imediata.
Instruções
Requisitos
Python
pandas
mysql-connector
smtplib (integrado)
email.mime (integrado)
Uso
Clonar o Repositório:

bash
Copy code
git clone https://github.com/seu-nome/seu-repositorio.git
cd seu-repositorio
Instalar Dependências:

bash
Copy code
pip install pandas mysql-connector
Configurar o MySQL:

Certifique-se de que o MySQL está em execução.
Atualize os detalhes de conexão do MySQL no script (host, usuário, senha, banco de dados).
Configurar E-mail:

Atualize os detalhes do servidor SMTP e as credenciais de e-mail no script.
Executar o Script:

bash
Copy code
python script.py
Notas Adicionais
Certifique-se de que o arquivo CSV ("user_manager.csv") e o arquivo JSON ("dblist.json") estejam no diretório do projeto.
O script assume o uso do Gmail para o envio de e-mails. Ajuste os detalhes do SMTP conforme necessário.
Contribuições
Sinta-se à vontade para contribuir abrindo problemas, fornecendo feedback ou enviando solicitações de pull.

Licença
Este projeto é licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.

