import streamlit as st

st.set_page_config(page_title="Supermercado", page_icon="🛒", layout="centered")

st.title("Calculadora de Compras de Supermercado")
st.write("Insira os itens, informe o valor pago e calcule o troco.")

precos_itens = {
    "Arroz (5kg)": 25.90,
    "Feijão (1kg)": 8.50, 
    "macarrão (500g)": 4.28,
    "Óleo de Soja (900ml)": 6.85,
    "Açúcar Refinado (1kg)": 4.50,
    "Café Torrado (500g)": 14.90,
    "Banana Prata (kg)": 5.99,
    "Tomate Italiano (kg)": 7.80,
    "Cebola (kg)": 4.20,
    "Patinho Bovino (kg)": 38.90,
    "Frango (Filé de Peito, kg)": 19.98,
    "Leite Integral (1L)": 4.89,
    "Queijo Muçarela (kg)": 42.00,
    "Detergente Líquido (500ml)": 2.20,
    "Sabonete (90g)": 1.95,
    "Sal Refinado (1kg)": 3.49,
    "Farinha de Trigo (1kg)": 5.20,
    "Molho de Tomate (Sachê 300g)": 2.85,
    "Milho Verde (Lata 170g)": 3.99,
    "Sardinha em Óleo (Lata 125g)": 4.75,
    "Biscoito Recheado (130g)": 3.10,
    "Cereal Matinal (250g)": 11.50,
    "Batata Monalisa (kg)": 6.40,
    "Maçã Gala (kg)": 9.80,
    "Alface Crespa (Unidade)": 3.50,
    "Pão de Forma (500g)": 7.90,
    "Pão Francês (kg)": 16.90,
    "Acém Bovino (kg)": 29.90,
    "Linguiça Toscana (kg)": 21.50,
    "Presunto Cozido (kg)": 34.90,
    "Manteiga com Sal (200g)": 11.40,
    "Iogurte Natural (170g)": 2.79,
    "Ovos Brancos (Dúzia)": 9.90,
    "Creme Dental (90g)": 4.25,
    "Shampoo Neutro (400ml)": 13.90,
    "Desodorante Roll-On (50ml)": 8.50,
    "Papel Higiênico (Leve 12 Pague 11)": 15.80,
    "Sabão em Pó (800g)": 12.40,
    "Amaciante de Roupas (2L)": 14.95,
    "Água Sanitária (1L)": 3.80,
    "Desinfetante Lavanda (500ml)": 4.10
    
}

def calcular_preco_total(itens_selecionados):
    total = sum(precos_itens[item] for item in itens_selecionados)
    return total

itens_selecionados = st.multiselect(
    label="Selecione os itens do supermercado:",
    options=list(precos_itens.keys())
)

if itens_selecionados:
    st.subheader("Itens Selecionados:")
    for item in itens_selecionados:
        st.write(f"- {item}: R$ {precos_itens[item]:.2f}")
        
    total_compra = calcular_preco_total(itens_selecionados)
    
    st.divider()
    st.metric(label="Total da Compra", value=f"R$ {total_compra:.2f}")
    st.divider()
    
    st.subheader("Pagamento e Troco")
    col1, col2 = st.columns(2)
    
    with col1:
        valor_pago = st.number_input("Dinheiro entregue (R$)", value=0.0, step=1.0)
        
    with col2:
        st.write("")
        st.write("")
        botao_calcular = st.button("Calcular Troco", type="primary")
        
    if botao_calcular:
        if valor_pago >= total_compra:
            troco = valor_pago - total_compra
            st.success(f"**Troco a devolver:** R$ {troco:.2f}")
        else:
            st.error("Erro: O valor pago é menor que o total da compra.")
else:
    st.info("Nenhum item selecionado. Marque os produtos acima para ver o valor total.")
