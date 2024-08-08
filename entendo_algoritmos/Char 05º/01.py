def verify_people_voted(name: str, record: dict[str, bool] = {}) -> None|dict:
    name = name.strip().title()
    
    if record.get(name):
        print(f'\033[32m{name} has already voted.\033[m')
    
    else:
        record[name] = True
        print(f'\033[33m{name} voted.\033[m')
        return record
    
def main() -> None:
    """Function used to run the main code."""
    d = verify_people_voted('josh')
    print(d, end='\n'*2)

    verify_people_voted('drake', d)
    verify_people_voted('drake', d)
    print(d, end='\n'*2)

    verify_people_voted('carly', d)
    verify_people_voted('carly', d)
    print(d)



if __name__ == '__main__':
    main()