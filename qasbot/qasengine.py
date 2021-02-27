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
        df['words'] = df["Keyword"] + ', ' + df["Alias"]
        df.drop(columns=['Alias', 'Keyword'], inplace=True)
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
        
        txt = self.Stem(teks)
        txt = self.Tokenize(txt)
        tag = txt[0]
        print (txt)
        if tag == "apa": 
            tag = 1
        elif tag == "kapan":
            tag = 2
        elif tag == "dimana":
            tag = 3
        else:
            return "Kamu mau tanya apa sii | " + tag 

        db = self.database
        db = db[db.tag == tag]
        print (db)
        for i in txt [1:]:
            print (i)
            for index, row in db.iterrows():

                words  = [x.strip()for x in row['words'].split(',') if x!='']
                if i in words:
                    return row['Jawaban']
        return "tidak ada jawaban"