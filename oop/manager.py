from oop.employee import Employee


class Manager(Employee):
    def __init__(self, name, id, department, responsibility) -> None:
        super().__init__(name, id, department)
        self.name=name
        self.id=id
        self.department=department
        self.responsibility=responsibility

    
    def getDetail(self):
        super().getDetail(True)
        print(f" with responsibility {self.responsibility}")

    
    def management(self):
        print("Here my management functions:\nplanning, organizing, leading and controlling")

