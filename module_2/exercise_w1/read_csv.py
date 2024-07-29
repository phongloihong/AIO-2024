import numpy as np
import pandas as pd


def get_max_sales(data):
    print(data[:, 3].argmax())
    print(data[:, 3].max())


def mean_tv(data):
    print(data[:, 0].mean())


def count_sales(data, max):
    print(len(np.where(data[:, 3] >= max)[0]))


def mean_radio(data, min_sales):
    filtered_indexes = np.where(data[:, 3] >= min_sales)[0]
    print(data[filtered_indexes][:, 1].mean())


def total_sale_by_avg_news_paper(data):
    mean_newspaper = data[:, 2].mean()
    filtered_data = data[np.where(data[:, 2] >= mean_newspaper)]
    print(filtered_data[:, 3].sum())


def calculate_scores_by_mean_sales(data):
    mean_sales = data[:, 3].mean()
    scores = np.where(data[:, 3] < mean_sales, "Bad", np.where(
        data[:, 3] == mean_sales, "Average", "Good"))
    print(scores[7:10])


def calculate_scores_by_median_sales(data):
    mean_sales = int(data[:, 3].mean())
    a = data[:, 3][mean_sales]
    scores = np.where(data[:, 3] < a, "Bad", np.where(
        data[:, 3] == a, "Average", "Good"))
    print(scores[7:10])


df = pd.read_csv('./data/ads.csv')
data = df.to_numpy()
calculate_scores_by_median_sales(data)
