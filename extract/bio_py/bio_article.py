from Bio import Entrez
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")


def get_article(word):
    Entrez.email = EMAIL    
    handle = Entrez.esearch(db="pubmed", term=word, retmax=1)
    record = Entrez.read(handle)
    handle.close()
    article_id = record["IdList"][0]
    handle = Entrez.efetch(db="pubmed", id=article_id, retmode="xml")
    records = Entrez.read(handle)
    handle.close()

    article_title = records["PubmedArticle"][0]["MedlineCitation"]["Article"]["ArticleTitle"]
    article_abstract = records["PubmedArticle"][0]["MedlineCitation"]["Article"]["Abstract"]["AbstractText"][0]
    article_doi = records["PubmedArticle"][0]["PubmedData"]["ArticleIdList"][1]

    json_object = {"title": article_title,
                    "img_src": "",
                    "text": f"{article_abstract} DOI:{article_doi}"}   
    #print(json_object)
    return json_object

