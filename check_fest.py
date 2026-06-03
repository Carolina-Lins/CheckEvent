import random
from datetime import datetime

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
  while True:
    try:
     valor_servico = input(f"Digite o valor do serviço '{servico}': R$ ")
     valor_formatado = valor_servico.replace(',', '.')

     valor_servico = float(valor_formatado)
     novo_orcamento = orcamento_final - valor_servico

     print(f"Orçamento restante: R$ {novo_orcamento:.2f}")

     if novo_orcamento < 0:
         print("Atenção: Orçamento excedido!")

     return novo_orcamento

    except ValueError:
            print("Entrada inválida! Por favor, digite apenas números (ex: 150.50 ou 150,50).")

def add_evento():
    servicos = []

    nome = input("Digite seu nome: ").capitalize()

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

    convidados = int(input(f"{nome}, informe quantos convidados haverá no {evento}: "))
    orcamento_final = orcamento1


    while True:
        servico_num = int(input(f"\nDigite qual serviço deseja para o {evento}:\n1. Buffet\n2. Banda\n3. Iluminação\n4. Ornamentação\n5. Segurança\n6. Doces e Bolos\n7. Serviços Gráficos\n8. Veículos\n9. Make\n10. Foto e Filmagem\n11. Cerimonial\n12. Outros\nOu '0' para SAIR\n"))

        if servico_num == 12:
            servico = input("Digite o nome do serviço que deseja: ")
            servicos.append(servico)

            orcamento_final = calcular_orcamento(servico, orcamento_final)

        elif servico_num == 0:
            break

        elif servico_num in opcoes_servicos:
            servico_nome = opcoes_servicos[servico_num]
            servicos.append(servico_nome)

            orcamento_final = calcular_orcamento(servico_nome, orcamento_final)

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
        try:
            try:
                data_evento = datetime.strptime(e['data'], '%d/%m/%Y').date()
            except ValueError:
                data_evento = datetime.strptime(e['data'], '%d/%m/%y').date()

            hoje = datetime.now().date()
            dias_restantes = (data_evento - hoje).days

            if dias_restantes > 0:
                print(f"Faltam: {dias_restantes} dias para o evento.")
            elif dias_restantes == 0:
                print("O evento é HOJE!")
            else:
                print(f"O evento já ocorreu há {abs(dias_restantes)} dias.")
        except ValueError:
            print("Não foi possível calcular os dias restantes. Formato de data inválido.")
            
        print(f"Local: {e['local']}")
        print(f"Orçamento: R$ {e['orcamento']:.2f}")
        print(f"Orçamento Final: R$ {e['orcamento_final']:.2f}")
        print(f"Convidados: {e['convidados']}")
        print(f"Serviços: {', '.join(e['servicos']) if e['servicos'] else 'Nenhum serviço selecionado'}")

def listar_todos_eventos():
    if not agenda:
        print("\nNenhum evento cadastrado no momento.")
        return
    
    print("\n--- LISTA DE EVENTOS CADASTRADOS ---")
    for ident, e in agenda.items():
        print(f"ID: {ident} | Cliente: {e['nome']} | Evento: {e['evento']} | Data: {e['data']}")


def excluir_evento():
    ident = int(input("Digite o ID do evento que deseja excluir: "))

    if ident in agenda:
        confirmacao = input(f"Tem certeza que deseja excluir o evento de {agenda[ident]['nome']}? (S/N): ").upper()
        if confirmacao == 'S':
            del agenda[ident]
            print("Evento excluído com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("ID não encontrado.")


def gerar_relatorio_financeiro():
    ident = int(input("Digite o ID do evento para ver o relatório financeiro: "))

    if ident in agenda:
        e = agenda[ident]
        gasto_total = e['orcamento'] - e['orcamento_final']
        
        print(f"\n--- RELATÓRIO FINANCEIRO: {e['evento'].upper()} ({e['nome']}) ---")
        print(f"Orçamento Inicial: R$ {e['orcamento']:.2f}")
        print(f"Gasto Total com Serviços: R$ {gasto_total:.2f}")
        print(f"Saldo Restante: R$ {e['orcamento_final']:.2f}")
        print(f"Total de Convidados: {e['convidados']}")
        
        if e['convidados'] > 0:
            custo_por_convidado = gasto_total / e['convidados']
            print(f"Custo estimado por convidado: R$ {custo_por_convidado:.2f}")
        else:
            print("Não é possível calcular o custo por convidado (0 convidados informados).")
    else:
        print("ID não encontrado.")


def buscar_evento_por_nome():
    nome_busca = input("Digite o nome da pessoa para buscar o evento: ").lower()
    encontrou = False

    print(f"\n--- Resultados para a busca: '{nome_busca}' ---")
    for ident, e in agenda.items():
        if nome_busca in e['nome'].lower():
            encontrou = True
            print(f"\nID: {ident}")
            print(f"Nome: {e['nome']}")
            print(f"Evento: {e['evento']}")
            print(f"Data: {e['data']}")
            try:
                try:
                    data_evento = datetime.strptime(e['data'], '%d/%m/%Y').date()
                except ValueError:
                    data_evento = datetime.strptime(e['data'], '%d/%m/%y').date()

                hoje = datetime.now().date()
                dias_restantes = (data_evento - hoje).days

                if dias_restantes > 0:
                    print(f"Faltam: {dias_restantes} dias para o evento.")
                elif dias_restantes == 0:
                    print("O evento é HOJE!")
                else:
                    print(f"O evento já ocorreu há {abs(dias_restantes)} dias.")
            except ValueError:
                print("Não foi possível calcular os dias restantes. Formato de data inválido.")
            
            print(f"Local: {e['local']}")
            print(f"Orçamento Inicial: R$ {e['orcamento']:.2f}")
            print(f"Orçamento Restante: R$ {e['orcamento_final']:.2f}")
            print(f"Convidados: {e['convidados']}")
            print(f"Serviços: {', '.join(e['servicos']) if e['servicos'] else 'Nenhum serviço selecionado'}")
            print("-" * 30)

    if not encontrou:
        print("Nenhum evento encontrado para este nome.")

while True:
    print("\n--- MENU ---")
    print("1. Cadastrar evento")
    print("2. Buscar evento por ID")
    print("3. Listar todos os eventos")
    print("4. Excluir um evento")
    print("5. Relatório financeiro do evento")
    print("6. Buscar evento por nome do cliente")
    print("0. Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        add_evento()
    elif opcao == 2:
        buscar_evento()
    elif opcao == 3:
        listar_todos_eventos()
    elif opcao == 4:
        excluir_evento()
    elif opcao == 5:
        gerar_relatorio_financeiro()
    elif opcao == 6:
        buscar_evento_por_nome()
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")