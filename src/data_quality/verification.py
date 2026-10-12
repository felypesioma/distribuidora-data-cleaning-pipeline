from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_dir = BASE_DIR / "data"

def duplicates_count(df):
    df_limpo = df.drop_duplicates()
    return (len(df) - len(df_limpo))

def verification():
    
    df_clientes = pd.read_csv(data_dir / "clientes_crm.csv", delimiter=';')
    if df_clientes.empty:
        raise Exception("Dataframe clientes_crm.csv is empty.")
    
    df_produtos = pd.read_csv(data_dir / "produtos_erp.csv")
    if df_produtos.empty:
        raise Exception("Dataframe produtos_erp.csv is empty.")
    
    df_vendas = pd.read_csv(data_dir / "vendas_erp.csv", delimiter=';')
    if df_vendas.empty:
        raise Exception("Dataframe vendas_erp.csv is empty.")

    print("Starting clientes verification")
    duplicates = duplicates_count(df_produtos)
    print("Number of duplicates: ", duplicates)
    nulls = df_clientes.isnull().sum()
    print(nulls)
    
    print("Starting produtos verification")
    duplicates = duplicates_count(df_produtos)
    print("Number of duplicates: ", duplicates)
    nulls = df_produtos.isnull().sum()
    print(nulls)
    
    print("Starting vendas verification")
    duplicates = duplicates_count(df_vendas)
    print("Number of duplicates: ", duplicates)
    nulls = df_vendas.isnull().sum()
    print(nulls)

verification()