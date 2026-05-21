import flet as ft 

def main(page: ft.Page): 
    # Configurações iniciais da página
    page.title = "Calculadora" 
    
    # Criando os componentes de texto e entrada 
    numero1 = ft.TextField(label="Primeiro número") 
    numero2 = ft.TextField(label="Segundo número") 
    resultado = ft.Text("Resultado: ") 
    
    # Criando a caixa de operações (Dropdown)
    operacoes = ft.Dropdown(
        label="Escolha a operação",
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/"),
        ] 
    )
    
    # Função interna para realizar o cálculo quando o botão for clicado
    def calcular(e): 
        # Pega os valores digitados e transforma em números decimais
        n1 = float(numero1.value) 
        n2 = float(numero2.value) 
        
        # Pega a operação escolhida no Dropdown 
        operacao = operacoes.value 
        
        # Estrutura condicional para verificar e executar a conta 
        if operacao == "+": 
            conta = n1 + n2 
        elif operacao == "-": 
            conta = n1 - n2
        elif operacao == "*": 
            conta = n1 * n2 
        elif operacao == "/": 
            # Nota: Lembre-se de que se n2 for 0, o Python pode retornar um erro de divisão por zero.
            conta = n1 / n2 
            
        # Atualiza o valor do texto com o resultado obtido 
        resultado.value = f"Resultado: {conta}" 
        
        # Atualiza a interface gráfica para exibir a mudança 
        page.update() 

    # Criando o botão que aciona a função de cálculo 
    botao = ft.ElevatedButton( 
        "Calcular", 
        on_click=calcular 
    ) 
    
    # Adicionando todos os componentes criados à tela do aplicativo 
    page.add( 
        numero1, 
        numero2, 
        operacoes,
        botao, 
        resultado 
    ) 

# Inicia a aplicação e define que a função principal é a main 
ft.app(target=main) 