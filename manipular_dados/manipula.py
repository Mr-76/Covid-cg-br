import pandas as pd

dados = pd.read_json("dados.json")

pd.set_option("display.max_rows", None, "display.max_columns", None)

def cria_df_time_stamp(data_frame):
    """cria um dataframe com timestamps"""
    datas = pd.to_datetime(data_frame["Data"],format='%d/%m/%Y')
    data_frame_datas_timestamp = datas.to_frame() 
    return (data_frame_datas_timestamp)

def compara_cdata_duplicates(data_frame,tipo1,tipo2):
    """
    compara 2 dataframes 2 colunas
    do dataframe original
    sem valores duplicados
    """


    coluna1 = pd.DataFrame(data_frame[tipo1])

    concatena_colunas = coluna1.assign(data = data_frame[tipo2])

    concatena_colunas = concatena_colunas.drop_duplicates(tipo1)


    return concatena_colunas


U_D = compara_cdata_duplicates(dados,"Total de doses únicas aplicadas","Data")
D1_D = compara_cdata_duplicates(dados,"Total de 1 doses aplicadas","Data")
D2_D = compara_cdata_duplicates(dados,"Total de 2 doses aplicadas","Data")
TP_D = compara_cdata_duplicates(dados,"Percentual da população vacinada","Data")
lista_time_stamp = cria_df_time_stamp(dados)
print(U_D,"\n\n",D1_D,"\n\n",D2_D,"\n\n",TP_D)


