import sys
import pandas as pd

if __name__ == '__main__':
    args = sys.argv
    file_path = args[1].replace('.zip', '')
    df = pd.read_csv(file_path, encoding='utf-8')
    prefecture_name_list = set(df['都道府県名_英字'].tolist())
    for prefecture_name in prefecture_name_list:
        prefecture_df = df.query(f'都道府県名_英字 == "{prefecture_name}"')
        with open(f'provide_data/{prefecture_name}.csv', 'w', encoding='utf-8') as f:
            f.write(prefecture_df.to_csv())
