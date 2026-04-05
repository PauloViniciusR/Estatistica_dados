import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import shapiro

def tabela_distribuicao_frequencias(dataframe, coluna, coluna_frequencia=False):
    """Cria uma tabela de distribuição de frequências para uma coluna de um dataframe.
    Espera uma coluna categórica.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Dataframe com os dados.
    coluna : str
        Nome da coluna categórica.
    coluna_frequencia : bool
        Informa se a coluna passada ja é com os valores de frequencia ou não. Padão: False

    Returns
    -------
    pd.DataFrame
        Dataframe com a tabela de distribuição de frequências.
    """ 
    
    df_estatistica = pd.DataFrame()

    if coluna_frequencia:
        df_estatistica["frequencia"] = dataframe[coluna]
        df_estatistica["frequencia_relativa"] = df_estatistica["frequencia"] / df_estatistica["frequencia"].sum()
    else:
        df_estatistica["frequencia"] = dataframe[coluna].value_counts().sort_index()
        df_estatistica["frequencia_relativa"] = dataframe[coluna].value_counts(normalize=True).sort_index()
        
    df_estatistica["frequencia_acumulada"] = df_estatistica["frequencia"].cumsum()
    df_estatistica["frequencia_relativa_acumulada"] = df_estatistica["frequencia_relativa"].cumsum()
    
    return df_estatistica

#-----------------------------------------------------------------------------------------------------------------------

def composicao_boxplot(dataframe, coluna, intervalos="auto"):
    fig, (ax1, ax2) = plt.subplots(
        nrows=2, 
        ncols=1, 
        sharex=True,
        gridspec_kw={
            "height_ratios": (0.15, 0.85),
            "hspace": 0.02
        }
    )

    sns.boxplot(
        data=dataframe, 
        x=coluna, 
        showmeans=True, 
        meanline=True,
        meanprops={"color": "C1", "linewidth": 1.5, "linestyle": "--"},
        medianprops={"color": "C2", "linewidth": 1.5, "linestyle": "--"},
        ax=ax1,
    )

    sns.histplot(
        data=dataframe, 
        x=coluna, 
        kde=True, 
        bins=intervalos, 
        ax=ax2
    )

    for ax in (ax1, ax2):
        ax.grid(True, linestyle="--", color="gray", alpha=0.5)
        ax.set_axisbelow(True)

    ax2.axvline(dataframe[coluna].mean(), color='C1', linestyle="--", label=("Média"))
    ax2.axvline(dataframe[coluna].median(), color='C2', linestyle="--", label=("Mediana"))
    ax2.axvline(dataframe[coluna].mode()[0], color='C3', linestyle="--", label=("Moda"))


    ax2.legend()

    plt.show()

def analise_shapiro(dataframe, alfa=0.05):
    print("Teste de Shapiro-Wilk")
    for coluna in dataframe.columns:
        estatistica, pvalue = shapiro(dataframe[coluna])
        print(f"{estatistica=:.3f}")
        if pvalue > alfa:
            print(f"{coluna} segue uma distribuição normal (valor p: {pvalue=:.3f})")
        else:
            print(f"{coluna} não segue uma distribuição normal (valor p: {pvalue=:.3f})")
