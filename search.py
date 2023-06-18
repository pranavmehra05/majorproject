def perform_search(search_query):
    import pandas as pd
    df = pd.read_csv(r'dataset/verify.csv')
    key = search_query
    if key in df.values:
        result = "verified"
    else:
        result = "not-verified"
    return result
