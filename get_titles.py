import random, csv

def get_unprotected_titles(number_of_articles):

    print("Trying to fetch", number_of_articles, " articles...")

    list_article_indices = random.sample(range(1, 6807), number_of_articles)

    with open('./view_count_unprotected_articles.csv', encoding="utf-8") as fd:
        reader=csv.reader(fd)
        interesting_rows=[row for idx, row in enumerate(reader) if idx in list_article_indices]
    
    print(len(interesting_rows), " titles have been picked!" )

    return interesting_rows

def get_sysop_titles(number_of_articles, total_articles_in_file):

    print("Trying to fetch", number_of_articles, " articles...")

    list_article_indices = random.sample(range(1, total_articles_in_file), number_of_articles)

    with open('parsed/concatenated-sysop.csv', encoding="utf-8") as fd:
        reader=csv.reader(fd)
        interesting_rows=[row for idx, row in enumerate(reader) if idx in list_article_indices]
    
    print(len(interesting_rows), " titles have been picked!" )

    return interesting_rows

def initial_write_to_csv(list_unprotected_articles, filepath):

    print("Writing to file....")

    # open the file in the append mode
    f = open(filepath, 'a', encoding='utf-8', newline='')    

    writer = csv.writer(f)

    header = ['page_id', 'page_title', 'view_count', ]
    writer.writerow(header)

    for article in list_unprotected_articles:
        #Set page title and ID
        page_id = article[0]
        page_title =  article[1]
        view_count = article [3]

        row = [page_id, page_title, view_count]
        
        #Write to CSV
        writer.writerow(row) 

    print("Writing has been completed!")

def add_sysop_titles(list_sysop_articles , filepath):
        print("Writing to file....")

        # open the file in the append mode
        f = open(filepath, 'a', encoding='utf-8', newline='')    

        writer = csv.writer(f)

        for article in list_sysop_articles:
            #Set page title and ID
            page_title =  article[0]
            #view_count = article [3]
            protection_status = article[1]

            row = [page_title, protection_status]
            
            #Write to CSV
            writer.writerow(row) 


def main():
    #Get 200 odd articles of each type

    #1. Get 200 titles from the unprotected pile
    # list_unprotected_articles = get_unprotected_titles(218)

    # #Write title, ID and view_count to file
    # initial_write_to_csv(list_unprotected_articles, "dataset/balanced_dataset2.csv")

    #2. Get 52 sysop articles
    number_of_articles = 52
    last_row_in_file = 168
    list_sysop_articles = get_sysop_titles(number_of_articles, last_row_in_file)

    add_sysop_titles(list_sysop_articles, "dataset/balanced_dataset2.csv")

if __name__ == "__main__":
    main()
