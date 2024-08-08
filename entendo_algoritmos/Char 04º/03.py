def multiplication(numbers_to_multiply: list[int]) -> None:
    for number in numbers_to_multiply:
        print('='*20)
        for c in range(1, 11):
            print(f'{number} X {c:2} = {number * c:>2}')
        print('='*20)

multiplication([2, 3, 4, 5])