import flet as ft

agenda = {}

def main(page: ft.Page):
    
        # Menu principal 

    def principal(e):
        page.controls.clear()

        page.bgcolor="#1a1a1a"
        
        page.fonts= {
            "Inder": "assets/Inder-Regular.ttf",
            "SoraM": "assets/Sora-Medium.ttf",
            "SoraL": "assets/Sora-Light.ttf"
        }

        titulo = ft.Text("O que você deseja fazer?", size=25, font_family="SoraM")

        # Botões

        botao_add = ft.ElevatedButton(
            text="Novo contato",
            color="#FFFFFF",
            bgcolor="#2e2e2e",
            on_click=adicionar_contato,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraM",
                    size=18
                )
            )
        )

        botao_rmv = ft.ElevatedButton(
            text="Remover contato",
            color="#FFFFFF",
            bgcolor="#2e2e2e",
            on_click=remover_contato,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraM",
                    size=18
                )
            )
        )

        botao_lista = ft.ElevatedButton(
            text="Lista de contatos",
            color="#FFFFFF",
            bgcolor="#2e2e2e",
            on_click=lambda e: lista_contato(e, agenda),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraM",
                    size=18
                )
            )
        )

        botao_bc = ft.ElevatedButton(
            text="Buscar contatos",
            color="#FFFFFF",
            bgcolor="#2e2e2e",
            on_click=page_buscar,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraM",
                    size=18,
                )
            )
        )

        principal_alinhado = ft.Column(
            controls=[
                ft.Container(height=20),
                titulo,
                ft.Container(height=10),
                botao_add,
                botao_rmv,
                botao_lista,
                botao_bc,

            ],

            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            
            )

        principal_centralizado = ft.Row(
            controls=[principal_alinhado],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER

        )

        page.add(
            principal_centralizado,

    )
        page.update()

        # Botão pra adicionar contatos

    def adicionar_contato(e):

        page.controls.clear()

        titulo_add = ft.Text("Adicionar Contato", font_family="SoraM", size=25)

        # Campo de entrada

        input_nome = ft.TextField(label="Nome do contato", label_style=ft.TextStyle(font_family="SoraL", size=14))
        input_telefone = ft.TextField(label="Número do contato", label_style=ft.TextStyle(font_family="SoraL", size=14))
        input_email = ft.TextField(label="Email do contato", label_style=ft.TextStyle(font_family="SoraL", size=14))

        # Botão de cancelar

        cancelar = ft.ElevatedButton(
            "Cancelar",
            color="#FFFFFF",
            bgcolor="#DF0026",
            on_click=principal,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraL",
                    size=16
                )
            )

        )
        # Botão de salvar

        salvar = ft.ElevatedButton(
            "Salvar",
            color="#FFFFFF",
            bgcolor="#2e2e2e",
            on_click=lambda e: Salvar(e, input_nome, input_telefone, input_email),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraL",
                    size=16
                )
            )    
        )

        # Botão de salvar e cancelar alinhados

        salvar_cancelar_alinhados = ft.Row(
            controls=[salvar, cancelar],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        # Campo de entrada alinhados

        add_alinhados = ft.Column(
            controls=[input_nome, input_telefone, input_email],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=15

        )

        page.add(
            ft.Container(height=8),
            ft.Container(content=titulo_add, alignment=ft.alignment.center),
            ft.Container(height=8),
            add_alinhados,
            ft.Container(height=8),
            salvar_cancelar_alinhados,  
    )
        
        page.update()

        # Função para salvar o contato
    
    def Salvar(e, input_nome, input_telefone, input_email):
        nome = input_nome.value
        telefone = input_telefone.value
        email = input_email.value

        if nome:
            agenda[nome] = {"Nome": nome, "Telefone": telefone, "Email": email}

            # Notificações temporárias

            page.snack_bar = ft.SnackBar(
            ft.Text(
                "Contato salvo",
                font_family="SoraM"),
                duration=3000,
                bgcolor="#00FF00"
                        
            )

            page.snack_bar.open = True
            page.update()
            principal(None)
            
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text(
                    "O nome não pode estar vazio!",
                    font_family="SoraL",
                    color="#FFFFFF"),
                    duration=3000,
                    bgcolor="#DF0026"
                )

            page.snack_bar.open = True
            page.update()

        # Botão de remover contatos

    def remover_contato(e):
        page.controls.clear()

        titulo_remover = ft.Text("Remover Contato", font_family="SoraM", size=25)

        input_nome = ft.TextField(label="Nome do contato", label_style=ft.TextStyle(font_family="SoraL"))

        excluir = ft.ElevatedButton(
            text="Excluir",
            color="#FFFFFF",
            bgcolor="#2e2e2e",
            on_click=lambda e: Excluir(e, input_nome),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraL",
                    size=16
                )
            )
        )

        cancelar = ft.ElevatedButton(
            text="Cancelar",
            color="#FFFFFF",
            bgcolor="#DF0026",
            on_click=principal,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraL",
                    size=16
                )
            )
        )

        excluir_cancelar_alinhados = ft.Row(
            controls=[excluir, cancelar],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        page.add(
            ft.Container(height=8),
            ft.Container(content=titulo_remover, alignment=ft.alignment.center),
            ft.Container(height=8),
            input_nome,
            ft.Container(height=8),
            excluir_cancelar_alinhados,

            )
        page.update()


        # Função para excluir o contato

    def Excluir(e, input_nome):
        nome = input_nome.value

        if nome in agenda:
            del agenda[nome]

            # Notificações temporárias

            page.snack_bar = ft.SnackBar(
            ft.Text("Contato excluido", font_family="SoraM"),
            bgcolor="#00FF00",
            duration=3000,
            )
            page.snack_bar.open = True
            page.update()

        else:
            page.snack_bar = ft.SnackBar(
            ft.Text("Contato não encontrado!", font_family="SoraL", color="#FFFFFF"),
            duration=3000,
            bgcolor="#DF0026"
        )
            page.snack_bar.open = True
            page.update()
        
    def lista_contato(e, agenda):
        agenda_alfabetica = sorted(agenda)

        titulo_lista = ft.Text("Lista de Contatos", font_family="SoraM", size=24)

        if agenda_alfabetica:
            page.controls.clear()
            lista = ft.Text("{}".format("\n".join(agenda_alfabetica)), font_family="SoraL", size=20)

            voltar = ft.ElevatedButton(
                text="Voltar",
                color="#FFFFFF",
                bgcolor="#2e2e2e",
                on_click=principal,
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(
                        font_family="SoraL",
                        size=16
                    )
                )
            )

            page.add(
            ft.Container(height=8),
            ft.Container(content=titulo_lista, alignment=ft.alignment.center),
            ft.Container(height=8),
            ft.Container(content=lista, alignment=ft.alignment.center),
            ft.Container(height=4),
            ft.Container(content=voltar, alignment=ft.alignment.center)
            )

        else:
            page.snack_bar = ft.SnackBar(
            ft.Text("Não há nenhum contato salvo!", font_family="SoraL", color="#FFFFFF"),
            duration=3000,
            bgcolor="#DF0026",
        )
            page.snack_bar.open = True
            page.update()

    def page_buscar(e):

        page.controls.clear()

        titulo_buscar = ft.Text("Buscar Contato", font_family="SoraM", size=22)

        input_nome = ft.TextField(label="Insira o nome do contato", label_style=ft.TextStyle(font_family="SoraL"))

        buscar = ft.ElevatedButton(
            text="Buscar",
            color="#FFFFFF",
            bgcolor="#2e2e2e",
            on_click=lambda e: buscar_contato(e, input_nome, agenda),
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraL",
                    size=16
                )
            )
        )

        voltar = ft.ElevatedButton(
            text="Voltar",
            color="#FFFFFF",
            bgcolor="#DF0026",
            on_click=principal,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    font_family="SoraL",
                    size=16
                )
            )
        )

        buscar_voltar = ft.Row(
            controls=[buscar, voltar],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        page.add(
            ft.Container(height=8),
            ft.Container(content=titulo_buscar, alignment=ft.alignment.center),
            ft.Container(height=8),
            input_nome,
            ft.Container(height=4),
            buscar_voltar,
            
            )
        page.update()

    def buscar_contato(e, input_nome, agenda):
        nome = input_nome.value

        if nome in agenda:
            page.controls.clear()

            titulo_buscar_contato = ft.Text("Buscar Contato", font_family="SoraM", size=22)

            input_nome = ft.TextField(label="Insira o nome do contato", label_style=ft.TextStyle(font_family="SoraL"))

            dados = agenda[nome]

            detalhes_contato1 = ft.Text(f"Contato: {dados["Nome"]}", font_family="SoraL", size=16)
            detalhes_contato2 = ft.Text(f"Número: {dados["Telefone"]}", font_family="SoraL", size=16)
            detalhes_contato3 = ft.Text(f"Email: {dados["Email"]}", font_family="SoraL", size=16)

            detalhes_alinhados = ft.Column(
                controls= [detalhes_contato1, detalhes_contato2, detalhes_contato3],
                alignment=ft.MainAxisAlignment.START,
                spacing=6

                )
            
            buscar = ft.ElevatedButton(
                text="Buscar",
                color="#FFFFFF",
                bgcolor="#2e2e2e",
                on_click=lambda e: buscar_contato(e, input_nome, agenda),
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(
                        font_family="SoraL",
                        size=16
                    )
                )
            )

            voltar = ft.ElevatedButton(
                text="Voltar",
                color="#FFFFFF",
                bgcolor="#DF0026",
                on_click=principal,
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(
                        font_family="SoraL",
                        size=16
                    )
                )
            )

            buscar_voltar = ft.Row(
                controls=[buscar, voltar],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            )

            page.add(
            ft.Container(height=8),
            ft.Container(content=titulo_buscar_contato, alignment=ft.alignment.center),
            ft.Container(height=8),
            detalhes_alinhados,
            ft.Container(height=5),
            input_nome,
            ft.Container(height=5),
            buscar_voltar,

            )
            page.update()
        
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("O contato inserido não existe!", font_family="SoraL", color="#FFFFFF"),
                duration=3000,
                bgcolor="#DF0026",
                )
            page.snack_bar.open = True
            page.update()

    page.title = "Agenda"

    principal(None)

ft.app(target= main)