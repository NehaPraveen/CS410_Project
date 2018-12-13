import pandas as pd
import numpy as np
import math

class BM25 :
    def __init__(self, dataframe) :
        self.df=dataframe
        self.corpus=[]
        self.docfreq_dict = {}
        self.M = len(self.df.columns.tolist()) 
        self.DocAvgLen = 0
        self.DocLen = []
        self.DocIDF={}
        self.buildDocDictionary()
        self.IDF_Generator()
        

    def buildDocDictionary(self) : 
        docTotalLen = 0            
        for j in range(len(self.df.columns.tolist())):
            doc=(self.df.iloc[:,j]).tolist()
            self.DocLen.append(np.sum(self.df.iloc[:,j]!=0))
            doc_bow={}
            for ind,val in enumerate(doc):
                doc_bow[ind]=val
            self.corpus.append(doc_bow)              
            docTotalLen +=np.sum(self.df.iloc[:,j]!=0)              
        self.DocAvgLen = docTotalLen / self.M  
        
                


    def IDF_Generator(self) :
        #calculating doc freq for each word. 
        fun=(self.df.apply(lambda r: np.sum(r.iloc[0:]!=0),axis=1)).tolist()
        for term,docfreq in enumerate(fun):
            self.docfreq_dict[term]=docfreq 
        for term, docfreq in self.docfreq_dict.items():
             self.DocIDF[term]=math.log10(self.M +1)- math.log10(float(docfreq))

                
         


    def BM25Score(self, Query=[], k1=1.5, b=0.75) :
        query_bow = {}
        scores=[]
        for ind,val in enumerate(Query):
            query_bow[ind]=val
        for idx,doc_bow in enumerate(self.corpus):
            commonTerms = set(query_bow.keys()) & set(doc_bow.keys())
            tmp_score = []
            doc_terms_len = self.DocLen[idx]
            for term in commonTerms :
                upper = (doc_bow[term] * (k1+1))
                below = ((doc_bow[term]) + k1*(1 - b + b*doc_terms_len/self.DocAvgLen))
                tmp_score.append(self.DocIDF[term] * upper / below)
            scores.append(sum(tmp_score))
        return scores

    def TFIDF(self) :       
        tfidf = []
        for doc_bow in self.corpus:
            doc_tfidf  = [(term, tf*self.DocIDF[term]) for term, tf in doc_bow.items()]
            doc_tfidf.sort()
            tfidf.append(doc_tfidf)
        return tfidf   
  




if __name__ == '__main__' :

    dataframe = pd.read_csv('temp.csv')
    bm25 = BM25(dataframe)
    Query = pd.Series([1,2,3]).tolist()
    scores = bm25.BM25Score(Query)
    tfidf = bm25.TFIDF()
    for i, tfidfscore in enumerate(tfidf):
        print(i, tfidfscore)
