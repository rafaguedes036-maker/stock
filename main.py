import streamlit as st
from functions import insert_product, list_products, delete_product, update_product






st.set_page_config(page_title= 'Sistema de Estoque', layout= 'centered')
st.title('📦Sistema de Estoque')

menu = st.sidebar.selectbox("Menu", ["Inserir Produto", "Ver Produtos", "Atualizar Produto", "Deletar Produto"])

#Inserir Produto

if menu == "Inserir Produto":
    st.subheader("➕Inserir Produto")
    name = st.text_input("Nome do Produto")
    category = st.text_input("Categoria")
    price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
    quitantity = st.number_input("Quantidade do Produto", min_value=1)
    provider = st.text_input("Fornecedor")

    if st.button("Salvar"):
        if name:
            insert_product(name, category, price, quitantity, provider)
            st.success("✅ Produto inserido com sucesso!")
        
        else:
            st.error("⚠️ O nome do produto é obrigatório.")


#Vizualizar Produtos

elif menu == "Ver Produtos":
    st.subheader("📋Todos os produtos do estoque ")
    dados = list_products()
    st.dataframe(dados, use_container_width=True)

#Atualizar Produto

elif menu == "Atualizar Produto":
    st.subheader("✏️Atualizar Produto")
    dados = list_products()
    produtos = {f"{p[0]} - {p[1]}": p for p in dados}
    escolhido = st.selectbox("Selecione o produto para atulizar", list(produtos.keys()))
    p = produtos[escolhido]
    print(p)
    novo_nome = st.text_input("Novo nome do produto", value=p[1])
    nova_categoria = st.text_input("Nova categoria", value=p[2])
    novo_preco = st.number_input("Novo preço do produto", value=float(p[3]), format="%.2f")
    nova_quantidade = st.number_input("Nova quantidade do produto", min_value=1, value=p[4])
    novo_fornecedor = st.text_input("Novo fornecedor", value=p[5])

    if st.button("Salvar alterações"):
        update_product(p[0], novo_nome, nova_categoria, novo_preco, nova_quantidade, novo_fornecedor)
        st.success("✅ Produto atualizado com sucesso!")


#Deletar Produto
elif menu == "Deletar Produto":
    st.subheader("🗑️Deletar Produto")
    dados = list_products()
    produtos = {f"{p[0]} - {p[1]}": p[0] for p in dados}
    escolhido = st.selectbox("Selecione o produto para deletar", list(produtos.keys()))
    if st.button("Deletar"):
        delete_product(produtos[escolhido])
        st.success("✅ Produto deletado com sucesso!")

