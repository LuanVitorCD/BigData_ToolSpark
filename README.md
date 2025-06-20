# Big Data com Apache Spark 🚀

> Pipeline básico em PySpark para ingestão, processamento, armazenamento e visualização de grandes volumes de dados.

---

## 📋 Sumário

1. [Visão Geral](#visão-geral)
2. [Funcionalidades](#funcionalidades)
3. [Pré-requisitos](#pré-requisitos)
4. [Instalação](#instalação)
5. [Execução](#execução)
6. [Estrutura do Projeto](#estrutura-do-projeto)
7. [Customização](#customização)
8. [Contribuição](#contribuição)
9. [Licença](#licença)

---

## 🧐 Visão Geral
Este repositório demonstra um fluxo de trabalho completo em **PySpark**:

- **Ingestão** de dados CSV
- **Processamento**: filtragem, agregação e transformações
- **Armazenamento** em **Parquet**
- **Visualização** dos resultados com **Pandas** e **Matplotlib**

Ideal para quem deseja entender como aplicar o Spark em cenários reais de Big Data.

---

## ✨ Funcionalidades

- Leitura de arquivos CSV com cabeçalho
- Limpeza de dados (remoção de valores nulos)
- Agregação por categoria
- Exportação de resultados em formato Parquet
- Geração de gráficos de barra a partir de DataFrame Pandas

---

## 🎯 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.7+**
- **Java 8+** (necessário para o Spark)
- **Pip** (gerenciador de pacotes Python)

Pacotes Python (via `requirements.txt`):

- `pyspark`
- `pandas`
- `matplotlib`

---

## 🚀 Instalação

1. **Clone este repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/bigdata-spark-project.git
   cd bigdata-spark-project
````

2. **Crie e ative um ambiente virtual (opcional)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Execução

Execute o script principal:

```bash
python pyspark_project.py
```

* Os arquivos Parquet serão gravados em `data/processed/`.
* Um gráfico de barras será exibido em tela mostrando a soma de valores por categoria.

---

## 🗂️ Estrutura do Projeto

```plaintext
bigdata-spark-project/
├── data/
│   ├── raw/
│   │   └── exemplo.csv        # Dados de entrada
│   └── processed/
│       └── total_por_categoria.parquet  # Saída do pipeline
├── pyspark_project.py         # Script principal em PySpark
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação (você está aqui)
```

---

## ⚙️ Customização

* **Caminhos de dados**: altere `data/raw/exemplo.csv` e `data/processed/` no script.
* **Transformações**: adicione novas operações no **DataFrame** PySpark.
* **Visualização**: modifique o código de plot em Matplotlib conforme sua necessidade.
* **MLlib**: acrescente etapas de machine learning utilizando `pyspark.ml`.

---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Fork este repositório
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`
4. Push para a branch: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

---

## 📝 Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

```
```
