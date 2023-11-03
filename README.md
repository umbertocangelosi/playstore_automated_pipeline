## PLAYSTORE_AUTOMATED_PIPELINE

Questo repository contiene il progetto finale del mio gruppo di lavoro della classe 'Data' del corso di Data Engineering di Develhope, la tech academy dove mi sono formato per 6 mesi con tanta dedizione e meticolosita'. Il repository e' la mia rifinitura del progetto originale a cui hanno partecipato i membri del mio gruppo di lavoro Alessio Spagnolo e Riccardo Convertino che ringrazio assieme al tutor Davide Posillipo. 

### Requisiti

#### Per eseguire la pipeline attraverso il main.py:
python
pandas
matplotlib
seaborn
numpy
psycopg2
sqlalchemy
afinn (https://github.com/fnielsen/afinn)

#### Per eseguire la pipeline attraverso airflow, su cui si basa il progetto, e far partire quindi la DAG e' necessario avere installato correttamente airflow.

### Il progetto
Il progetto "e' scritto in Python e utilizza Apache Airflow per creare un pipeline di elaborazione dei dati che costituisce una ETL completa con visualizzazione dati in una dashboard finale su POWERBI. Il progetto è strutturato in diverse funzioni, ognuna delle quali svolge un compito specifico nel processo di elaborazione dei dati.
Il progetto inizia con l'importazione dei dati da un file CSV ricavato da kaggle riguardante i download delle applicazioni del google playstore, utilizzando la classe DataIngestor per leggere il file e salvare i dati in un dataframe. Questi dati vengono poi puliti utilizzando la classe DataCleaner, che rimuove eventuali errori o anomalie presenti nei dati. Una volta puliti, i dati vengono salvati utilizzando XCom, un meccanismo di Airflow che permette di condividere i dati tra diverse funzioni.
Successivamente, il progetto importa un altro set di dati, questa volta contenente recensioni degli utenti. Anche questi dati vengono puliti utilizzando la classe DataCleaner. Dopo la pulizia, i dati vengono salvati utilizzando XCom.
Il progetto prosegue con la creazione di un database utilizzando la classe DbHandler. I dati puliti vengono poi caricati nel database. Infine, il progetto esegue un'analisi dei dati utilizzando la classe DataAnalyser, che assegna un punteggio di sentiment ai dati basandosi sulle recensioni degli utenti. I risultati dell'analisi vengono poi salvati nel database.
Il progetto utilizza il concetto di Directed Acyclic Graph (DAG) di Airflow per definire l'ordine in cui le funzioni devono essere eseguite. Ogni funzione è definita come un task in Airflow, e le dipendenze tra i task sono definite utilizzando l'operatore >> di Airflow.
In sintesi, il progetto "Automated Pipeline" è un esempio di come utilizzare Python e Apache Airflow per creare un pipeline di elaborazione dei dati automatizzato, che va dall'importazione dei dati alla loro pulizia, analisi e infine al salvataggio dei risultati in un database, per poi poterli visualizzare attraverso la potenza di POWERBI.
