class Employee:
    def __init__(self, name, id, department) -> None:
        self.name=name
        self.id=id
        self.department=department

    
    def getDetail(self, is_modify=False):
        my_type = type(self)
        print(f"Hi, my name is {self.name} with ID {self.id}.\nI'm in the department {self.department}.\nMy role is {my_type.__name__}", end="" if is_modify else ".\n")