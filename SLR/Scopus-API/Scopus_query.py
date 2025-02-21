from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json

## Carica la configurazione dal file config.json
with open("config.json", "r") as con_file:
    config = json.load(con_file)

## Inizializza il client Scopus
client = ElsClient(config["apikey"])
client.inst_token = config["insttoken"]

## 🔍 Definizione della tua query Scopus
query = """
( TITLE-ABS-KEY ("systemic risks" OR "systemic risk" OR "credit rating" OR "credit ratings" 
OR "probability of default" OR "credit risk assessment" OR "copulas" OR "credit derivatives" 
OR "credit score cards" OR "risk modelling" OR "counterparty risk" OR "lending risk" OR 
"financial stability" OR "tail dependence" OR "early warning system" OR "CDS" OR "PD" 
OR "loans" OR "borrowers" OR "default" OR "defaults" OR "bankruptcy" OR "failure" OR 
"financial distress" OR "financial crisis" OR "stress test*") ) 
AND ( TITLE-ABS-KEY ( "machine learning" OR "ML" OR "DP" OR "RL" OR "NN" OR "deep learning" 
OR "neural network" OR "artificial intelligence" OR "AI" OR "predictive modelling" OR 
"forecast" OR "reinforcement learning" OR "big data" OR "computational finance" OR 
"transition matrices" OR "econometrics" OR "synthetic data" OR "spatial data" OR "kernel" 
OR "spatial finance" OR "fuzzy" OR "GAN" OR "generative adversarial networks" OR "GNN" 
OR "graph neural networks" ) ) 
AND ( TITLE-ABS-KEY ( "sustainability" OR "risk mitigation" OR "ESG integration" OR 
"climate risk" OR "green credit scoring" OR "ESG credit scoring" OR "sustainable credit risk" 
OR "environmental credit risk" OR "green finance" OR "extreme events" OR "transition risk" 
OR "physical risk" OR "ESG" OR "carbon footprint" OR "catastrophic bond" OR 
"Sustainability-linked loans" OR "ESG scoring" OR "environmental risk") ) 
AND ( LIMIT-TO ( SUBJAREA,"COMP" ) OR LIMIT-TO ( SUBJAREA,"MATH" ) OR LIMIT-TO ( SUBJAREA,"ECON" ) 
OR LIMIT-TO ( SUBJAREA,"BUSI" ) ) AND ( LIMIT-TO ( DOCTYPE,"ar" ) ) AND ( LIMIT-TO ( LANGUAGE,"English" ) )
"""

## 🔎 Esegui la ricerca su Scopus
doc_search = ElsSearch(query, "scopus")
doc_search.execute(client, get_all=True)

## 📄 Stampa i risultati della ricerca
print(f"📄 Trovati {len(doc_search.results)} documenti.")
if len(doc_search.results) > 0:
    print("\n📌 Esempio di primi 5 documenti trovati:")
    for doc in doc_search.results[:5]:  # Mostra solo i primi 5
        print(f"- {doc['dc:title']} ({doc['prism:coverDate']})")

