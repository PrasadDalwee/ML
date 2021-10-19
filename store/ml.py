import pandas as pd
import os
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df=pd.read_csv("amazon.csv")
print(df[1])

df = df.iloc[:3]
for i, p in df.iterrows():
    print(p.description)


# df1 = df[['description']]
# tfidf = TfidfVectorizer(stop_words='english')
# df1['description'] = df1['description'].fillna('')

# overview_matrix = tfidf.fit_transform(df1['description'])
# similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
# mapping = pd.Series(df.index,index = df['product_name'])


# def recommend(df_input):
#     df_index = mapping[df_input]
#     similarity_score = list(enumerate(similarity_matrix[df_index]))
#     similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
#     similarity_score = similarity_score[1:15]
#     df_indices = [i[0] for i in similarity_score]
#     return (df['product_name'].iloc[df_indices])



# for i, p in df.iterrows():
#     name = p['product_name']
#     price = p['price']
#     brand = p['manufacturer']
#     description = p['description']
#     technical_specs = p['product_information']
#     new_product = Product(
    
#     name = name,
#     price = price,
#     digital = False,
#     brand = brand,
#     description = description,
#     technical_specs = technical_specs,

#     )
#     new_product.save()

# print("success!!!")