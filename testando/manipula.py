import pandas as pd

dados = pd.read_json("dados.json")

pd.set_option("display.max_rows", None, "display.max_columns", None)

visualisa_intevalo_atualizacao = dados["Dose 1"].drop_duplicates()

def compara_cdata_duplicates(data_frame,tipo,data):
    visualisa_intevalo_atualizacao = data_frame[tipo].drop_duplicates()
    lista_datas = []
    for index in visualisa_intevalo_atualizacao.index:
        data_valores = data_frame[data].iloc[index]
        lista_datas.append(data_valores)


    visualisa_intevalo_atualizacao = visualisa_intevalo_atualizacao.to_frame()

    visualisa_intevalo_atualizacao[data] = lista_datas

    print(visualisa_intevalo_atualizacao)

compara_cdata_duplicates(dados,"Doses Unicas","Data")
compara_cdata_duplicates(dados,"Dose 1","Data")
compara_cdata_duplicates(dados,"Dose 2","Data")
compara_cdata_duplicates(dados,"Total percentagem","Data")
