from oop.manager import Manager
from technicaltest.technicaltest import (
    count_vocal,
    print_opensource,
    find_max_recursive,
)

from oop.secretary import Secretary
from oop.manager import Manager
from oop.developer import Developer
from oop.employee import Employee
from logictest.alice_bob_readingbooks import Book, solve


if __name__ == "__main__":
    #text = input("input your text: ")
    #count_vocal(text)
    #print_opensource()
    #find_max_recursive([5,1,3,4,9])
    
    # secretary=Secretary("Bobby", 1, "Marketing")
    # secretary.getDetail()
    # secretary.printDocument()
    # secretary.sendDocument()

    # manager=Manager("Alex", 2, "Marketing", "Management")
    # manager.getDetail()
    # manager.management()

    # developer = Developer("Alex", 3, "IT", "python", "nodejs")
    # developer.getDetail()

    # employee = Employee("Alex", 4, "IT")
    # employee.getDetail()

    list_book = [
        Book(7, 0, 1),
        Book(2, 1, 0),
        Book(4, 1, 1),
        Book(1, 0, 1),
        Book(6, 1, 0),
    ]

    result = solve(2, list_book)
    print(result)


