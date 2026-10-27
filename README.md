# Executar os testes

No PowerShell, na pasta do projeto, instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Execute os testes:

```powershell
python -m pytest -v
```

Para executar e salvar o resultado em `relatorio-testes.txt`:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-testes.txt
```
