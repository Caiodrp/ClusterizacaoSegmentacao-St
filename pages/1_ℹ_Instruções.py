import pandas as pd
import pandas as pd
import numpy as np
import streamlit as st
import base64
import requests

# Definir o template
st.set_page_config(page_title='Previsão de Renda',
                page_icon='🧩',
                layout='wide')

# Título centralizado
st.write(
    '<div style="display:flex; align-items:center; justify-content:center;">'
    '<h1 style="font-size:4.5rem;">Instruções</h1>'
    '</div>',
    unsafe_allow_html=True
)

# Divisão
st.write("---")

# Adicionando texto antes do vídeo
st.write("Este é um tutorial em vídeo sobre como usar a aplicação")

# Adicionando vídeo
st.write()
st.write(
    '<div style="display:flex; align-items:center; justify-content:center;">'
    '<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ?start=40" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
    '</div>',
    unsafe_allow_html=True
)
# Arquivo csv modelo 
st.write('# Modelos dos arquivos CSV')
st.write('Os arquivos a serem usados devem ser com o nome e ordem das colunas identicos a do modelo')
url = "https://github.com/seu_usuario/seu_repositorio/raw/main/arquivo.xlsx"

# Função para baixar o arquivo
def download_file(url):
    response = requests.get(url)
    b64 = base64.b64encode(response.content).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="arquivo.xlsx">Baixar arquivo</a>'

# Adicionando botão para download
st.markdown(download_file(url), unsafe_allow_html=True)

# Adicionando texto
st.write(
    """
    # Análise Clusterização

    Na página "Análise Clusterização", após carregar o arquvio .CSV, você pode visualizar diferentes gráficos e informações sobre o conjunto de dados "online_shoppers_intention" que são o comportamento de diversos acessos de usuários em diferentes tipos de sites, disponível em https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset. 

    ### Info

    Na opção "Info" encontram-se as informações sobre os dados tais como o dicionário de dados, algumas linhas do dataframe e a opção de gerar um relatório completo sobre eles.

    ### Descritiva

    Na opção "Descritiva' encontram-se opções de visualizações gráficas entre as variáveis da base de dados e relações entre elas e o problema em questão

    # Clusterização
    
    Após carregar o arquivo, essa página possibilita a realização da clusterização do comportamento de navegação dos acessos, através de um algoritmo de K-means ou de algorítimos hierárquicos, oferecendo um filtro por variáveis com os grupos formados os grupos.

    ### K-Means

    Selecionando o "K-means", aparecerá a opção de visualizar através do método do cotovelo ou da silhueta sugestão de quantidades de grupos, e logo após o usuário define quantos grupos deseja que o algoritmo divida. Um filtro para ver a distribuição das variáveis por grupo e a opção de baixar o Data Frame com a coluna dea grupamento.

    ### Hierárquicos
    
    Selecionando "Hierárquicos", aparecerá a opção de escolher qual o método de ligação (de acordo com o estudo dos dados). Depois digitar a quantidade de clusters desejados (por medidas de poder computacional, também testar a quantidade no notebook de dados). E logo depois um filtro e um botão de dowload semelhante ao do K-means. 
    
    # Análise Segmentação
    
    Na página "Análise Clusterização", após carregar o arquvio .CSV, você pode visualizar diferentes gráficos e informações sobre o conjunto de dados "exemplo_RFV" que são o comportamento de clientes quanto a compras, como o tempo, quantidade e valor. Disponível em https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset. 
    
    # Segmentação
    
    Após o caregamento do arquivo, irá retornar um dataframe com cada cliente segmentado por Recência, Frequencia e Valor em "A", "B", "C" e "D" sendo A um melhor nível e D o pior (assim como mostrado no notebook de dados). E também um botão para download do Data Frame segmentado.

    """
)