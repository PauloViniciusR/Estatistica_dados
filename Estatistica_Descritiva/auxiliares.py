import pandas as pd


def tabela_distribuicao_frequencias(dataframe, coluna):
    """Cria uma tabela de distribuição de frequências para uma coluna de um dataframe.
    Espera uma coluna categórica.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Dataframe com os dados.
    coluna : str
        Nome da coluna categórica.

    Returns
    -------
    pd.DataFrame
        Dataframe com a tabela de distribuição de frequências.
    """ 
    
    df_estatistica = pd.DataFrame()
    
    df_estatistica["frequencia"] = dataframe[coluna].value_counts().sort_index()
    df_estatistica["frequencia_relativa"] = dataframe[coluna].value_counts(normalize=True).sort_index()
    df_estatistica["frequencia_acumulada"] = df_estatistica["frequencia"].cumsum()
    df_estatistica["frequencia_relativa_acumulada"] = df_estatistica["frequencia_relativa"].cumsum()
    
    return df_estatistica
