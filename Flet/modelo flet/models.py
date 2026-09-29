from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

CONN = "sqlite:///projeto.db"

engine = create_engine(CONN, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True)
    usuario = Column(String(50), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)


Base.metadata.create_all(engine)
