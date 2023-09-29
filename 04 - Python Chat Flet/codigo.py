#gazap
# botao de iniciar chat
# popup para entrar no site
# quando entrar no chat:( aparece para todos)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que envia ( aparece para todos)
    # nome: texto da mensagem
import flet as ft


def main(pagina):
    texto = ft.Text("Uaitizap")
    
    chat = ft.Column()
    nome_usuario = ft.TextField(label="Escreva o seu nome")
    
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: entrou no chat", 
                                         size=12, italic= True, color=ft.colors.BLUE_ACCENT_200))
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({
            "texto": campo_mensagem.value, 
            "usuario": nome_usuario.value,
            "tipo": "mensagem"
            })
        campo_mensagem.value = ""
        pagina.update()
        
    
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    def entrar_popup(event):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.add(ft.Row(
            [
                campo_mensagem, 
                botao_enviar_mensagem
            ]
        ))
        pagina.update()
        
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title= ft.Text("Bem vindo ao Uaitizap"),
        content= nome_usuario,
        actions= [ft.ElevatedButton("Entrar", on_click=entrar_popup)],
    )
    
    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)

# ft.app(target=main , view= ft.AppView.WEB_BROWSER)
ft.app(target=main , view= ft.AppView.FLET_APP, port=8000)