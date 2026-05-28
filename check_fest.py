import random

agenda = {}

opcoes_eventos = {
    1: "Casamento",
    2: "Aniversário",
    3: "Confraternização",
    4: "Reunião",
    5: "Formatura",
    6: "Outro"
}

opcoes_servicos = {
    1: "Buffet",
    2: "Banda",
    3: "Iluminação",
    4: "Ornamentação",
    5: "Segurança",
    6: "Doces e Bolos",
    7: "Serviços Gráficos",
    8: "Veículos",
    9: "Make",
    10: "Foto e Filmagem",
    11: "Cerimonial",
    12: "Outros"
}
def gerar_id():
    return random.randint(10000, 99999)

def calcular_orcamento(servico, orcamento_final):
     valor_servico = float(input(f"Digite o valor do serviço '{servico}': R$ "))
     novo_orcamento = orcamento_final - valor_servico

     print(f"Orçamento restante: R$ {novo_orcamento:.2f}")

     if novo_orcamento < 0:
         print("Atenção: Orçamento excedido!")

     return novo_orcamento

def add_evento():
    servicos = []

    nome = input("Digite seu nome: ")

    evento_num = int(input(f"Olá, {nome}, informe o tipo de evento que deseja realizar:\n1. Casamento\n2. Aniversário\n3. Confraternização\n4. Reunião\n5. Formatura\n6. Outro\n"))
    if evento_num not in opcoes_eventos:
        print("Opção inválida.")
        return
    elif evento_num == 6:
        evento = input("Digite o nome do seu evento: ")
    else:
        evento = opcoes_eventos[evento_num]

    data = input(f"{nome}, informe a data do {evento}: ").lower()
    local = input(f"{nome}, informe o local do {evento}: ").lower()
    while True:
        try:
            orcamento1 = float(input(f"{nome}, informe o orçamento disponível para o {evento}: R$ "))
            break  
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números (use ponto para centavos, ex: 1500.50).")
        
    orcamento1 = float(input(f"{nome}, informe o orçamento disponível para o {evento}: R$ "))
        
    print ("Formato não reconhecido. Favor corrija o valor do orçamento.")
        
    convidados = int(input(f"{nome}, informe quantos convidados haverá no {evento}: "))
    orcamento_final = orcamento1


    while True:
        servico_num = int(input(f"\nDigite qual serviço deseja para o {evento}:\n1. Buffet\n2. Banda\n3. Iluminação\n4. Ornamentação\n5. Segurança\n6. Doces e Bolos\n7. Serviços Gráficos\n8. Veículos\n9. Make\n10. Foto e Filmagem\n11. Cerimonial\n12. Outros\nOu '0' para SAIR\n"))

        if servico_num == 12:
            servico = input("Digite o nome do serviço que deseja: ")
            servicos.append(servico)

            orcamentoFinal = calcular_orcamento(servico, orcamento_final)

        elif servico_num == 0:
            break

        elif servico_num in opcoes_servicos:
            servico_nome = opcoes_servicos[servico_num]
            servicos.append(servico_nome)

            orcamentoFinal = calcular_orcamento(servico_nome, orcamento_final)

        else:
            print("Opção inválida, tente novamente.")

    ident = gerar_id()

    agenda[ident] = {
        "nome": nome,
        "evento": evento,
        "data": data,
        "local": local,
        "orcamento": orcamento1,
        "orcamento_final": orcamento_final,
        "convidados": convidados,
        "servicos": servicos
    }

    print(f"\nEvento cadastrado com sucesso! Seu ID é: {ident}. Guarde-o!")
    return ident

def buscar_evento():
    ident = int(input("Digite o ID do evento: "))
    if ident in agenda:
        e = agenda[ident]
        print(f"\n--- Evento encontrado ---")
        print(f"Nome: {e['nome']}")
        print(f"Evento: {e['evento']}")
        print(f"Data: {e['data']}")
        print(f"Local: {e['local']}")
        print(f"Orçamento: R$ {e['orcamento']:.2f}")
        print(f"Orçamento Final: R$ {e['orcamento_final']:.2f}")
        print(f"Convidados: {e['convidados']}")
        print(f"Serviços: {', '.join(e['servicos']) if e['servicos'] else 'Nenhum serviço selecionado'}")
    else:
        print("ID não encontrado.")

while True:
    print("\n--- MENU ---")
    print("1. Cadastrar evento")
    print("2. Buscar evento por ID")
    print("0. Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        add_evento()
    elif opcao == 2:
        buscar_evento()
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")