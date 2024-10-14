import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


#Criando banco de dados/
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#Criando conexão comn banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#Criando tabela

Base = declarative_base() # Caracterrísticas que irá trazer para  minha classe 

#Quando trazemos uma classe, criamos um objeto
class Cliente(Base):
    #Tabela clientes 
    __tablename__ = "clientes"

    #Definindo campos de tabela.
    id = Column("id", Integer, primary_key= True, autoincrement= True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    senha = Column("senha", String)

    def __init__(self, nome: str, sobrenome: str, senha: str):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.senha = senha

#Criando tabela no banco de dados 
Base.metadata.create_all(bind=MEU_BANCO)


# CRUD 
# Create - Insert - Salvar.
os.system("cls || clear")
print("Solicitando dados para o usário: ")
inserir_nome = input("Digite seu nome: ")
inserir_sobrenome = input("Digite seu email: ")
inserir_senha = input("Digite seu senha: ")


cliente = Cliente(nome = inserir_nome, sobrenome= inserir_sobrenome, senha=inserir_senha)
session.add(cliente)# É um insert, vai adicionar valores 
session.commit()# Grava as informaçõesw no banco de dados 



#Read - Select - Consulta
print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.sobrenome} - {cliente.senha}")



#U - UPDATE - Atualizar 
print("\nAtualizando dados do usuário.")
sobrenome_cliente = input("Diigte o sobrenome do cliente que será atualizado:")

cliente = session.query(Cliente).filter_by(sobrenome = sobrenome_cliente).first()

if cliente:
    cliente.nome = input("Digite seu nome: ")
    cliente.sobrenome = input("Digite seu sobrenome: ")
    cliente.senha = input("Digite seu senha: ")

    session.commit()

else:
    print("Cliente não encontrado.")


#Read - Select - Consulta
print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.sobrenome} - {cliente.senha}")


#D - Delete - DELETE - Excluir 
print("\nExcluindo dados do usuário.")
email_cliente = input("Digite o sobrenome do cliente que será excluido:")

cliente = session.query(Cliente).filter_by(sobrenome = email_cliente).first()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome} excluido com sucesso!")

else:
    print("Cliente não encontrado")



#R - SELECT - CONSULTA 
print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.sobrenome} - {cliente.senha}")


#R - SELECT - CONSULTA
print("\nConsultando os dados de um cliente.")
id_cliente = input("Digite o id do cliente:")
cliente = session.query(Cliente).filter_by(id = id_cliente).first()
"""email_cliente = input("Digite o email do cliente:")
cliente = session.query(Cliente).filter_by(email = email_cliente).first()
"""
if cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.sobrenome} - {cliente.senha}")

else:
    print("Cliente não encontrado")
