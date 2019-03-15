import pandas as pd
import numpy as np
import collections
from sklearn import preprocessing
from config import Config


class DataEncoder(Config):
    config = Config()

    def one_hot_encoder(self, raw_df, config):
        for cat_col in config.ENCODING_CONFIG['CAT_COLS']:
            encoded_df = raw_df[cat_col].astype(str)
            encoded_df[cat_col] = encoded_df[cat_col].str.lower()
            ohe_encoded_df = pd.concat([encoded_df, pd.get_dummies(encoded_df[cat_col],
            prefix=cat_col)], axis=1)
        return ohe_encoded_df

    def binarizer(self, ohe_encoded_df, config):
        for bi_col in config.ENCODING_CONFIG['BINARY_COLS']:
            binarizer = preprocessing.LabelBinarizer(sparse_output=False)
            binarized_col = binarizer.fit_transform(ohe_encoded_df[bi_col])
            ohe_encoded_df[bi_col] = binarized_col
        return ohe_encoded_df

    def size_range_encoder(self):
        # encode size_range
        ordered_size_range = {}
        le_size = preprocessing.LabelEncoder()
        le_size.fit(df['size_range'])
        for range_of_size in list(le_size.classes_):
            ordered_size_range[int(range_of_size.split('-')[0])] = range_of_size
        ordered_size_range = collections.OrderedDict(
            sorted(ordered_size_range.items()))

        ordered_range_list = []
        for _, ordered_range in ordered_size_range.items():
            ordered_range_list.append(ordered_range)

        ordered_range_list.insert(0, '0')
        ordered_range_list.insert(4, '700-799')

        replace_map_comp = {'size_range': {k: v for k, v in
                            zip(ordered_range_list,
                            list(range(1,len(ordered_range_list) + 1)))}}

        df_encoded = df.replace(replace_map_comp, inplace=False)

        return df_encoded

