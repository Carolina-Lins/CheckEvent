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

def limpar_tela():
    """Limpa o terminal de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados():
    global agenda
    if os.path.exists(ARQUIVO_TXT):
        with open(ARQUIVO_TXT, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip() 
                if not linha:
                    continue 
                
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
                    servicos = {}
                    if servicos_str:
                        itens = servicos_str.split(',')
                        for item in itens:
                            if ':' in item:
                                s_nome, s_valor = item.split(':')
                                servicos[s_nome] = float(s_valor)
                            else:
                                servicos[item] = 0.0
                        
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
            servicos_str = ",".join([f"{k}:{v}" for k, v in e['servicos'].items()])
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

            return novo_orcamento, valor_servico

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
    limpar_tela()
    servicos = {}
    
    while True:
        nome = input("Digite seu nome: ")
        if nome.replace(" ", "").isalpha():
            nome = nome.capitalize()
            break
        else:
            print("❌ Erro: O nome não pode conter números ou símbolos. Digite apenas letras.")

    while True:
        try:
            evento_num = int(input(f"Olá, {nome}, informe o tipo de evento que deseja realizar:\n1. Casamento\n2. Aniversário\n3. Confraternização\n4. Reunião\n5. Formatura\n6. Outro\n=> "))
            if evento_num not in opcoes_eventos:
                print("❌ Opção inválida. Escolha um número de 1 a 6.")
                continue
            
            if evento_num == 6:
                while True:
                    evento = input("Digite o nome do seu evento: ")
                    if not any(char.isdigit() for char in evento): 
                        break
                    print("❌ Erro: O nome do evento não pode conter números.")
                break
            else:
                evento = opcoes_eventos[evento_num]
                break
        except ValueError:
            print("❌ Erro: Digite apenas o número correspondente à opção.")

    while True:
        data_str = input(f"{nome}, informe a data do {evento} (DD/MM/AAAA): ")
        try:
            evento_data = datetime.strptime(data_str, "%d/%m/%Y").date()
            hoje = datetime.now().date()

            if evento_data < hoje:
                confirma_data = input("A data do evento já passou, deseja continuar mesmo assim? (S/N): ").upper()
                if confirma_data != 'S':
                    print("Por favor, informe a data novamente.")
                    continue 
            break 
        except ValueError:
            print("❌ O formato de data não é válido! Tente novamente no padrão DD/MM/AAAA.")

    while True:
        local = input(f"{nome}, informe o local do {evento} (sem números): ").lower()
        if not any(char.isdigit() for char in local):
            break
        print("❌ Erro: O nome do local não pode conter números. Digite apenas o nome do espaço.")

    while True:
        try:
            orcamento1 = float(input(f"{nome}, informe o orçamento disponível para o {evento}: R$ "))
            if orcamento1 > 0:
                break
            print("❌ O orçamento deve ser maior que zero.")
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite apenas números (use ponto para centavos).")

    while True:
        try:
            convidados = int(input(f"{nome}, informe quantos convidados haverá no {evento}: "))
            if convidados > 0:
                break
            print("❌ A quantidade de convidados deve ser maior que zero.")
        except ValueError:
            print("❌ Erro: Digite apenas números inteiros para os convidados.")
            
    orcamento_final = orcamento1
    sugestoes_eventos(evento, convidados)

    while True:
        try:
            servico_num = int(input(f"\nDigite qual serviço deseja para o {evento}:\n1. Buffet\n2. Banda\n3. Iluminação\n4. Ornamentação\n5. Segurança\n6. Doces e Bolos\n7. Serviços Gráficos\n8. Veículos\n9. Make\n10. Foto e Filmagem\n11. Cerimonial\n12. Outros\nOu '0' para FINALIZAR\n=> "))
        except ValueError:
            print("❌ Opção inválida. Digite apenas o número do serviço.")
            continue

        if servico_num == 12:
            while True:
                servico = input("Digite o nome do serviço que deseja: ")
                if not any(char.isdigit() for char in servico):
                    break
                print("❌ Erro: O nome não pode conter números.")
            
            orcamento_final, valor = calcular_orcamento(servico, orcamento_final)
            servicos[servico] = valor

        elif servico_num == 0:
            break

        elif servico_num in opcoes_servicos:
            servico_nome = opcoes_servicos[servico_num]
            orcamento_final, valor = calcular_orcamento(servico_nome, orcamento_final)
            servicos[servico_nome] = valor
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
    limpar_tela()
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
            print(f"Orçamento Inicial: R$ {e['orcamento']:.2f}")
            print(f"Orçamento Restante: R$ {e['orcamento_final']:.2f}")
            print(f"Convidados: {e['convidados']}")
            
            if e['servicos']:
                servicos_formatados = ", ".join([f"{k} (R$ {v:.2f})" for k, v in e['servicos'].items()])
                print(f"Serviços: {servicos_formatados}")
            else:
                print("Serviços: Nenhum serviço selecionado")
            
            break 
        else:
            print("❌ ID não encontrado no sistema. Verifique o número e tente novamente.")

def listar_todos_eventos():
    limpar_tela()
    if not agenda:
        print("\n❌ Nenhum evento cadastrado no momento.")
        return
    
    print("\n--- LISTA DE EVENTOS CADASTRADOS ---")
    for ident, e in agenda.items():
        print(f"ID: {ident} | Cliente: {e['nome']} | Evento: {e['evento']} | Data: {e['data']}")

def excluir_evento():
    limpar_tela()
    try:
        ident = int(input("Digite o ID do evento que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    if ident in agenda:
        confirmacao = input(f"Tem certeza que deseja excluir o evento de {agenda[ident]['nome']}? (S/N): ").upper()
        if confirmacao == 'S':
            del agenda[ident]
            salvar_dados() 
            print("🗑️ Evento excluído com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("ID não encontrado.")

def update_evento():
    limpar_tela()
    try:
        ident = int(input("Digite o ID do evento que deseja atualizar: "))
    except ValueError:
        print("❌ ID inválido. Digite apenas números.")
        return

    if ident in agenda:
        e = agenda[ident]
        
        while True:
            limpar_tela()
            print(f"\n--- 📝 EDITANDO O EVENTO DE {e['nome'].upper()} ---")
            print(f"💰 Orçamento Restante Atual: R$ {e['orcamento_final']:.2f}")
            
            print("\nO que você deseja alterar?")
            print("1. Alterar Data")
            print("2. Alterar Local")
            print("3. Alterar Quantidade de Convidados")
            print("4. ADICIONAR Novo Serviço")
            print("5. EDITAR Valor de um Serviço Específico")
            print("6. EXCLUIR um Serviço Específico")
            print("7. Alterar Orçamento Inicial Total")
            print("8. Resetar TODOS os Serviços (Limpa a lista e devolve o dinheiro)")
            print("0. Finalizar alterações e Sair")
            
            try:
                opcao_update = int(input("\nEscolha uma opção: "))
            except ValueError:
                print("❌ Opção inválida. Digite um número.")
                input("\nPressione ENTER para tentar novamente...")
                continue
            
            if opcao_update == 1:
                while True:
                    nova_data = input(f"Nova data (Atual: {e['data']}) (DD/MM/AAAA) ou '0' para cancelar: ")
                    if nova_data == '0':
                        break
                    try:
                        datetime.strptime(nova_data, "%d/%m/%Y")
                        e['data'] = nova_data
                        print("✅ Data atualizada com sucesso!")
                        break 
                    except ValueError:
                        print("❌ Formato de data inválido! Tente no padrão DD/MM/AAAA.")
                input("\nPressione ENTER para continuar...")
                    
            elif opcao_update == 2:
                while True:
                    novo_local = input(f"Novo local (Atual: {e['local']}) ou '0' para cancelar: ").lower()
                    if novo_local == '0':
                        break
                    if not any(char.isdigit() for char in novo_local):
                        e['local'] = novo_local
                        print("✅ Local atualizado com sucesso!")
                        break
                    else:
                        print("❌ Erro: O nome do local não pode conter números.")
                input("\nPressione ENTER para continuar...")
                
            elif opcao_update == 3:
                while True:
                    entrada_convidados = input(f"Nova quantidade (Atual: {e['convidados']}) ou '0' para cancelar: ")
                    if entrada_convidados == '0':
                        break
                    try:
                        novos_convidados = int(entrada_convidados)
                        if novos_convidados > 0:
                            e['convidados'] = novos_convidados
                            print("✅ Quantidade de convidados atualizada!")
                            sugestoes_eventos(e['evento'], novos_convidados)
                            break
                        else:
                            print("❌ A quantidade deve ser maior que zero.")
                    except ValueError:
                        print("❌ Entrada inválida! Digite apenas números inteiros.")
                input("\nPressione ENTER para continuar...")
                        
            elif opcao_update == 4:
                try:
                    servico_num = int(input(f"\nQual serviço deseja ADICIONAR:\n1. Buffet\n2. Banda\n3. Iluminação\n4. Ornamentação\n5. Segurança\n6. Doces e Bolos\n7. Serviços Gráficos\n8. Veículos\n9. Make\n10. Foto e Filmagem\n11. Cerimonial\n12. Outros\nOu '0' para CANCELAR\n=> "))
                except ValueError:
                    print("❌ Opção inválida.")
                    input("\nPressione ENTER para continuar...")
                    continue

                if servico_num == 0:
                    continue
                elif servico_num == 12:
                    while True:
                        servico = input("Digite o nome do serviço que deseja: ")
                        if not any(char.isdigit() for char in servico):
                            break
                        print("❌ Erro: O nome não pode conter números.")
                    orc_temp, valor = calcular_orcamento(servico, e['orcamento_final'])
                    e['orcamento_final'] = orc_temp
                    e['servicos'][servico] = valor
                elif servico_num in opcoes_servicos:
                    servico_nome = opcoes_servicos[servico_num]
                    orc_temp, valor = calcular_orcamento(servico_nome, e['orcamento_final'])
                    e['orcamento_final'] = orc_temp
                    e['servicos'][servico_nome] = valor
                else:
                    print("❌ Opção inválida.")
                input("\nPressione ENTER para continuar...")
            
            elif opcao_update == 5:
                if not e['servicos']:
                    print("❌ Você ainda não adicionou nenhum serviço para poder editar.")
                    input("\nPressione ENTER para continuar...")
                    continue
                    
                lista_serv = list(e['servicos'].keys())
                print("\n--- EDITAR VALOR DE UM SERVIÇO ---")
                for i, s_nome in enumerate(lista_serv):
                    print(f"{i+1}. {s_nome} (Valor atual: R$ {e['servicos'][s_nome]:.2f})")
                
                try:
                    idx = int(input("\nDigite o NÚMERO do serviço para alterar o valor (ou 0 para cancelar): "))
                    if idx == 0:
                        continue
                    if 1 <= idx <= len(lista_serv):
                        s_nome_escolhido = lista_serv[idx-1]
                        valor_antigo = e['servicos'][s_nome_escolhido]
                        
                        novo_v_str = input(f"Digite o NOVO valor para '{s_nome_escolhido}': R$ ")
                        novo_v_float = float(novo_v_str.replace(',', '.'))
                        if novo_v_float >= 0:
                            e['orcamento_final'] = e['orcamento_final'] + valor_antigo - novo_v_float
                            e['servicos'][s_nome_escolhido] = novo_v_float
                            print(f"✅ Valor de '{s_nome_escolhido}' atualizado de R$ {valor_antigo:.2f} para R$ {novo_v_float:.2f}!")
                            print(f"💰 Novo Orçamento Restante: R$ {e['orcamento_final']:.2f}")
                        else:
                            print("❌ O valor não pode ser negativo.")
                    else:
                        print("❌ Número inválido.")
                except ValueError:
                    print("❌ Entrada inválida. Digite apenas números.")
                input("\nPressione ENTER para continuar...")

            elif opcao_update == 6:
                if not e['servicos']:
                    print("❌ Você não tem nenhum serviço para excluir.")
                    input("\nPressione ENTER para continuar...")
                    continue
                    
                lista_serv = list(e['servicos'].keys())
                print("\n--- EXCLUIR APENAS UM SERVIÇO ---")
                for i, s_nome in enumerate(lista_serv):
                    print(f"{i+1}. {s_nome} (Valor: R$ {e['servicos'][s_nome]:.2f})")
                
                try:
                    idx = int(input("\nDigite o NÚMERO do serviço que deseja excluir (ou 0 para cancelar): "))
                    if idx == 0:
                        continue
                    if 1 <= idx <= len(lista_serv):
                        s_nome_escolhido = lista_serv[idx-1]
                        valor_antigo = e['servicos'][s_nome_escolhido]
                        
                        del e['servicos'][s_nome_escolhido]
                        e['orcamento_final'] += valor_antigo
                        print(f"✅ Serviço '{s_nome_escolhido}' excluído da lista!")
                        print(f"💸 O valor de R$ {valor_antigo:.2f} foi devolvido ao seu orçamento.")
                        print(f"💰 Novo Orçamento Restante: R$ {e['orcamento_final']:.2f}")
                    else:
                        print("❌ Número inválido.")
                except ValueError:
                    print("❌ Entrada inválida. Digite apenas números.")
                input("\nPressione ENTER para continuar...")
                        
            elif opcao_update == 7:
                while True:
                    entrada_orc = input(f"Novo Orçamento Inicial (Atual: R$ {e['orcamento']:.2f}) ou '0' para cancelar: R$ ")
                    if entrada_orc == '0':
                        break
                    try:
                        novo_orcamento = float(entrada_orc.replace(',', '.'))
                        if novo_orcamento > 0:
                            diferenca = novo_orcamento - e['orcamento']
                            e['orcamento'] = novo_orcamento
                            e['orcamento_final'] += diferenca
                            print(f"✅ Orçamento inicial atualizado!")
                            print(f"💰 Novo saldo restante ajustado para: R$ {e['orcamento_final']:.2f}")
                            break
                        else:
                            print("❌ O orçamento deve ser maior que zero.")
                    except ValueError:
                        print("❌ Entrada inválida! Digite apenas números.")
                input("\nPressione ENTER para continuar...")
            
            elif opcao_update == 8:
                print(f"\n⚠️ ATENÇÃO: Isso irá apagar todos os serviços ({len(e['servicos'])}) e restaurar o saldo para R$ {e['orcamento']:.2f}.")
                confirm = input("Tem certeza que deseja resetar os serviços? (S/N): ").upper()
                if confirm == 'S':
                    e['servicos'] = {}
                    e['orcamento_final'] = e['orcamento']
                    print("✅ Todos os serviços foram apagados! O saldo foi totalmente restaurado.")
                else:
                    print("❌ Operação cancelada.")
                input("\nPressione ENTER para continuar...")

            elif opcao_update == 0:
                salvar_dados() 
                print("💾 Retornando ao menu principal... Alterações salvas!")
                break
            else:
                print("❌ Opção inválida.")
                input("\nPressione ENTER para tentar novamente...")
    else:
        print("❌ ID não encontrado no sistema.")

def gerar_relatorio_financeiro():
    limpar_tela()
    entrada = input("Digite o ID do evento ou o Nome do cliente para ver o relatório: ")
    
    eventos_encontrados = []

    if entrada.isdigit():
        ident = int(entrada)
        if ident in agenda:
            eventos_encontrados.append((ident, agenda[ident]))
    else:
        nome_busca = entrada.lower()
        for ident, e in agenda.items():
            if nome_busca in e['nome'].lower():
                eventos_encontrados.append((ident, e))

    if not eventos_encontrados:
        print("❌ Nenhum evento encontrado para esta busca.")
        return

    for ident, e in eventos_encontrados:
        gasto_total = e['orcamento'] - e['orcamento_final']
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        print("\n" + "="*45)
        print(f"{'C H E C K   E V E N T':^45}")
        print(f"{'CUPOM / NOTA FISCAL':^45}")
        print("="*45)
        print(f" DATA: {data_atual:<19} ID: {ident}")
        print(f" CLIENTE: {e['nome']}")
        print(f" EVENTO: {e['evento']}")
        print("-" * 45)
        print(f"{'DESCRIÇÃO DOS SERVIÇOS':^45}")
        print("-" * 45)
        
        if e['servicos']:
            for s_nome, s_valor in e['servicos'].items():
                linha_servico = f"{s_nome} (R$ {s_valor:.2f})"
                print(f" * {linha_servico:<41}")
        else:
            print(f"{'(Nenhum serviço contratado)':^45}")
            
        print("-" * 45)
        print(" RESUMO FINANCEIRO")
        print("-" * 45)
        print(f" Orçamento Inicial:           R$ {e['orcamento']:>10.2f}")
        print(f" Total Gasto:                 R$ {gasto_total:>10.2f}")
        print("." * 45)
        print(f" SALDO RESTANTE:              R$ {e['orcamento_final']:>10.2f}")
        print("=" * 45)
        print(" ESTATÍSTICAS DO EVENTO")
        print("." * 45)
        print(f" Total de Convidados: {e['convidados']:>23}")
        
        if e['convidados'] > 0:
            custo_por_convidado = gasto_total / e['convidados']
            print(f" Custo/Convidado (Estimado):  R$ {custo_por_convidado:>10.2f}")
        else:
            print(f" Custo/Convidado:        (Sem convidados)")
            
        print("=" * 45)
        print(f"{'Obrigado pela preferência!':^45}")
        print("=" * 45 + "\n")

def buscar_evento_por_nome():
    limpar_tela()
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
            
            if e['servicos']:
                servicos_formatados = ", ".join([f"{k} (R$ {v:.2f})" for k, v in e['servicos'].items()])
                print(f"Serviços: {servicos_formatados}")
            else:
                print("Serviços: Nenhum serviço selecionado")
            
            print("-" * 30)

    if not encontrou:
        print(" ❌ Nenhum evento encontrado para este nome.")

carregar_dados() 

while True:
    limpar_tela()
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
        input("\nPressione ENTER para tentar novamente...")
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
        limpar_tela()
        print("Saindo... Obrigado por usar o Check Event! 👋")
        break
    else:
        print("❌ Opção inválida. Por favor, escolha um número entre 0 e 7.")
        
    if opcao != 0 and opcao != 4: 
        input("\nPressione ENTER para voltar ao menu...")