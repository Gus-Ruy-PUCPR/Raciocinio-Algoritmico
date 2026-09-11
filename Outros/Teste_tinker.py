import os, random, json
from tkinter import *

def centralizar_janela(janela, largura=500, altura=550):
    """Define o tamanho da janela e a centraliza no monitor."""
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

root = Tk()
root.title("Sistema Gustavo Ruy")
centralizar_janela(root, 500, 550)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=0)

# Frame global para armazenar o conteúdo do menu atual
frame_conteudo = None

# Funções do def inscrição
def popup_attcadastrosTrue():
    popup_cad = Toplevel()
    popup_cad.title("Cadastro")
    centralizar_janela(popup_cad, 250, 100)
    label_popup = Label(popup_cad, text="Cadastrado com sucesso!")
    label_popup.pack(pady=10)
    close_button = Button(popup_cad, text="Fechar", command=popup_cad.destroy)
    close_button.pack()

def popup_attcadastrosFalse():
    popup_cad = Toplevel()
    popup_cad.title("Cadastro")
    centralizar_janela(popup_cad, 250, 100)
    label_popup = Label(popup_cad, text="Cadastro não encontrado!")
    label_popup.pack(pady=10)
    close_button = Button(popup_cad, text="Fechar", command=popup_cad.destroy)
    close_button.pack()

def attcadastros(dicionario, nomeEntry, idadeEntry, cpfEntry, emailEntry, IDs):
    nome = nomeEntry.get(); idade = idadeEntry.get(); cpf = cpfEntry.get(); email = emailEntry.get()
    cadastros = {"nome": nome, "idade": idade, "cpf": cpf, "email": email}
    dicionario[IDs] = cadastros
    if IDs in dicionario:
        with open("clientes.json", 'w') as f:
            json.dump(dicionario, f, indent=2, ensure_ascii=False)
        popup_attcadastrosTrue()
    else:    
        popup_attcadastrosFalse()    

def validar_id(dicionario):
    randomID = f"{random.randint(0,9999):04}"
    if randomID in dicionario:
        return validar_id(dicionario)
    else:
        return randomID

def voltar(frame, botoes):
    for btn in botoes:
        btn.grid()
    if frame:
        frame.destroy()

def inscricao(dicionario, botoes):
    global frame_conteudo
    for btn in botoes:
        btn.grid_remove()

    if frame_conteudo:
        frame_conteudo.destroy()

    frame_conteudo = LabelFrame(root, padx=10, pady=10)
    frame_conteudo.grid(row=5, column=0, padx=20, pady=10, sticky="n")

    text_menu_inscricao = Label(frame_conteudo, text="Inscrição do cliente", borderwidth=1, relief="solid")
    text_menu_inscricao.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    labelNome = Label(frame_conteudo, text="Nome:")
    labelNome.grid(row=1, column=0, sticky="e", padx=2, pady=2)
    nomeEntry = Entry(frame_conteudo)
    nomeEntry.grid(row=1, column=1, padx=2, pady=2)

    labelIdade = Label(frame_conteudo, text="Idade:")
    labelIdade.grid(row=2, column=0, sticky="e", padx=2, pady=2)
    idadeEntry = Entry(frame_conteudo)
    idadeEntry.grid(row=2, column=1, padx=2, pady=2)

    labelCPF = Label(frame_conteudo, text="CPF:")
    labelCPF.grid(row=3, column=0, sticky="e", padx=2, pady=2)
    cpfEntry = Entry(frame_conteudo)
    cpfEntry.grid(row=3, column=1, padx=2, pady=2)

    labelEmail = Label(frame_conteudo, text="Email:")
    labelEmail.grid(row=4, column=0, sticky="e", padx=2, pady=2)
    emailEntry = Entry(frame_conteudo)
    emailEntry.grid(row=4, column=1, padx=2, pady=2)

    entrada_id = StringVar()
    IDs = validar_id(dicionario)
    entrada_id.set(IDs)
    labelID = Label(frame_conteudo, text="ID:")
    labelID.grid(row=5, column=0, sticky="e", padx=2, pady=2)
    idEntry = Entry(frame_conteudo, textvariable=entrada_id, state="readonly")
    idEntry.grid(row=5, column=1, padx=2, pady=2)

    inscricao_buton = Button(frame_conteudo, text="Cadastrar", borderwidth=1, relief="solid", 
                              command=lambda: attcadastros(dicionario, nomeEntry, idadeEntry, cpfEntry, emailEntry, IDs))
    inscricao_buton.grid(row=6, column=1, padx=2, pady=10)

    voltar_button = Button(frame_conteudo, text="Voltar", borderwidth=1, relief="solid", 
                           command=lambda: voltar(frame_conteudo, botoes))
    voltar_button.grid(row=6, column=0, padx=2, pady=10)

# Funções consulta_cadastro com Scrollbar
def buscar_por(dicionario, entry, frame_resultado):
    # Limpa os resultados anteriores
    for widget in frame_resultado.winfo_children():
        widget.destroy()

    busca = entry.get().strip().lower()
    lista_cad = []

    for chave, dados in dicionario.items():
        nome = str(dados.get("nome", "")).lower()
        cpf = str(dados.get("cpf", "")).lower()
        idade = str(dados.get("idade", ""))
        email = str(dados.get("email", ""))

        # Se a caixa estiver vazia (not busca) OU houver correspondência, inclui o cadastro
        if not busca or busca == chave.lower() or busca in nome or busca == cpf:
            lista = f"ID: {chave}\nNome: {dados['nome']}\nIdade: {idade}\nCPF: {cpf}\nEmail: {email}\n" + ("-"*35)
            lista_cad.append(lista)

    if len(lista_cad) > 0:
        string_lista = '\n\n'.join(lista_cad)

        # Widget de Texto com Scrollbar integrada
        text_area = Text(frame_resultado, width=40, height=10, wrap="word")
        scrollbar = Scrollbar(frame_resultado, command=text_area.yview)
        text_area.configure(yscrollcommand=scrollbar.set)

        text_area.insert("1.0", string_lista)
        text_area.config(state="disabled") # Deixa apenas leitura

        text_area.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    else:
        popup_attcadastrosFalse()

def consulta_cadastro(dicionario, botoes):
    global frame_conteudo
    for btn in botoes:
        btn.grid_remove()

    if frame_conteudo:
        frame_conteudo.destroy()

    frame_conteudo = LabelFrame(root, padx=10, pady=10)
    frame_conteudo.grid(row=5, column=0, padx=20, pady=10, sticky="n")

    text_menu_consulta = Label(frame_conteudo, text="Consulta de cliente", borderwidth=1, relief="solid")
    text_menu_consulta.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    label_busca = Label(frame_conteudo, text="Buscar (Nome/CPF/ID):")
    label_busca.grid(row=1, column=0, padx=2, pady=2)

    entry_busca = Entry(frame_conteudo)
    entry_busca.grid(row=1, column=1, padx=2, pady=2)

    # Frame reservado especificamente para renderizar a Scrollbar + Resultados
    frame_resultados = Frame(frame_conteudo)
    frame_resultados.grid(row=3, column=0, columnspan=2, pady=10)

    busca_button = Button(frame_conteudo, text="Buscar", borderwidth=1, relief="solid", 
                          command=lambda: buscar_por(dicionario, entry_busca, frame_resultados))
    busca_button.grid(row=2, column=1, padx=2, pady=5)

    voltar_button = Button(frame_conteudo, text="Voltar", borderwidth=1, relief="solid", 
                           command=lambda: voltar(frame_conteudo, botoes))
    voltar_button.grid(row=2, column=0, padx=2, pady=5)

def ajuda():
    popup_ajuda = Toplevel()
    popup_ajuda.title("Ajuda")
    centralizar_janela(popup_ajuda, 320, 120)
    label_popup = Label(popup_ajuda, text="Para alterar um cadastro, insira ele no menu\nde inscrição com o ID do cadastro a ser alterado.", pady=10)
    label_popup.pack()
    label_button = Button(popup_ajuda, text="Fechar", command=popup_ajuda.destroy)
    label_button.pack()

def carregar_clientes():
    """Carrega o JSON lidando com incompatibilidades de codificação do Windows."""
    if os.path.exists("clientes.json"):
        for enc in ['utf-8', 'cp1252', 'latin-1']:
            try:
                with open("clientes.json", 'r', encoding=enc) as f:
                    dados = json.load(f)
                with open("clientes.json", 'w', encoding='utf-8') as f:
                    json.dump(dados, f, indent=2, ensure_ascii=False)
                return dados
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue

    # Na falta de SQL, usa json mesmo...
    dados_padrao = {
        '1369': {'nome': 'Luiz Kauê Murilo Carvalho', 'idade': 59, 'cpf': '17669981946', 'email': 'luiz_kaue_carvalho@arysta.com.br'}, 
        '1879': {'nome': 'Milena Natália Cardoso', 'idade': 75, 'cpf': '07552372931', 'email': 'milena_cardoso@zignani.com.br'}, 
        '2594': {'nome': 'Julio Sérgio das Neves', 'idade': 69, 'cpf': '97579691418', 'email': 'julio_sergio_dasneves@uol.com.br'}, 
        '2967': {'nome': 'Gabriela Evelyn Eliane Corte Real', 'idade': 20, 'cpf': '44991896916', 'email': 'gabriela_evelyn_cortereal@estagiarios.com'}, 
        '3109': {'nome': 'Lavínia Caroline Emilly Oliveira', 'idade': 57, 'cpf': '56219958640', 'email': 'lavinia_caroline_oliveira@hotmail.com'}, 
        '4736': {'nome': 'Nicolas Joaquim Thiago Rodrigues', 'idade': 43, 'cpf': '92311127322', 'email': 'nicolas-rodrigues73@gustavoscoelho.com.br'}, 
        '4781': {'nome': 'Manuel Alexandre Almeida', 'idade': 22, 'cpf': '57378797200', 'email': 'manuel_alexandre_almeida@soelegancia.com.br'}, 
        '5320': {'nome': 'Fábio Manoel Lima', 'idade': 39, 'cpf': '07390154276', 'email': 'fabio-lima85@coldblock.com.br'}, 
        '5840': {'nome': 'Anthony Samuel dos Santos', 'idade': 28, 'cpf': '72931649988', 'email': 'anthonysamueldossantos@antunez.com.br'}, 
        '6512': {'nome': 'Geraldo Gael Pedro Henrique Moura', 'idade': 33, 'cpf': '79076011770', 'email': 'geraldo-moura70@amoamar.com.br'}, 
        '6809': {'nome': 'Igor Igor Rafael Alves', 'idade': 67, 'cpf': '38403960000', 'email': 'igor_alves@mailnull.com'}, 
        '7325': {'nome': 'Carlos Eduardo Miguel Silva', 'idade': 30, 'cpf': '54449426827', 'email': 'carlos.eduardo.silva@santosferreira.abv.br'}, 
        '8316': {'nome': 'Sebastião Raimundo da Conceição', 'idade': 27, 'cpf': '73035589348', 'email': 'sebastiao_daconceicao@cmfcequipamentos.com.br'}, 
        '8607': {'nome': 'Noah Vicente Igor Freitas', 'idade': 40, 'cpf': '30355893541', 'email': 'noah_vicente_freitas@granvale.com.br'}, 
        '9078': {'nome': 'Mateus Vicente André Ribeiro', 'idade': 44, 'cpf': '68658157504', 'email': 'mateusvicenteribeiro@msds.com.br'}
    }
    with open("clientes.json", 'w', encoding='utf-8') as f:
        json.dump(dados_padrao, f, indent=2, ensure_ascii=False)
    return dados_padrao

def main():
    dicionario_de_dicionarios = carregar_clientes()

    text_menu = Label(root, text="Bem vindo ao sistema de cadastros da loja!", borderwidth=2, relief="solid")
    text_menu.grid(row=0, column=0, padx=5, pady=10)

    inscricao_button = Button(root, text="Inscrição", borderwidth=1, relief="solid")
    consulta_button = Button(root, text="Pesquisar cadastros", borderwidth=1, relief="solid")
    help_button = Button(root, text="Ajuda", borderwidth=1, relief="solid", command=ajuda)

    botoes_principais = [inscricao_button, consulta_button, help_button]

    inscricao_button.config(command=lambda: inscricao(dicionario_de_dicionarios, botoes_principais))
    consulta_button.config(command=lambda: consulta_cadastro(dicionario_de_dicionarios, botoes_principais))

    inscricao_button.grid(row=1, column=0, padx=2, pady=2)
    consulta_button.grid(row=2, column=0, padx=2, pady=2)
    help_button.grid(row=3, column=0, padx=2, pady=2)

    root.mainloop()

if __name__ == "__main__":
    main()