def get_data_from_server(url) -> str:
    return 'This is just an example, relax.'

def get_page(url: str, cached_memory: dict) -> tuple[str, dict]:
    if cached_memory.get(url):
        return cached_memory[url], cached_memory
    
    else:
        print('Adding this url to the cached memory')
        data = get_data_from_server(url)
        cached_memory[url] = data
        return data, cached_memory
    
def main() -> None:
    """Function used to run the main code."""
    memory = {}
    data = ''

    data, memory = get_page('www.https.com', memory)
    print(data)
    print(memory, end='\n'*2)

    data, memory = get_page('www.https.com', memory)
    print(data, end= '\n'*2)

    data, memory = get_page('www.http.com', memory)
    print(data)
    print(memory, end='\n'*2)


if __name__ == '__main__':
    main()
    