import pandas as pd
import matplotlib.pyplot as plt


dados_vendas = {
    'mes': ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro','novembro', 'dezembro'],
        'vendas': [120, 150, 160, 170, 180, 190, 210, 220, 280, 230, 240, 250]
        }
        df = pd.DataFrame(dados_vendas)

        # 2. Cálculo dos quartis
        # O método .describe() do pandas já retorna os quartis (25%, 50% e 75%).
        estatisticas = df['vendas'].describe()

        # Exibe as estatísticas
        print("Estatísticas Descritivas:")
        print(estatisticas)

        # 3. Criação do boxplot
        plt.figure(figsize=(8, 6)) # Define o tamanho da figura
        plt.boxplot(df['vendas'])

        # Adiciona título e rótulos
        plt.title('Boxplot das Vendas')
        plt.ylabel('Valor das Vendas')
        plt.xticks([1], ['Vendas']) # Rótulo para o eixo X

        plt.grid(True, linestyle='--', alpha=0.6) 
        # Adiciona um grid ao gráfico
        plt.show()
        plt.savefig('chart9.png')


        