from oop.employee import Employee


class Developer(Employee):
    def __init__(self, name, id, department, backendTool, frontendTool) -> None:
        super().__init__(name, id, department)
        self.name=name
        self.id=id
        self.department=department
        self.backendTool=backendTool
        self.frontendTool=frontendTool

    
    def getDetail(self):
        super().getDetail(True)
        print(f".\nI'm using {self.backendTool} as backend and {self.frontendTool} as frontend")