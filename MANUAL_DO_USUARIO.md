# 📖 Manual do Usuário - CheckEvent

## Sobre o Sistema

O CheckEvent é um sistema de gerenciamento de eventos desenvolvido em Python que auxilia usuários no planejamento, controle financeiro e organização de eventos.

O sistema permite cadastrar eventos, controlar serviços contratados, monitorar o orçamento disponível e gerar relatórios financeiros detalhados.

---

# 📅 Iniciando o Sistema

Após executar o programa, será exibido o menu principal:

```text
---------- MENU ----------
1. Cadastrar evento
2. Buscar evento por ID
3. Buscar evento por nome do cliente
4. Atualizar dados de um evento
5. Relatório financeiro do evento
6. Excluir um evento
7. Listar todos os eventos
0. Sair
```

Digite o número correspondente à operação desejada.

---

# 1️⃣ Cadastrar Evento

Selecione a opção:

```text
1. Cadastrar evento
```

O sistema solicitará:

### Nome do Cliente

Digite apenas letras.

✅ Exemplo:

```text
Maria Silva
```

❌ Não permitido:

```text
Maria123
```

---

### Tipo de Evento

Escolha uma das opções:

```text
1. Casamento
2. Aniversário
3. Confraternização
4. Reunião
5. Formatura
6. Outro
```

Caso escolha "Outro", informe o nome do evento.

---

### Data do Evento

Informe a data no formato:

```text
DD/MM/AAAA
```

Exemplo:

```text
25/12/2026
```

O sistema validará a data informada.

---

### Local do Evento

Digite o local do evento.

Exemplo:

```text
salão imperial
```

Não são permitidos números.

---

### Orçamento Disponível

Informe o valor total disponível para o evento.

Exemplo:

```text
5000
```

---

### Quantidade de Convidados

Informe o número previsto de participantes.

Exemplo:

```text
120
```

---

### Sugestões Personalizadas

Após o cadastro inicial, o sistema exibirá sugestões automáticas com base:

* No tipo de evento
* Na quantidade de convidados

---

### Adição de Serviços

O usuário poderá contratar serviços como:

```text
1. Buffet
2. Banda
3. Iluminação
4. Ornamentação
5. Segurança
6. Doces e Bolos
7. Serviços Gráficos
8. Veículos
9. Make
10. Foto e Filmagem
11. Cerimonial
12. Outros
```

Para cada serviço será solicitado o valor contratado.

O sistema atualizará automaticamente o orçamento restante.

Exemplo:

```text
Digite o valor do serviço 'Buffet': R$ 1500
Orçamento restante: R$ 3500
```

---

### Finalização do Cadastro

Ao finalizar:

```text
0. FINALIZAR
```

O sistema gerará automaticamente um ID único.

Exemplo:

```text
Evento cadastrado com sucesso!
Seu ID é: 54321
```

⚠️ Guarde o ID para futuras consultas.

---

# 2️⃣ Buscar Evento por ID

Selecione:

```text
2. Buscar evento por ID
```

Informe o ID do evento.

Exemplo:

```text
54321
```

O sistema exibirá:

* Nome
* Evento
* Data
* Local
* Orçamento
* Serviços
* Quantidade de convidados
* Dias restantes para o evento

---

# 3️⃣ Buscar Evento por Nome

Selecione:

```text
3. Buscar evento por nome do cliente
```

Digite o nome do cliente.

Exemplo:

```text
Maria
```

Todos os eventos associados serão exibidos.

---

# 4️⃣ Atualizar Evento

Selecione:

```text
4. Atualizar dados de um evento
```

Informe o ID do evento.

O sistema disponibiliza as seguintes opções:

```text
1. Alterar Data
2. Alterar Local
3. Alterar Quantidade de Convidados
4. Adicionar Novo Serviço
5. Editar Valor de Serviço
6. Excluir Serviço
7. Alterar Orçamento Inicial
8. Resetar Todos os Serviços
0. Finalizar Alterações
```

---

## Alterar Data

Permite alterar a data do evento.

---

## Alterar Local

Permite alterar o local do evento.

---

## Alterar Quantidade de Convidados

Atualiza o número de participantes e gera novas sugestões personalizadas.

---

## Adicionar Serviço

Permite incluir novos serviços ao evento.

O orçamento restante será recalculado automaticamente.

---

## Editar Valor de Serviço

Permite corrigir ou atualizar o valor de um serviço já cadastrado.

O orçamento restante será ajustado automaticamente.

---

## Excluir Serviço

Remove um serviço específico.

O valor removido retorna ao orçamento disponível.

---

## Alterar Orçamento Inicial

Permite aumentar ou reduzir o orçamento total do evento.

O saldo restante será recalculado automaticamente.

---

## Resetar Serviços

Remove todos os serviços cadastrados.

O orçamento restante retorna ao valor inicial.

⚠️ Esta ação exige confirmação.

---

# 5️⃣ Gerar Relatório Financeiro

Selecione:

```text
5. Relatório financeiro do evento
```

A busca pode ser feita por:

* ID do evento
* Nome do cliente

O relatório apresenta:

* Dados do evento
* Lista de serviços contratados
* Valor de cada serviço
* Total gasto
* Saldo restante
* Custo estimado por convidado

Exemplo:

```text
RESUMO FINANCEIRO

Orçamento Inicial: R$ 5000,00
Total Gasto:       R$ 1800,00
Saldo Restante:    R$ 3200,00

Custo por Convidado: R$ 15,00
```

---

# 6️⃣ Excluir Evento

Selecione:

```text
6. Excluir um evento
```

Informe o ID do evento.

O sistema solicitará confirmação antes da exclusão.

Exemplo:

```text
Tem certeza que deseja excluir? (S/N)
```

Após confirmação, o evento será removido permanentemente.

---

# 7️⃣ Listar Todos os Eventos

Selecione:

```text
7. Listar todos os eventos
```

O sistema exibirá:

* ID
* Nome do cliente
* Tipo do evento
* Data

---

# 💾 Armazenamento dos Dados

Todas as informações são salvas automaticamente no arquivo:

```text
agenda_salva.txt
```

Os dados são carregados sempre que o sistema é iniciado.

Não é necessário realizar salvamento manual.

---

# ⚠️ Regras e Validações

O sistema possui validações para garantir a integridade dos dados:

* Nome do cliente não pode conter números.
* Nome do evento personalizado não pode conter números.
* Local não pode conter números.
* Data deve estar no formato DD/MM/AAAA.
* Orçamento deve ser maior que zero.
* Quantidade de convidados deve ser maior que zero.
* Valores de serviços devem ser numéricos.

---

# 🛠️ Solução de Problemas

### "ID não encontrado"

Verifique se o número informado está correto.

---

### "Formato de data inválido"

Utilize o padrão:

```text
DD/MM/AAAA
```

---

### "Entrada inválida"

Certifique-se de informar apenas números quando solicitado.

---

# 👨‍💻 Equipe de Desenvolvimento

Projeto desenvolvido para a disciplina de Fundamentos de Programação.

CheckEvent © 2026
