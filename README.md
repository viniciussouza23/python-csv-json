# Apresentação no GitHub: Sistema de Integração e Notificação

## Visão Geral
Este projeto envolve a fusão de dados de arquivos CSV e JSON, a importação dos dados mesclados em um banco de dados MySQL e a notificação de partes interessadas por e-mail sobre situações críticas de dados. O script em Python fornecido realiza essas tarefas de maneira eficiente.

### Recursos
1. **Mesclar Dados de CSV e JSON**
   - Combinar dados de um arquivo CSV ("user_manager.csv") e de um arquivo JSON ("dblist.json").
   - Organizar e salvar os dados mesclados em um novo arquivo CSV ("dados-mesclados.csv").

2. **Importar Dados para o Banco de Dados MySQL**
   - Conectar-se a um banco de dados MySQL ("Mercadolivre").
   - Criar uma tabela ("challenger") com as colunas necessárias.
   - Inserir dados mesclados do arquivo CSV na tabela MySQL.

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

### Uso
1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/seu-nome/seu-repositorio.git
   cd seu-repositorio
