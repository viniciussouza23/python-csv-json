import pandas as pd
import json
import csv
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Função para mesclar dados de CSV e JSON e salvá-los em um novo arquivo CSV
def merge_csv_and_json_to_csv(csv_file, json_file, output_csv):
    print("Carregando dados do CSV...")
    # Carregar dados do CSV para um DataFrame do Pandas
    csv_data = pd.read_csv(csv_file, header=None, names=['id', 'user_id', 'user_state', 'user_manager'])

    print("Carregando dados do JSON...")
    # Carregar dados do JSON
    with open(json_file) as json_file:
        json_data = json.load(json_file)

    # Extrair informações relevantes do JSON
    db_list = json_data['db_list']
    json_records = []
    for record in db_list:
        # Extrair informações do proprietário
        owner_name = record['owner']['name'] if 'name' in record['owner'] else ''
        owner_uid = record['owner']['uid'] if 'uid' in record['owner'] else ''
        owner_email = record['owner']['email'] if 'email' in record['owner'] else ''

        json_records.append({
            'db_list/dn_name': record['dn_name'],
            'db_list/classification/confidentiality': record['classification'].get('confidentiality', ''),
            'db_list/classification/integrity': record['classification'].get('integrity', ''),
            'db_list/classification/availability': record['classification'].get('availability', ''),
            'db_list/owner/name': owner_name,
            'db_list/owner/uid': owner_uid,
            'db_list/owner/email': owner_email,
            'db_list/time_stamp': record['time_stamp']
        })

    # Criar um DataFrame do Pandas para os dados do JSON
    json_df = pd.DataFrame(json_records)

    # Mesclar DataFrames do CSV e JSON em uma coluna comum, por exemplo, 'userid'
    print("Mesclando DataFrames do CSV e JSON...")
    merged_df = pd.merge(csv_data, json_df, left_on='user_id', right_on='db_list/owner/uid', how='left')

    # Reorganizar colunas conforme o formato desejado
    output_columns = [
        'id', 'user_id', 'user_state', 'user_manager',
        'db_list/dn_name', 'db_list/classification/confidentiality',
        'db_list/classification/integrity', 'db_list/classification/availability',
        'db_list/owner/name', 'db_list/owner/uid', 'db_list/owner/email',
        'db_list/time_stamp'
    ]
    merged_df = merged_df[output_columns]

    # Salvar o DataFrame mesclado em um novo arquivo CSV
    print(f"Salvando DataFrame mesclado em {output_csv}...")
    merged_df.to_csv(output_csv, index=False)

# Função para importar dados de CSV para o banco de dados MySQL e enviar e-mails
def import_csv_to_mysql(arquivo, tabela):
    print("Conectando ao MySQL...")
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Mercadolivre"
    )

    with open(arquivo, "r") as arquivo_csv:
        reader = csv.reader(arquivo_csv, delimiter=",")

        cursor = connection.cursor()

        # Criar a tabela com as colunas corretas
        print("Criando tabela no MySQL...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS challenger (
                id INT,
                user_id VARCHAR(255),
                user_state  VARCHAR(255),
                user_manager VARCHAR(255),
                db_list_dn_name VARCHAR(255),
                db_list_classification_confidentiality VARCHAR(255),
                db_list_classification_integrity VARCHAR(255),
                db_list_classification_availability VARCHAR(255),
                db_list_owner_name VARCHAR(255),
                db_list_owner_uid VARCHAR(255),
                db_list_owner_email VARCHAR(255),
                db_list_time_stamp DATETIME
            )
        """)

        # Ignorar a primeira linha do CSV
        next(reader)

        # Inserir os dados do CSV na tabela
        print("Inserindo dados do CSV no MySQL...")
        for linha in reader:
            cursor.execute(
                "INSERT INTO challenger VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                linha
            )

        # Adicione este trecho após a inserção de dados
        print("Selecionando dados do MySQL high em qualquer campo...")
        cursor.execute("SHOW COLUMNS FROM challenger")
        columns = [column[0] for column in cursor.fetchall()]

        high_confidentiality_rows = []
        for column in columns:
            cursor.execute(f"SELECT * FROM challenger WHERE {column} = 'high'")
            high_confidentiality_rows.extend(cursor.fetchall())

        for row in high_confidentiality_rows:
            print(f"Enviando e-mail para {row[3]} com status High da Tabela {row[4]}...")
            send_email(row[4], row[3], row[3], row)  # Assumindo que db_list_owner_email está na posição 10

        connection.commit()
        connection.close()

# Função para enviar um e-mail
def send_email(to_email, user_manager_email, user_id, database_row):
    # Configurações do servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "python.mercadolibre@gmail.com"
    smtp_password = "willrzafeqxibgak"

    # Configurar e-mail
    subject = "Alerta de alta confidencialidade! "
    
    # Construir o corpo do e-mail com informações detalhadas
    body = f"""
    Olá {database_row[3]}, 
    
    Espero que este e-mail o encontre bem. Gostaria de informar sobre uma situação crítica relacionada à alta confidencialidade de dados de um usuário sob sua supervisão.


    Detalhes do Usuário:
    - ID do Usuário: {database_row[0]}
    - Nome do Usuário: {database_row[8]}
    - Usuario: {database_row[1]}
    - Status Atual do Usuário: {database_row[2]}
    - Nome do Banco: {database_row[4]}
    - Outras informações conforme necessário...

    Por favor, tome as medidas imediatas para revisar e proteger essas informações. Se precisar de mais detalhes, estou à disposição.
    
    Solicito que, após revisar esta informação, confirme recebimento deste e-mail respondendo com um "ok" ou uma breve confirmação.

    Atenciosamente,
    Team Security - Mercado Livre

    Linha completa do banco de dados:
    {database_row}
    """

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = user_manager_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Configurar conexão SMTP e enviar e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, user_manager_email, msg.as_string())

if __name__ == "__main__":
    merge_csv_and_json_to_csv("user_manager.csv", "dblist.json", "dados-mesclados.csv")
    import_csv_to_mysql("dados-mesclados.csv", "challenger")
