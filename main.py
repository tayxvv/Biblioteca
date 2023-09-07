

# from Usuario import Usuario

# objeto = Usuario('nome', 'endereco', 1, 'login', 'senha', 'email@gmail.com', '123456789')
# objeto.cadastrarUsuario()
# objeto.consultarUsuario('nome')
# objeto.alterarUsuario('nome2', 'endereco2', 3, 'login2', 'senha2', 'email2@gmail.com', '1234567892')

import asyncio
import uvicorn
from typing import Union
from Connection import Connection
import jwt

from fastapi import FastAPI, Body, Header, Depends, HTTPException

app = FastAPI()

SECRET_KEY = 'chaveSuperSecreta'

@app.get("/apiname")
# @app.post("/login")

# async def login(data: dict = Body(...)):
#     login = data.get('login')
#     senha = data.get('senha')
#     connection = Connection()
#     returnConnect = connection.connect()
#     cursor = returnConnect.cursor()

#     cursor.execute("select * from adm.users where user_name ='" + login + "' and password = '" + senha + "';")
#     loginReturn = cursor.fetchone()
#     if (not loginReturn):
#         return "Usuario nao encontrado"
    
#     encoded = jwt.encode({"some": "payload"}, SECRET_KEY, algorithm="HS256")
#     return encoded

async def apiname(authorization: str = Header(None)) -> str:
    if authorization is None:
        raise HTTPException(status_code=401, detail="Token não encontrado")

    # Verificar se o cabeçalho começa com "Bearer "
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")

    # Extrair o token após "Bearer "
    token = authorization.split(" ")[1]

    #jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    return token

async def main():
    config = uvicorn.Config("main:app", port=8004, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()
    return {"Hello": "World"}

if __name__ == "__main__":
    asyncio.run(main)
    print("Ola")
