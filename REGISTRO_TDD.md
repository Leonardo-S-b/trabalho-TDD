# Registro do ciclo de TDD

Executado em 27/10/2026 com Python 3.14.0 e pytest 9.2.0.
Cada teste foi criado e executado antes da implementacao correspondente.
As etapas Red e Green tambem foram registradas em commits separados.

## Estado inicial

Os quatro testes originais de `calcular_total` passaram antes das alteracoes.

## Cenario 1: 2 km e pedido de R$ 50

- **Teste:** `test_taxa_de_cinco_reais_para_dois_km_e_pedido_de_cinquenta`.
- **Red:** a execucao falhou na coleta com `ImportError`, pois a funcao
  `calcular_taxa_entrega` ainda nao existia em `src/pedido.py`.
- **Green:** criada a funcao com `return 5`, somente o necessario para esse teste.
- **Resultado:** 5 testes passaram, incluindo os quatro originais.
- **Refactor:** nenhuma mudanca estrutural necessaria nessa etapa.

## Cenario 2: 4 km e pedido de R$ 50

- **Teste:** `test_taxa_de_sete_reais_para_quatro_km_e_pedido_de_cinquenta`.
- **Red:** `assert 5 == 7`; resultado da suite: 1 falhou e 5 passaram.
- **Green:** adicionada a condicao `distancia_km > 3`, retornando
  `5 + (distancia_km - 3) * 2`; ate 3 km, permanece o retorno de 5.
- **Resultado:** todos os 6 testes passaram.
- **Refactor:** a formula ja expressa diretamente a regra; sem mudanca adicional.

## Cenario 3: 5 km e pedido de R$ 100

- **Teste:** `test_entrega_gratis_para_cinco_km_e_pedido_de_cem`.
- **Red:** `assert 9 == 0`; resultado da suite: 1 falhou e 6 passaram.
- **Green:** adicionada, antes do calculo por distancia, a condicao
  `total_pedido >= 100`, retornando 0 para garantir a entrega gratuita.
- **Resultado:** todos os 7 testes passaram.

## Revisao final (Refactor)

A funcao foi revisada: o retorno antecipado para entrega gratuita evita
aninhamento, e a formula do adicional nao possui duplicacao. Nao foi necessaria
uma refatoracao estrutural. A documentacao da funcao foi detalhada para explicar
as tres regras, sem alterar o comportamento.

## Relatorio final

Comando executado no PowerShell:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-testes.txt
```

Resultado: **7 testes passaram** (4 originais e 3 obrigatorios de entrega).
A saida completa esta em `relatorio-testes.txt`.
