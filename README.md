# cadastro_raaei

API para cadastro de atletas usando FastAPI e Supabase.

## Instalação

1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure as variáveis de ambiente no `.env` (SUPABASE_URL e SUPABASE_KEY).
4. Execute: `uvicorn main:app --reload`

## Endpoints

- `POST /atletas/`: Cadastrar atleta
- `GET /atletas/`: Listar atletas
- `GET /atletas/{cpf}`: Buscar atleta por CPF