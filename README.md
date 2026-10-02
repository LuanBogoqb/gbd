# GBD - GelBooru Bulk Downloader

Bulk downloader de imagens e videos do **GelBooru**, escrito em **Python**, com foco em:

- Facilidade de uso  

---

## Funcionalidades

- Download em massa de posts do GelBooru  
- Filtro por tags  
- Suporte a múltiplas páginas  
- Downloads paralelos (multithreading)  
- Configuração externa (API e comportamento pelo config.json)   
- Prevenção de sobrecarga do sistema  

---

## 📁 Estrutura do Projeto

```
GelBooru-Bulk-Downloader/
├── main.py            # Lógica principal / interface CLI
├── configlib.py       # Configurações e carregamento de dados
├── gelboorulib.py     # Comunicação com a API e download
├── requirements.txt   # Dependências do projeto
└── README.md
```

---

## Requisitos

- Python **3.10** ou superior  
- Conexão com a internet  
- Conta no GelBooru (para API Key)  

### Dependências

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Quando executar GBD.py, ele irá criar um config.json na raiz. configure com suas credenciais e o caminho para downloads.

---

## Como Usar

```bash
python main.py
```
