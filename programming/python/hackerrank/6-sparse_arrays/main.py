'Challenge to check arrays'

strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']


def search_list(string_list: list, query_list: list) -> list:
    'Function to return number of queries hit'
    return_list = []
    for query in query_list:
        return_list.append(string_list.count(query))

    return return_list


print(search_list(strings, queries))
