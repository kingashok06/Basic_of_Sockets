class Person:
    def __init__(self,name , client , addr) -> None:
        self.client = client
        self.addr = addr
        self.name = None

    def set_name(self,name):
        self.name = name

    def __repr__(self) -> str:
        return f"Person{self.name}{self.addr}"