# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Calendar.png" alt="Calendar" width="25" height="25" /> CheckEvent - Sistema de Gestão de Eventos

O **CheckEvent** é uma ferramenta de linha de comando desenvolvida em Python para auxiliar no planejamento, controle e execução de eventos de forma prática e organizada. O sistema foi projetado para ajudar organizadores a manterem seus eventos estritamente dentro do prazo e do orçamento previstos.

Este projeto foi desenvolvido como parte dos requisitos avaliativos da disciplina de Fundamentos de Programação.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Inbox%20Tray.png" alt="Inbox Tray" width="25" height="25" />  Funcionalidades

O sistema conta com os seguintes módulos e recursos principais:

#### 1. **Menu Interativo:**
- Cadastrar evento
- Buscar evento por ID
- Buscar evento por nome do cliente
- Atualizar dados de um evento
- Relatório financeiro do evento
- Excluir um evento
- Listar todos os eventos
- Sair

#### 2. **Cada evento armazena:**
- Nome
- Tipo (Aniversário, Casamento, Reunião, etc.) 
- Data do evento 
- Local 
- Orçamento inicial
- Orçamento final
- Quantidade de convidados
- Serviços contratados
     
#### 3. **Gerenciamento de Serviços e Controle de Orçamento Integrado:**
- Cadastro de tarefas específicas (como decoração, buffet, música, etc) vinculando seus respectivos custos.
- O sistema desconta e atualiza automaticamente o saldo do orçamento do evento.
- Alerta sobre estouro de orçamento: Se o total gasto ultrapassar o orçamento inicial, o sistema exibe imediatamente um aviso.
   
#### 4. **Sugestões Personalizadas:**
- Sugestão de Cardápio de acordo com o tipo de evento escolhido e a quantidade de pessoas.

#### 5. **Geração de ID único:**
- Para garantir que os eventos não se misturem e possam ser encontrados facilmente, o programa gera um ID aleatório de 5 dígitos (entre 10000 e 99999) assim que o cadastro é concluído com sucesso.
- Esse ID funciona como a "chave de acesso" do evento. Se o usuário não lembrar do ID pode fazer a busca do seu evento pelo nome.
   
#### 6. **Contagem Regressiva:** 
- Exibição automatizada de quantos dias faltam para a realização do evento ao visualizá-lo.
   
#### 7. **Funcionalidade Extra:**
- Relatórios financeiros detalhados, o sistema gera nota fiscal com um resumo completo com custos, saldo restante e custo por convidado.
---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20Index%20Dividers.png" alt="Card Index Dividers" width="25" height="25" /> Banco de Dados

Todos os dados são armazenados em um arquivo `.txt` local utilizando separadores (`|`) para estruturar as informações, garantindo persistência simples sem uso de banco de dados externo.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Warning.png" alt="Warning" width="25" height="25" />  Pré-requisitos e Restrições Técnicas

O projeto foi construído seguindo rigorosamente as diretrizes de desenvolvimento do ecossistema nativo do Python:
* **Linguagem:** Python 3.x 
* **Dependências:** Nenhuma biblioteca externa foi utilizada.
* **Bibliotecas Nativas Permitidas:**
  - `os`
  - `datetime`
  - `random`
* **Interface:** Interação baseada 100% em linha de comando (CLI) via terminal.

---

##  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Key.png" alt="Key" width="25" height="25" />  Como Executar
1. Certifique-se de ter o Python instalado em sua máquina. 
2. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/Carolina-Lins/CheckEvent.git
   ```
3. Navegue até o diretório do projeto:
   ```bash
   cd CheckEvent
    ```
4. Execute o arquivo principal do sistema:
   ```bash
   python check_event.py
   ```
   
---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Memo.png" alt="Memo" width="25" height="25" />  Licença 

Educacional e não comercial.

 ---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Handshake.png" alt="Handshake" width="25" height="25" /> Colaboradores

Integrante 1 - Alexandre Miranda [(https://github.com/aabmiranda-ops)]

Integrante 2 - Bernardo Acioli  [(https://github.com/aciolibernardo-code)]

Integrante 3 - Maria Carolina Lins [(https://github.com/Carolina-Lins)]

Integrante 4 - Mirna Cordeiro [(https://github.com/Mirnacls)]
