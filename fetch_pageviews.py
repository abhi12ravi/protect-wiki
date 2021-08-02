import pandas as pd
import pageviewapi
import time

def fetch_pageviews(title):
    retry_count = 0
    MAX_RETRIES = 10
    try:
        page_views = pageviewapi.per_article('en.wikipedia', title, '20150701', '20210607', access='all-access', agent='all-agents', granularity='daily')
    except ConectionResetError as e:
        if (retry_count == MAX_RETRIES):
            raise e
        time.sleep(5)
        retry_count +=1
        page_views = pageviewapi.per_article('en.wikipedia', title, '20150701', '20210607', access='all-access', agent='all-agents', granularity='daily')
    
    except ZeroOrDataNotLoadedException:
        print("Got ZeroOrDataNotLoadedException error")
        pass
    
    view_counter = 0
    for i in range (0, len(page_views['items'])):
        view_counter += page_views['items'][i]['views']
    
    return view_counter


def main():
    filepath = "dataset/balanced_dataset2.csv"
    #Fetch edit count and write to CSV
    df = pd.read_csv(filepath, skiprows=range(1, 643))

    # df = pd.read_csv(filepath)
    titles = df['page_title']

    for title in titles:
        page_views = fetch_pageviews(title)
        print('Tilte:', title, 'View Count:',page_views)

        #Write to df
        index = titles[titles == title].index[0]
        df.loc[index,'view_count'] = page_views
    
    # writing into the file
    try:
        df.to_csv(filepath, mode='a', index=False)
    except PermissionError:
        df.to_csv("dataset/new.csv", mode='a', index=False)
    

if __name__ == "__main__":
    main()