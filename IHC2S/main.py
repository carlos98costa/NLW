import PySimpleGUI as sg

listaClientes = ['Cliente1', 'Cliente2', 'Cliente3']
listPets = []
listVets = ['Vet1', 'Vet2']
pets1 = ['Cachorro1', 'Gato1']
pets2 = ['Cachorro1', 'Gato1', 'Hamster1']
pets3 = ['Hamster1', 'Coelho1', 'Cachorro1', 'Gato1', 'Gato2']

def janela_inicial():
    sg.theme('LightGray1')
    menu_def = [["Menu", ["Sobre", "Equipe", "Contato"]]]
    layout_register = [[sg.MenubarCustom(menu_def, background_color='purple', bar_text_color='purple')],
                        [sg.T('Bem-vindo ao Pet Shop Mi-Au', text_color='purple' ,font='_ 18', justification='c', expand_x=True)],
                        [sg.Image('gato-cachorro2.png')],
                       [sg.Ok('Logar', button_color='purple'), sg.Cancel('Sair', button_color='red')]
                       ]

    return sg.Window('Pet Shop Mi-Au - Inicio', layout=layout_register, finalize=True)

def janela_login():
    sg.theme('LightGray1')
    layout_login = [[sg.T('Fazer Login', font=40, text_color='purple')],
                        [sg.Text("Usuario:", text_color='purple'), sg.Input("", k='-LOGIN-')],
                       [sg.Text("Senha:", text_color='purple'), sg.Input("", k='-SENHA-', password_char="*")],
                       [sg.Ok('Logar', button_color='purple'), sg.Cancel('Voltar', button_color='gray')]
                       ]

    return sg.Window('Pet Shop Mi-Au - Login', layout=layout_login, finalize=True)

def janela_secretario():
    sg.theme('LightGray1')
    layout_secretario = [[sg.T('Painel do Secretario - Inicio', font=40, text_color='purple')],
                        [sg.Button('Marcar consulta', button_color='purple'), sg.Button('Consultas agendadas', button_color='purple')],
                        [sg.Button('Voltar', button_color='gray')]]

    return sg.Window('Pet Shop Mi-Au - Painel Secretario', layout=layout_secretario, finalize=True)

def janela_cadastrar():
    sg.theme('LightGray1')
    layout_marcar_consulta = [[sg.T('Painel do Secretario - Cadastrar', font=40)],
                        [sg.Ok('Manter cliente', button_color='purple'), sg.Ok('Manter animal', button_color='purple')],
                        [sg.Ok('Voltar')]]

    return sg.Window('Pet Shop Mi-Au - Cadastrar', layout=layout_marcar_consulta, finalize=True)


def janela_marcar_consulta():
    sg.theme('LightGray1')
    layout_marcar_consulta = [[sg.T('Painel do Secretario - Marcar consulta', font=40)],
                              [sg.T('Cliente'), sg.LB(listaClientes, size=(10, 4), k='-LCLIENTES-', enable_events=True),
                               sg.T('Pet'), sg.LB(listPets, size=(10, 4), k='-LPETS-', enable_events=True),
                               sg.T('Veterinario'), sg.LB(listVets, size=(10, 4), k='-LVETS-', enable_events=True)
                               ],
                              [sg.T('Buscar cliente pelo nome'),
                               sg.Input(size=(25, 1), enable_events=True, key='-FILTER-'),
                               sg.T(size=(15, 1), k='-FILTER NUMBER-')],
                            [sg.Ok('Manter cliente'), sg.Ok('Manter animal'), sg.Button('Cadastrar cliente', button_color='purple'),
                             sg.Button('Agendar', button_color='purple')],
                            [sg.Ok('Voltar')]]

    return sg.Window('Pet Shop Mi-Au - Marcar consulta', layout=layout_marcar_consulta, finalize=True)


def janela_veterinario():
    sg.theme('LightGray1')
    layout_veterinario= [[sg.T('Painel do Veterinario', font=40)],
                        [sg.Ok('Realizar consulta', button_color='purple'), sg.Button('Consultas agendadas', button_color='purple')],
                         [sg.Cancel('Voltar', button_color='gray')]]

    return sg.Window('Pet Shop Mi-Au - Veterinario', layout=layout_veterinario, finalize=True)

def janela_consulta():
    sg.theme('LightGray1')
    layout_consulta= [[sg.T('Painel do Veterinario - Consulta', font=40, text_color='purple')],
                      [sg.Ok('Informações do animal', button_color='purple')],
                        [sg.Ok('Marcar exame', button_color='purple')],
                         [sg.Ok('Finalizar consulta', button_color='purple'), sg.Cancel('Voltar', button_color='gray')]]

    return sg.Window('Pet Shop Mi-Au - Veterinario Consulta', layout=layout_consulta, finalize=True)

janela1, janela2, janela3, janela4, janela5, janela6 = janela_inicial(), None, None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if window == janela1 and event == 'Logar':
        janela1.hide()
        janela2 = janela_login()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2.un_hide()

    if window == janela2 and event == 'Logar':
        if values['-LOGIN-'] == 'secretaria' and values['-SENHA-'] == '123':
            janela2.hide()
            janela3 = janela_secretario()
        if values['-LOGIN-'] == 'veterinaria' and values['-SENHA-'] == '123':
            janela2.hide()
            janela3 = janela_veterinario()


    if window == janela3 and event == 'Deslogar':
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Realizar consulta':
        janela3.hide()
        janela4 = janela_consulta()

    if window == janela4 and event == 'Finalizar consulta':
        sg.Popup('Consulta finalizada com sucesso!')
        janela4.hide()
        janela3.un_hide()

    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela3.un_hide()

    if event == 'Cadastrar cliente':
        janela5 = janela_cadastrar()
        janela6.hide()

    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela6.un_hide()

    if window == janela3 and event == 'Marcar consulta':
        janela3.hide()
        janela6 = janela_marcar_consulta()
        print('Recebeu janela 6')


    new_list = []
    if window == janela6 and event == '-FILTER-':
        new_list = [i for i in listaClientes if values['-FILTER-'].lower() in i.lower()]
        window['-LCLIENTES-'].update(new_list)
        window['-FILTER NUMBER-'].update(f'{len(new_list)} cliente(s)')


    if window == janela6 and event == '-LCLIENTES-':
        if values['-LCLIENTES-'] == ['Cliente1']:
            window['-LPETS-'].update(pets1)
        if values['-LCLIENTES-'] == ['Cliente2']:
            window['-LPETS-'].update(pets2)
        if values['-LCLIENTES-'] == ['Cliente3']:
            window['-LPETS-'].update(pets3)

    if window == janela6 and event == 'Agendar':
        sg.popup('Consulta agendada com sucesso!')
        janela6.hide()
        janela3.un_hide()
