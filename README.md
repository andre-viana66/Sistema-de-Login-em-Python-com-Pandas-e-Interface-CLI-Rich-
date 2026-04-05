# Sistema-de-Login-em-Python-com-Pandas-e-Interface-CLI-Rich-
🔐 Sistema de Login em Python

Um sistema simples de autenticação desenvolvido em Python, com funcionalidades de cadastro, login e atualização de senha, utilizando pandas como armazenamento de dados em arquivo .csv.

## 🚀 Funcionalidades

- ✅ Cadastro de usuários  
- 🔐 Login com validação de credenciais  
- 🔄 Atualização de senha  
- 📁 Armazenamento de dados em CSV  
- 🎨 Interface no terminal com a biblioteca `rich`  

---

## 🛠️ Tecnologias utilizadas

- Python 3  
- Pandas  
- Rich  
- OS (manipulação de arquivos)

## 📂 Estrutura do projeto


projeto-sistema_login/
│-- menu_usuario.py
│-- lista_senhas.csv


---

## ▶️ Como executar

```bash
git clone https://github.com/andre-viana66/Sistema-de-Login-em-Python-com-Pandas-e-Interface-CLI-Rich-
cd seu-repositorio
pip install pandas rich
python sistema_login.py
```
💡 Como funciona

O sistema utiliza um arquivo .csv como banco de dados:

No cadastro → os dados são salvos no arquivo
No login → os dados são lidos e validados
Na atualização → os dados são modificados diretamente no arquivo

📸 Exemplo de uso
```
[1] Acessar o sistema
[2] Cadastrar usuário
[3] Atualizar cadastro
[4] Sair
````
👨‍💻 Autor

Desenvolvido por André Viana