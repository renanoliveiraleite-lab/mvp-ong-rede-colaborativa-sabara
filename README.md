# mvp-ong-rede-colaborativa-sabara
# MVP — ONG Rede Colaborativa Brasil (Sabará/MG)

Sistema web progressivo (PWA) desenvolvido para otimizar a triagem, o cadastro de beneficiários e o controle de entregas de cestas básicas por ciclo na **ONG Rede Colaborativa Brasil** (núcleo Sabará/MG), alinhado à **Meta 2.1 do ODS 2 (Fome Zero e Agricultura Sustentável)**.

## Problema Resolvido
Substituição do controle manual em papel por uma interface móvel rápida e acessível em campo, evitando filas e bloqueando entregas duplicadas dentro do mesmo ciclo mensal de distribuição.

## Funcionalidades do MVP
- **Tela 1 — Acesso Operacional (`RNF01`, `RNF04`):** Autenticação segura para voluntários e coordenadores.
- **Tela 2 — Atendimento de Campo (`RF01`, `RF02`, `RF03`, `RNF02`):** Consulta rápida por CPF com máscara/validação e registro de entrega vinculado ao ciclo de referência vigente.
- **Tela 3 — Alertas e Resultados (`RNF04`):** Confirmação visual multimodal (cor, ícone, texto e alto contraste) para operação sob luz solar direta.

## Arquitetura e Tecnologias Planejadas
- **Frontend:** PWA Mobile-First (HTML5, CSS3, JavaScript) com foco em alto contraste e áreas de toque acessíveis (≥44px).
- **Backend:** Python + FastAPI + Pydantic (validação estrita de entradas).
- **Banco de Dados:** PostgreSQL com SQLAlchemy ORM.
- **Qualidade e DevOps:** Testes automatizados unitários/integração (`pytest`) e pipeline de Integração Contínua (CI) via GitHub Actions.

## Estrutura do Repositório
```text
├── backend/          # API FastAPI, modelos, regras de negócio e testes
├── frontend/         # Interface PWA (Telas 1, 2 e 3)
└── .github/workflows # Pipeline de Integração Contínua (CI)
