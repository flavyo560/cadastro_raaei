import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configuração Supabase
data = {
    "SUPABASE_URL": os.environ["SUPABASE_URL"],
    "SUPABASE_KEY": os.environ["SUPABASE_KEY"],
}

# como os.environ[] lança KeyError se faltar, isso garante fail-fast
supabase: Client = create_client(data["SUPABASE_URL"], data["SUPABASE_KEY"])

# Modelo de Dados (Pydantic) para validação
class Atleta(BaseModel):
    nome_atleta: str
    cpf_atleta: str
    rg_atleta: Optional[str] = None
    inep_aluno: Optional[str] = None
    data_nascimento: str  # Formato YYYY-MM-DD
    cbat: Optional[str] = None
    telefone_atleta: Optional[str] = None
    sexo: str

    mae_nome: str
    mae_cpf: Optional[str] = None
    mae_rg: Optional[str] = None
    mae_telefone: Optional[str] = None
    mae_pis: Optional[str] = None
    mae_email: Optional[str] = None

    pai_nome: Optional[str] = None
    pai_cpf: Optional[str] = None
    pai_rg: Optional[str] = None
    pai_telefone: Optional[str] = None
    pai_pis: Optional[str] = None
    pai_email: Optional[str] = None

    endereco_cep: Optional[str] = None
    endereco_rua_av: Optional[str] = None
    endereco_numero: Optional[str] = None
    endereco_bairro: Optional[str] = None

    escola_nome: Optional[str] = None
    escola_cnpj: Optional[str] = None
    escola_inep: Optional[str] = None
    escola_telefone: Optional[str] = None
    escola_endereco: Optional[str] = None


@app.post("/atletas/")
async def cadastrar_atleta(atleta: Atleta):
    try:
        # Converte o objeto Pydantic em dicionário e envia ao Supabase
        data = atleta.dict()
        response = supabase.table("atletas").insert(data).execute()
        return {"status": "sucesso", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/atletas/")
async def listar_atleta():
    try:
        response = supabase.table("atletas").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))