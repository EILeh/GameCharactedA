"""
Game character A

In the program is implemented a very simple game character who is able to carry
along some items. A game character is a character who has some kind of backpack
containing  the items the character has.

Writer of the program: EILeh

"""

class Character:

    def __init__(self, character_name,
                 items = None):

        self.__name = character_name

        # Initializes an empty dictionary if the character doesn't have any
        # items.
        if items is None:
            items = {}

        self.__items = items

    def printout(self):

        # If character doesn't have items, only character's name is printed.
        if not self.__items:
            print("Name:", self.__name)
            print("  --nothing--")

        else:
            print("Name:", self.__name)

            # Goes through the character's item that are in a dictionary and
            # prints the item and the amount of items.
            for item in sorted(self.__items):
                print(" ", self.__items[item], item)


    def get_name(self):
        return self.__name


    def give_item(self, test_item):

        # If character already has the given item, the item's value is grown
        # by one.
        if test_item in self.__items:
            self.__items[test_item] += 1

        # If character doesn't have the given item, a new key-value pair it
        # added to the dictionary __items.
        else:
            self.__items[test_item] = 1

    def remove_item(self, item_to_be_removed):

        # If character already has the given item, the item's value is reduced
        # by one.
        if item_to_be_removed in self.__items:
            self.__items[item_to_be_removed] -= 1

            # If character had only one of the items that was reduced,
            # the item itself is removed from the dictionary.
            if self.__items[item_to_be_removed] == 0:
                self.__items.pop(item_to_be_removed)

    def has_item(self, test_item):

        if test_item in self.__items:
            return True

        else:
            return False


    def how_many(self, amount_of_test_items):

        # If character doesn't have the item in the dictionary then zero it
        # returned.
        if amount_of_test_items not in self.__items:
            return 0

        # Otherwise the item's value is returned.
        else:
            return self.__items.get(amount_of_test_items)


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()