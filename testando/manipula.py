import pandas as pd

dados = pd.read_json("dados.json")

pd.set_option("display.max_rows", None, "display.max_columns", None)

visualisa_intevalo_atualizacao = dados["Dose 1"].drop_duplicates()

def cria_df_time_stamp(data_frame):
    tamanho_df = len(data_frame.index)
    lista_datas_time_stamp = []
    for index in range(tamanho_df):
        temporario = pd.Timestamp(data_frame["Data"][index])
        lista_datas_time_stamp.append(temporario)
    #armazenando timestamp
    data_frame_datas_timestamp = pd.DataFrame(lista_datas_time_stamp,columns = ["Timestamp"])
    return (data_frame_datas_timestamp)

def compara_cdata_duplicates(data_frame,tipo,data):
    visualisa_intevalo_atualizacao = data_frame[tipo].drop_duplicates()
    lista_datas = []
    dias_diff = visualisa_intevalo_atualizacao.index
    print(dias_diff)
    #media de dias de atuaizaçao
    for i in range(len(dias_diff)-1):
        if (i == 0):
            soma = 0
        diff = dias_diff[i+1] - dias_diff[i]
        soma += diff
    media = (soma/len(dias_diff))
    

    for index in dias_diff:
        data_valores = data_frame[data].iloc[index]
        lista_datas.append(data_valores)
    
    #transforma em df para append 
    visualisa_intevalo_atualizacao = visualisa_intevalo_atualizacao.to_frame()
    
    #adicinona coluna com conteudo de lista_datas
    visualisa_intevalo_atualizacao[data] = lista_datas

    print(visualisa_intevalo_atualizacao)
    print("Media de dias ate a atualizaçao dos dados sobre {} {:.2f}\n".format(tipo,media))

compara_cdata_duplicates(dados,"Doses Unicas","Data")
compara_cdata_duplicates(dados,"Dose 1","Data")
compara_cdata_duplicates(dados,"Dose 2","Data")
compara_cdata_duplicates(dados,"Total percentagem","Data")

lista_time_stamp = cria_df_time_stamp(dados)

df_time_stamp = pd.DataFrame(lista_time_stamp,columns = ["Timestamp"])

print(df_time_stamp.head())
