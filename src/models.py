from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

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
    mae_email: Optional[EmailStr] = None

    pai_nome: Optional[str] = None
    pai_cpf: Optional[str] = None
    pai_rg: Optional[str] = None
    pai_telefone: Optional[str] = None
    pai_pis: Optional[str] = None
    pai_email: Optional[EmailStr] = None

    endereco_cep: Optional[str] = None
    endereco_rua_av: Optional[str] = None
    endereco_numero: Optional[str] = None
    endereco_bairro: Optional[str] = None

    escola_nome: Optional[str] = None
    escola_cnpj: Optional[str] = None
    escola_inep: Optional[str] = None
    escola_telefone: Optional[str] = None
    escola_endereco: Optional[str] = None