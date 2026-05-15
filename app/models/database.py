import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# No Render, configure a variável de ambiente DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_3hydgXeNft0j@ep-shiny-voice-aqkly1g7-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

class Carros(Base):
    __tablename__ = "Carros"
    id = Column(Integer, primary_key=True, index=True)
    Carro = Column(String)
    Ano = Column(String)
    Cambio = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)