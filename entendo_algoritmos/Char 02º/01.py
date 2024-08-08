class Order:
    def __init__(self, dish: str, table: int):
        self.dish = dish
        self.table = table

    def __repr__(self) -> str:
        return f"Making the {self.dish} for the table {self.table}."


class OrdersList(list):
    def add_order(self, dish: str, table: int):
        self.append(Order(dish, table))

    def cook_order(self):
        try:
            print(self.pop(0))
        except IndexError:
            print("All the orders were cooked.")
        
        
    def __repr__(self) -> str:
        # Provide a more accurate representation of the OrdersList
        return f"OrdersList with {super().__len__()} orders.\nTo more \
information use the 'cook_order' funct."

def main() -> None:
    """Function used to run the main code."""
    ordlist = OrdersList()
    ordlist.add_order("Feijoada", 231)
    ordlist.add_order("Peixe assado", 235)
    ordlist.cook_order()
    ordlist.cook_order()
    ordlist.cook_order()

    print()
    print(ordlist)

    print(len(ordlist))

if __name__ == "__main__":
    main()
