import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import LatentDirichletAllocation as LDA

from wordcloud import WordCloud

import base64
from base64 import b64encode
from io import BytesIO


def extract_digest(df: pd.DataFrame, keywords: list[str]):
    """
    Функция возвращает набор дайджестов, а также изображение - облако тегов

    Args:

    df - PandasDataframe со срезом новостей, уже очищенные и лемматизиованные колонки
    ['url', 'title', 'text', 'date', 'url_preview', 'text_prepared2', 'title_prepared2']

    keywords - list ключевых слов для фильтации тем для данного типа пользователя

    """

    # кластеризация
    text_to_clusterize = df["text_prepared2"].apply(lambda x: " ".join(x)).values
    v = TfidfVectorizer()
    x = v.fit_transform(text_to_clusterize)
    df_tmp = df.copy()
    df_tmp["tf-idf"] = pd.Series(list(x.toarray()))
    n_clusters = 10
    model = KMeans(n_clusters=n_clusters, init="k-means++", max_iter=200, n_init=10)
    model.fit(x)
    labels = model.labels_
    df_tmp["labels"] = labels

    # выделение тем из кластеров
    result = []
    for idx, label in enumerate(set(labels)):
        cluster_df = df_tmp[df_tmp["labels"] == label]
        if not len(cluster_df):
            continue
        news_ids = cluster_df.index.to_list()
        cluster_news = cluster_df["text_prepared2"].to_list()
        cluster_words = []
        for itm in cluster_news:
            for i in itm:
                cluster_words.append(i)
        count_vect = CountVectorizer()
        x_counts = count_vect.fit_transform(cluster_words)
        x_counts.todense()
        tfidf_transformer = TfidfTransformer()
        x_tfidf = tfidf_transformer.fit_transform(x_counts)
        dimension = 1  # число кластеров/тем
        lda = LDA(n_components=dimension)
        lda_array = lda.fit_transform(x_tfidf)
        topic_length = 5  # число слов в теме
        components = [lda.components_[i] for i in range(len(lda.components_))]
        features = count_vect.get_feature_names()
        important_words = [
            sorted(features, key=lambda x: components[j][features.index(x)], reverse=True)[:topic_length]
            for j in range(len(components))
        ]

        long_string = ",".join(list(cluster_df["text_prepared2"].apply(lambda x: ",".join(x)).values))
        wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color="steelblue")
        # Generate a word cloud
        wordcloud.generate(long_string)
        # Visualize the word cloud
        image = wordcloud.to_image()

        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_b64str = base64.b64encode(buffered.getvalue())

        result.append(
            {
                "topic": important_words[0],
                "title": cluster_df["title"].iloc[0],
                "news": news_ids,
                "image_tags": img_b64str,
            }
        )

    result_filtered = []
    for itm in result:
        if bool(set(itm["topic"]) & set(keywords)):
            result_filtered.append(itm)

    return result_filtered
