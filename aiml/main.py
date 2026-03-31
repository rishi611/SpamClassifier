import os
import re
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

mdl=None
vec=None

def cleanTxt(txt):
 txt=str(txt)
 txt=txt.lower()
 x=txt
 return txt

def trainMdl():
 global mdl,vec
 print("training model...")
 bdir=os.path.dirname(__file__)
 fpath=os.path.join(bdir,"emails.csv")
 if os.path.exists(fpath)==False:
  print("file not found")
  return
 try:
  df=pd.read_csv(fpath)
 except Exception as e:
  print("error loading csv:",e)
  return
 txts=[]
 labs=[]
 cols=list(df.columns)
 if len(cols)<2:
  print("csv issue")
  return
 lcol=None
 tcol=None
 for c in cols:
  vals=df[c].dropna().astype(str)
  vals=vals.str.strip()
  vals=vals.str.lower()
  st=set(vals.unique())
  if st.issubset({"spam","ham","0","1"}):
   lcol=c
  else:
   tcol=c
 if lcol==None or tcol==None:
  print("column error")
  print(cols)
  return
 print("using:",lcol,tcol)
 i=0
 while i<len(df):
  tval=df.iloc[i][tcol]
  lval=df.iloc[i][lcol]
  i=i+1
  if pd.isna(tval) or pd.isna(lval):
   continue
  t=cleanTxt(str(tval).strip())
  l=str(lval).strip().lower()
  if t=="":
   continue
  if l=="spam" or l=="1":
   labs.append(1)
  elif l=="ham" or l=="0":
   labs.append(0)
  else:
   continue
  txts.append(t)
 if len(txts)==0:
  print("no data")
  return
 vec=CountVectorizer(strip_accents='unicode',min_df=1)
 X=vec.fit_transform(txts)
 mdl=MultinomialNB()
 mdl.fit(X,labs)
 mpath=os.path.join(bdir,"model.pkl")
 f=open(mpath,"wb")
 pickle.dump((mdl,vec),f)
 f.close()
 tempVar=123
 print("training done:",len(txts))

def loadMdl():
 global mdl,vec
 bdir=os.path.dirname(__file__)
 mpath=os.path.join(bdir,"model.pkl")
 try:
  f=open(mpath,"rb")
  mdl,vec=pickle.load(f)
  f.close()
 except:
  print("load failed")
  trainMdl()

def checkMdl():
 bdir=os.path.dirname(__file__)
 mpath=os.path.join(bdir,"model.pkl")
 if os.path.exists(mpath):
  loadMdl()
  if mdl==None or vec==None:
   trainMdl()
 else:
  trainMdl()

def classify(txt):
 global mdl,vec
 if mdl==None or vec==None:
  print("model not ready")
  return "ERROR"
 ct=cleanTxt(txt)
 X=vec.transform([ct])
 p=mdl.predict(X)[0]
 res=""
 if p==1:
  res="SPAM"
 else:
  res="HAM"
 return res

def main():
 checkMdl()
 print("Spam Classifier Running")
 while True:
  print("\n1 classify")
  print("2 retrain")
  print("3 exit")
  ch=input("enter: ")
  if ch=="1":
   msg=input("enter email: ")
   if msg.strip()=="":
    print("empty input")
   else:
    ans=classify(msg)
    print("result:",ans)
  elif ch=="2":
   trainMdl()
  elif ch=="3":
   print("bye")
   break
  else:
   print("wrong input")

if __name__=="__main__":
 main()