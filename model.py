from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/mokyklos_studentai.db')
Base = declarative_base()

class Mokykla(Base):
    __tablename__ = "mokykla"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    imones_kodas = Column("imones_kodas", Integer, unique=True, nullable=False)
    pvm_kodas = Column("pvm_kodas", String)
    adresas = Column("adresas", String)
    studijos = relationship("Studijos", back_populates="mokykla")

    def __repr__(self):
        return f"{self.id}, {self.pavadinimas}, {self.imones_kodas}, {self.pvm_kodas}, {self.adresas}"

class Studijos(Base):
    __tablename__ = "studijos"
    id = Column(Integer, primary_key=True)
    programos_pavadinimas = Column("programa", String)
    trukme = Column("trukme", String)
    kaina = Column("kaina", Float)
    mokykla_id = Column("mokykla_id", Integer, ForeignKey("mokykla.id"))
    mokykla = relationship("Mokykla", back_populates="studijos")
    studentai = relationship("Studentas", back_populates="studijos")

    def __repr__(self):
        return f"{self.id}, {self.programos_pavadinimas}, {self.trukme}, {self.kaina}, {self.mokykla}"

class Studentas(Base):
    __tablename__ = "studentas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    asm_kodas = Column("asmens_kodas", Integer, unique=True, nullable=False)
    el_pastas = Column("el_pastas", String)
    mobilus = Column("tel_nr", Integer)
    studijos_id = Column("studijos_id", Integer, ForeignKey("studijos.id"))
    studijos = relationship("Studijos", back_populates="studentai")

    def __repr__(self):
        return f"{self.id}, {self.vardas}, {self.pavarde}, {self.asm_kodas}, {self.el_pastas}, {self.mobilus}, {self.studijos}"


if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)