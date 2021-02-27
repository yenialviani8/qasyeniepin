from Sastrawi.Stemmer.StemmerFactory import StemmerFactory 
import pandas as pd 
import numpy as np 
file_name = "qasbot\\templates\\database.csv"
class Engine:
    tags = {
        1:"Apa",
        2:"Kapan",
        3:"Dimana" 
        
    }
    def __init__(self):
        df = pd.read_csv(file_name,delimiter=';', header=0, index_col=0)
        print(df.columns)
        df['obj'] = df["object"]
        df['keys'] = df["keywords"]
        df.drop(columns=['object', 'keywords'], inplace=True)
        self.database = df
        self.stemmer = StemmerFactory().create_stemmer()
        pass

    def Tokenize(self, teks):
        print("Memulai Tokenisasi..")
        return teks.split(' ')

    def Stem(self, teks):
        print("Memulai Stem..")
        return self.stemmer.stem(teks)

    def Parse(self, teks):
        # [tag] [pred] [object]?
        txt = self.Tokenize(teks)
        tag = txt[0] 
        if tag == "apa": 
            tag = 1
        elif tag == "kapan":
            tag = 2
        elif (tag == "dimana") or (tag == "mana"):
            tag = 3
        elif (tag == "berapa"):
            tag = 4
        else:
            return False, "Kamu mau tanya apa sii | " + tag 
        txt = self.Stem(teks)
        txt = self.Tokenize(txt) 

        db = self.database
        db = db[db.tag == tag] 
        for i in txt [1:]: 
            for _, row in db.iterrows():
                words  = [x.strip()for x in row['obj'].split(',') if x!='']
                if i in words:
                    alias = [x.strip()for x in row['keys'].split(',') if x!='']
                    for j in alias:
                        if j in txt[1:]:
                            return True, row['response']
        return False, "tidak ada jawaban"