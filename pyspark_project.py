from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # 1) Inicializa Spark
    spark = SparkSession.builder \
        .appName("BigDataSparkProjeto") \
        .getOrCreate()

    # 2) Ingestão: lê CSV exemplo
    df = spark.read.option("header", True) \
        .csv("data/raw/exemplo.csv")
    df.printSchema()

    # 3) Processamento: filtra e faz agregações
    df_clean = df.filter(df.valor.isNotNull())
    agg = df_clean.groupBy("categoria").sum("valor")
    agg.show()

    # 4) Escrita: salva resultado em Parquet
    agg.write.mode("overwrite").parquet("data/processed/total_por_categoria.parquet")

    # 5) Visualização: converte para Pandas
    pandas_df = agg.toPandas()
    pandas_df.plot.bar(x='categoria', y='sum(valor)')
    plt.title('Total por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Soma de Valor')
    plt.tight_layout()
    plt.show()

    spark.stop()


if __name__ == '__main__':
    main()
