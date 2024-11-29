# Import necessari
import os
import json
import re
from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def create_unique_folder(base_name: str) -> Path:
    """
    Crea una cartella con un nome unico basato su un nome di base.
    Se la cartella esiste già, aggiunge un numero progressivo.
    
    Parametri:
    base_name : str
        Il nome base della cartella da creare.

    Restituisce:
    Path
        Il percorso completo della cartella creata.
    """
    base_path = Path(base_name)
    folder_path = base_path

    # Crea una nuova cartella unica
    counter = 1
    while folder_path.exists():
        folder_path = base_path.with_name(f"{base_name}_{counter}")
        counter += 1

    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path


def analyze_and_plot_fixed(
    dataframe: pd.DataFrame, 
    base_path: str = None, 
    radius: float = 0.30, 
    savefig: bool = False, 
    agg_plot: bool = False
) -> list:
    """
    Analizza un dataframe per categorie, calcola correlazioni significative, 
    salva heatmap, JSON, e opzionalmente crea scatterplot per le colonne correlate.

    Parametri:
    dataframe : pd.DataFrame
        Il dataframe contenente i dati da analizzare.
    base_path : str, opzionale
        Il percorso di base dove salvare le heatmap e i file JSON. Se non fornito, 
        verrà utilizzato il percorso corrente.
    radius : float, opzionale
        Il valore minimo della correlazione che viene considerata significativa.
    savefig : bool, opzionale
        Se True, salva le heatmap come immagini PNG.
    agg_plot : bool, opzionale
        Se True, salva gli scatterplot per le colonne correlate.

    Restituisce:
    list
        Una lista contenente i gruppi di correlazioni per ogni colonna categorica.
    """
    
    # Controllo per valori NaN
    if dataframe.isna().sum().sum() > 0:
        raise ValueError("Il DataFrame contiene valori NaN. Si prega di rimuoverli prima di procedere.")
    
    # Se base_path non è fornito, usa il percorso corrente
    if base_path is None:
        base_path = '/'

    # Categorie nel dataframe
    cat_col = dataframe.select_dtypes(include='object').columns

    if not cat_col.any():
        raise ValueError("Il DataFrame non contiene colonne categoriali.")
    
    filtered_corr_list_total = []

    # Crea la cartella per le heatmap
    base_folder = create_unique_folder("Categorical_Filtered_Heatmaps")
    
    # Elenco delle correlazioni filtrate
    for category in cat_col:
        filtered_corr_list = []

        # Valori unici della colonna
        unique_values = dataframe[category].unique()

        for value in unique_values:
            # Filtra il DataFrame
            df_filtered = dataframe[dataframe[category] == value]
            
            if df_filtered.empty:
                continue

            # Nome del gruppo
            group_name = str(df_filtered[category].iloc[0]).replace("/", "-")  # Gestione caratteri speciali
            
            # Rimuovi le colonne non necessarie
            df_cleaned = df_filtered.drop(cat_col, axis=1, errors='ignore')
            
            # Calcola la matrice di correlazione
            corr_matrix = df_cleaned.corr()

            # Filtra correlazioni significative
            filtered = corr_matrix.where(((corr_matrix > radius) | (corr_matrix < -radius)) & (corr_matrix != 1)).stack()
            filtered_corr_list.append((f'{category} name: {group_name}', filtered))

            # Salva i grafici, se richiesto
            if savefig:
                save_path = base_folder / category
                save_path.mkdir(exist_ok=True)
                
                plt.figure(figsize=(10, 8))
                sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
                plt.title(f'Heatmap for {category}: {group_name}')
                plt.savefig(f'{save_path}/{group_name}_heatmap.png', bbox_inches='tight')
                plt.close()

            # Crea gli scatterplot, se richiesto
            if agg_plot:
                correlated_columns = filtered.index.get_level_values(0).to_list()
                agg_plot_data = df_filtered[correlated_columns]
                if len(correlated_columns) > 1:
                    x_col, y_col = agg_plot_data.columns[:2]
                    sns.scatterplot(data=df, x=x_col, y=y_col, palette='Set1')
                    plt.title(f'Jointplot for {category}: {group_name}')
                    plt.savefig(f'{save_path}/{group_name}_scatterplot.png', bbox_inches='tight')
                    plt.close()

        filtered_corr_list_total.append((category, filtered_corr_list))

    # Salva le correlazioni in un file JSON
    filtered_dict = {
        category: {group_name: corr.tolist() for group_name, corr in filtered_corr_list}
        for category, filtered_corr_list in filtered_corr_list_total
    }
    
    json_file_path = base_folder / "correlations.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(filtered_dict, json_file, indent=4)

    return filtered_corr_list_total


# Esempio di utilizzo
if __name__ == "__main__":
    # Assumiamo di avere un DataFrame 'df' pronto per l'analisi
    df = pd.DataFrame({
        'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value1': [1, 2, 3, 4, 5, 6],
        'Value2': [6, 5, 4, 3, 2, 1]
    })

    result = analyze_and_plot_fixed(
        df,
        savefig=True,  # Imposta True per salvare le heatmap
        agg_plot=True  # Imposta True per salvare gli scatterplot
    )
