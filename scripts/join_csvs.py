import pandas as pd
import os
def main():
    #subdir="hashtags_suicide_en"
    #subdir="hashtags_covid_en_clean_eng"
    subdir="news_eng_clean"
    dir = "../data/accounts/" + subdir
    print(dir)

    dfs = []
    for path in os.listdir(dir):
        print("---------------",path)
        current_path = dir + "/" + path
        for filename in os.listdir(current_path):
            if filename.endswith("csv"):
                print("joining " + filename)
                df = pd.read_csv(current_path + "/" +filename, sep=",")
                df.keyword = filename
                df.path = path
                dfs.append(df)
    df_concat = pd.concat(dfs)
    df_concat.to_csv("../data/output/" + subdir + "_merged.csv")
    print(df_concat)


if __name__ == '__main__':
	main()