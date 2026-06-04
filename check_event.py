import random
import os
from datetime import datetime

agenda = {}
ARQUIVO_TXT = "agenda_salva.txt"

opcoes_eventos = {
    1: "Casamento",
    2: "Aniversário",
    3: "Confraternização",
    4: "Reunião",
    5: "Formatura",
    6: "Outro"
}

opcoes_servicos = {
    1: "Buffet", 2: "Banda", 3: "Iluminação", 4: "Ornamentação", 
    5: "Segurança", 6: "Doces e Bolos", 7: "Serviços Gráficos", 8: "Veículos",
    9: "Make", 10: "Foto e Filmagem", 11: "Cerimonial", 12: "Outros"
}

def carregar_dados():
    global agenda
    if os.path.exists(ARQUIVO_TXT):
        with open(ARQUIVO_TXT, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip() # Remove espaços e quebras de linha nas pontas
                if not linha:
                    continue # Pula linhas vazias
                
                # Quebramos a linha toda vez que encontrar a barra '|'
                partes = linha.split('|')
                
                if len(partes) == 9:
                    ident = int(partes[0])
                    nome = partes[1]
                    evento = partes[2]
                    data_str = partes[3]
                    local = partes[4]
                    orcamento = float(partes[5])
                    orcamento_final = float(partes[6])
                    convidados = int(partes[7])
                    
                    servicos_str = partes[8]
                    if servicos_str:
                        servicos = servicos_str.split(',')
                    else:
                        servicos = []
                        
                    agenda[ident] = {
                        "nome": nome,
                        "evento": evento,
                        "data": data_str,
                        "local": local,
                        "orcamento": orcamento,
                        "orcamento_final": orcamento_final,
                        "convidados": convidados,
                        "servicos": servicos
                    }

def salvar_dados():
    with open(ARQUIVO_TXT, 'w', encoding='utf-8') as arquivo:
        for ident, e in agenda.items():
            servicos_str = ",".join(e['servicos'])
            
            linha = f"{ident}|{e['nome']}|{e['evento']}|{e['data']}|{e['local']}|{e['orcamento']}|{e['orcamento_final']}|{e['convidados']}|{servicos_str}\n"
            
            arquivo.write(linha)

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

            if novo_orcamento <= 0:
                print(" ⚠️ Atenção: Orçamento excedido ou no limite!")

            return novo_orcamento

        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números (ex: 150.50 ou 150,50).")

def sugestoes_eventos(evento, convidados):
    print("\n" + "="*40)
    print("💡 SUGESTÕES PERSONALIZADAS DO SISTEMA")
    if evento == "Casamento":
        print("- Dica de Cardápio: Jantar empratado ou buffet completo são ideais.")
        print("- Dica de Fornecedor: Não esqueça de contratar um bom fotógrafo e banda!")
    elif evento == "Aniversário":
        print("- Dica de Cardápio: Salgadinhos tradicionais, bolo decorado e doces.")
        print("- Decoração: Balões e painéis temáticos são o diferencial.")
    elif evento == "Reunião" or evento == "Confraternização":
        print("- Dica de Cardápio: Coffee break, finger foods ou churrasco são bastante utilizados.")

    if convidados > 100:
        print(f"- Estrutura: Para {convidados} pessoas, sugerimos locar um espaço amplo e contratar equipe de limpeza.")
    elif convidados < 40:
        print(f"- Estrutura: Um evento íntimo para {convidados} pessoas permite maior investimento na qualidade do buffet e lembrancinhas.")
    print("="*40 + "\n")

def add_evento():
    servicos = []
    
    while True:
        nome = input("Digite seu nome: ")
        
        if nome.replace(" ", "").isalpha():
            nome = nome.capitalize()
            break
        else:
            print("❌ Erro: O nome não pode conter números ou símbolos. Digite apenas letras.")

    evento_num = int(input(f"Olá, {nome}, informe o tipo de evento que deseja realizar:\n1. Casamento\n2. Aniversário\n3. Confraternização\n4. Reunião\n5. Formatura\n6. Outro\n"))
    if evento_num not in opcoes_eventos:
        print("Opção inválida.")
        return
    elif evento_num == 6:
        evento = input("Digite o nome do seu evento: ")
    else:
        evento = opcoes_eventos[evento_num]

    data_str = input(f"{nome}, informe a data do {evento} (DD/MM/AAAA): ")
    
    try:
        evento_data = datetime.strptime(data_str, "%d/%m/%Y").date()
        hoje = datetime.now().date()

        if evento_data < hoje:
            confirma_data = input("A data do evento já passou, deseja continuar mesmo assim? S/N: ").upper()
            if confirma_data != 'S':
                print("❌ Operação cancelada")
                return
    except ValueError:
        print("❌ O formato de data não é válido! Operação Cancelada.")
        return

    local = input(f"{nome}, informe o local do {evento}: ").lower()
    while True:
        try:
            orcamento1 = float(input(f"{nome}, informe o orçamento disponível para o {evento}: R$ "))
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números (use ponto para centavos, ex: 1500.50).")

    convidados = int(input(f"{nome}, informe quantos convidados haverá no {evento}: "))
    orcamento_final = orcamento1

    sugestoes_eventos(evento, convidados)

    while True:
        servico_num = int(input(f"\nDigite qual serviço deseja para o {evento}:\n1. Buffet\n2. Banda\n3. Iluminação\n4. Ornamentação\n5. Segurança\n6. Doces e Bolos\n7. Serviços Gráficos\n8. Veículos\n9. Make\n10. Foto e Filmagem\n11. Cerimonial\n12. Outros\nOu '0' para FINALIZAR\n"))

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
        "data": data_str,
        "local": local,
        "orcamento": orcamento1,
        "orcamento_final": orcamento_final,
        "convidados": convidados,
        "servicos": servicos
    }
    
    salvar_dados() 
    print(f"\n ✅ Evento cadastrado com sucesso! Seu ID é: {ident}. Guarde-o!")
    return ident

def buscar_evento():
    while True:
        entrada = input("\nDigite o ID do evento (ou digite '0' para voltar ao menu): ")
        
        if entrada == '0':
            print("Retornando ao menu principal...")
            return

        try:
            ident = int(entrada)
        except ValueError:
            print("❌ Erro: ID inválido! Por favor, digite apenas números.")
            continue 

        if ident in agenda:
            e = agenda[ident]
            print(f"\n--- 📅 Evento encontrado ---")
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
                    print(f"⏳ Faltam: {dias_restantes} dias para o evento.")
                elif dias_restantes == 0:
                    print("🎉 O evento é HOJE!")
                else:
                    print(f"🕰️ O evento já ocorreu há {abs(dias_restantes)} dias.")
            except ValueError:
                print(" ⚠️ Não foi possível calcular os dias restantes. Formato de data inválido.")
                
            print(f"Local: {e['local']}")
            print(f"Orçamento: R$ {e['orcamento']:.2f}")
            print(f"Orçamento Final: R$ {e['orcamento_final']:.2f}")
            print(f"Convidados: {e['convidados']}")
            print(f"Serviços: {', '.join(e['servicos']) if e['servicos'] else 'Nenhum serviço selecionado'}")
            
            break 
        else:
            print("❌ ID não encontrado no sistema. Verifique o número e tente novamente.")

def listar_todos_eventos():
    if not agenda:
        print("\n❌ Nenhum evento cadastrado no momento.")
        return
    
    print("\n--- LISTA DE EVENTOS CADASTRADOS ---")
    for ident, e in agenda.items():
        print(f"ID: {ident} | Cliente: {e['nome']} | Evento: {e['evento']} | Data: {e['data']}")

def excluir_evento():
    try:
        ident = int(input("Digite o ID do evento que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    if ident in agenda:
        confirmacao = input(f"Tem certeza que deseja excluir o evento de {agenda[ident]['nome']}? (S/N): ").upper()
        if confirmacao == 'S':
            del agenda[ident]
            salvar_dados() # Atualiza o txt
            print("🗑️ Evento excluído com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("ID não encontrado.")

def update_evento():
    try:
        ident = int(input("Digite o ID do evento que deseja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    if ident in agenda:
        e = agenda[ident]
        print(f"\n--- 📝 Editando o evento de {e['nome']} ({e['evento']}) ---")
        
        while True:
            print("\nO que você deseja alterar?")
            print("1. Alterar Data")
            print("2. Alterar Local")
            print("3. Alterar Quantidade de Convidados")
            print("0. Finalizar alterações")
            
            try:
                opcao_update = int(input("\nEscolha uma opção: "))
            except ValueError:
                print("Opção inválida.")
                continue
            
            if opcao_update == 1:
                nova_data = input(f"Nova data (Data atual: {e['data']}) (DD/MM/AAAA): ")
                try:
                    datetime.strptime(nova_data, "%d/%m/%Y")
                    e['data'] = nova_data
                    print("Data atualizada com sucesso!")
                except ValueError:
                    print("Formato de data inválido! A data não foi alterada.")
                    
            elif opcao_update == 2:
                novo_local = input(f"Novo local (Local atual: {e['local']}): ").lower()
                e['local'] = novo_local
                print("Local atualizado com sucesso!")
                
            elif opcao_update == 3:
                try:
                    novos_convidados = int(input(f"Nova quantidade de convidados (Atual: {e['convidados']}): "))
                    e['convidados'] = novos_convidados
                    print("Quantidade de convidados atualizada!")
                    sugestoes_eventos(e['evento'], novos_convidados)
                except ValueError:
                    print("Entrada inválida! Digite apenas números inteiros.")
                    
            elif opcao_update == 0:
                salvar_dados() # Salva no txt ao finalizar
                print(" Retornando ao menu principal... Alterações salvas!")
                break
            else:
                print("Opção inválida.")
    else:
        print("ID não encontrado.")

def gerar_relatorio_financeiro():
    try:
        ident = int(input("Digite o ID do evento para ver o relatório financeiro: "))
    except ValueError:
        print("ID inválido.")
        return

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
        print("❌ ID não encontrado.")

def buscar_evento_por_nome():
    nome_busca = input("Digite o nome da pessoa para buscar o evento: ").lower()
    encontrou = False

    print(f"\n--- Resultados para a busca: '{nome_busca}' ---")
    for ident, e in agenda.items():
        if nome_busca in e['nome'].lower():
            encontrou = True
            print(f"\n--- 📅 Evento encontrado ---")
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
                    print(f"⏳ Faltam: {dias_restantes} dias para o evento.")
                elif dias_restantes == 0:
                    print("🎉 O evento é HOJE!")
                else:
                    print(f"🕰️ O evento já ocorreu há {abs(dias_restantes)} dias.")
            except ValueError:
                print("⚠️ Não foi possível calcular os dias restantes. Formato de data inválido.")
            
            print(f"Local: {e['local']}")
            print(f"Orçamento Inicial: R$ {e['orcamento']:.2f}")
            print(f"Orçamento Restante: R$ {e['orcamento_final']:.2f}")
            print(f"Convidados: {e['convidados']}")
            print(f"Serviços: {', '.join(e['servicos']) if e['servicos'] else 'Nenhum serviço selecionado'}")
            print("-" * 30)

    if not encontrou:
        print(" ❌ Nenhum evento encontrado para este nome.")

carregar_dados() 

while True:
    print("\n---------- MENU ----------")
    print("1. Cadastrar evento")
    print("2. Buscar evento por ID")
    print("3. Buscar evento por nome do cliente")
    print("4. Atualizar dados de um evento")
    print("5. Relatório financeiro do evento")
    print("6. Excluir um evento")
    print("7. Listar todos os eventos")
    print("0. Sair")
    
    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("❌ Opção inválida. Digite um número.")
        continue
    if opcao == 1:
        add_evento()
    elif opcao == 2:
        buscar_evento()
    elif opcao == 3:
        buscar_evento_por_nome()
    elif opcao == 4:
        update_evento()
    elif opcao == 5:
        gerar_relatorio_financeiro()
    elif opcao == 6:
        excluir_evento()
    elif opcao == 7:
        listar_todos_eventos()
    elif opcao == 0:
        print("Saindo... Obrigado por usar o Check Event! 👋")
        break
    else:
        print("❌ Opção inválida. Por favor, escolha um número entre 0 e 7.")