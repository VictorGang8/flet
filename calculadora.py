import flet as ft

def main(page: ft.Page):
    
    page.title = "Calculadora"
    numero1 = ft.TextField(label="Primeiro número")
    numero2 = ft.TextField(label="Segundo número")
    resultado = ft.Text("Resultado:")
    
    def calcular():
        n1 = float(numero1.value)
        n2 = float(numero2.value)
    
    page.add(resultado)
ft.app(target=main)
