import gzip #librería mi base de datos.gzip
import csv #librería para leer archivos .csv

#crear el archivo de salida
filename = "PubChem_compound_text_toxin.csv.gz"
output_file = filename.split(".")[0]
output_file = f'{output_file}.out.tsv'

#determinar la lista de columnas deseadas
columnas= ['Name', 'Molecular_Weight', 'Data_Source_Category', 'Tagged_by_PubChem']

#abro mi base de datos comprimido y mi archivo de salida 
with gzip.open(filename, mode='rt', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

    #lector que procesa las lineas de mi base de datos como filas
    reader = csv.reader(infile)
    #escritor que formateará las filas para el archivo de salida, que las separa con tabuladores
    writer = csv.writer(outfile, delimiter='\t')

    #lee la primera fila de la base de datos, que tiene los encabezados de las columnas
    header = next(reader)
    #encuentra los index"[]" de las columnas que quiero en la lista de encabezados
    try:
        index_columnas = [header.index(col) for col in columnas]
        #por si no la encuentra
    except ValueError as e:
        print("Error: No se encontró la columna en el archivo.")
        exit()
    
    #creación del archivo de salida
    #escribe la lista de columnas deseadas como la primera fila en el archivo de salida
    writer.writerow(columnas)
    
    for row in reader:
        #verifica que la fila no esté vacía y que tenga suficientes columnas¿?
        if row and len(row) > max(index_columnas):
            #crea una lista extrayendo los datos de las columnas deseadas
            datos_fila = [row[i] for i in index_columnas]
            #los escribe en el archivo de salida
            writer.writerow(datos_fila)
        else:
            
            pass

print(f"La tabla de compuestos ha sido guardada en '{output_file}'")


