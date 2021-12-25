from oop.employee import Employee


class Secretary(Employee):
    def __init__(self, name, id, department) -> None:
        super().__init__(name, id, department)
        self.name=name
        self.id=id
        self.department=department
    
    
    def printDocument(self):
        print(f"All right, give me 5 minutes and I'll give the document to you as soon as possible.")

    
    def sendDocument(self):
        print(f"All right, I'll give it to you via email.")


    