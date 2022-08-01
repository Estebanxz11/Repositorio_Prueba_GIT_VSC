import pandas as pd

#ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022/blob/3f3847bbf2dbe4b2cf4dcceb96a455d92c88f9c5/movies.csv?raw=true' 

def listaPeliculas(rutaFileXlv: str)-> str:
    if rutaFileXls.split('.')[-1] != 'xls': 
        try:
            xlsx = pd.ExcelFile(rutaFileCsv)
            registroPeliculas = []
            for hojas in xlsx.sheet_names:
                registroPeliculas.append(xlsx.parse(hojas))
            peliculas = pd.concat(registroPeliculas)
        except:  
            print('Error al leer el archivo de datos.')
        subGrupoPeliculas = peliculas[['Country', 'Language', 'Gross Earnings']]
        subGrupoPeliculas.head() #Sub grupo completo [5042 rows x 3 columns]
        gananciaPaisLanguaje = subGrupoPeliculas.pivot_table(index=['Country', 'Languaje'])
        gananciaPaisLanguaje.head()
        print(gananciaPaisLanguaje) #[100 rows x 1 columns]
    else:
        print('Extensión inválida.')
    return 'Fin del registro'
print(listaPeliculas(rutaFileXls))