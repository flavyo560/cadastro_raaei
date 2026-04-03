import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv
from src.models import Atleta

load_dotenv()

app = FastAPI()

# Configuração Supabase
data = {
    "SUPABASE_URL": os.environ["SUPABASE_URL"],
    "SUPABASE_KEY": os.environ["SUPABASE_KEY"],
}

# como os.environ[] lança KeyError se faltar, isso garante fail-fast
supabase: Client = create_client(data["SUPABASE_URL"], data["SUPABASE_KEY"])


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


@app.get("/atletas/{cpf}")
async def buscar_atleta_por_cpf(cpf: str):
    try:
        # Remove pontos e traços caso o usuário envie formatado
        cpf_limpo = cpf.replace(".", "").replace("-", "")

        response = supabase.table("atletas").select("*").eq("cpf_atleta", cpf_limpo).execute()

        if not response.data:
            raise HTTPException(status_code=404, detail="Atleta não encontrado.")

        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))