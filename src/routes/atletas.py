@app.get("/atletas/{cpf}")
async def buscar_atleta_por_cpf(cpf: str):
    # Remove pontos e traços caso o usuário envie formatado
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    
    response = supabase.table("atletas").select("*").eq("cpf_atleta", cpf_limpo).execute()
    
    if not response.data:
        raise HTTPException(status_code=404, detail="Atleta não encontrado.")
    
    return response.data[0]