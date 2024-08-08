def print_every_item_in_list(_list: list, tab= 0) -> None:
    print(f'{" " * 4 * tab}', end= ' ')
    
    for item in _list:
        if isinstance(item, list):
            print()
            print_every_item_in_list(item, tab + 1)
            
        else:
            print(f'{item}', end= ' ')

l = [12, 1, 2,
        [3, 5, 4,
            [32, 55, 100, 99,
                [1003,
                 [
                    245398
                ]
                 ]
                ]
            ]
        ]

print_every_item_in_list(l)
