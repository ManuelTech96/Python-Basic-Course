import db

from sqlalchemy import Column, Integer, String, Boolean

class Client(db.Base):
    __tablename__ = 'Clients'
    
    id = Column(Integer, primary_key=True)
    Dni = Column(String, nullable=False)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Phone = Column(String, nullable=False)
    Email = Column(String, nullable=False,)
    ContractId = Column(Integer, nullable=True)
    VehiculeId = Column(Integer, nullable=True)
    Activo = Column(Boolean, default=True)
    
    def __init__(self, Dni, FirstName, LastName, Phone, Email, ContractId, VehiculeId, Activo):
        self.Dni = Dni
        self.FirstName = FirstName
        self.LastName = LastName
        self.Phone = Phone
        self.Email = Email
        self.ContractId = ContractId
        self.VehiculeId = VehiculeId
        self.Activo = Activo
    
    def __repr__(self):
        return f'''Client({self.Dni}, {self.FirstName}, {self.LastName}, {self.Phone}, 
                    {self.Email}, {self.ContractId}, {self.VehiculeId}, {self.Activo})'''
                    
    def __str__(self):
        return self.Dni