# Engenharia de Requisitos

Neste arquivo serão apresentados os`diagrama de casos de uso`, `casos de uso` e as `histórias de usuários` do sistema de agendamentos dos salões.

## Diagrama de Casos de Uso

![Diagrama de casos de uso](https://github.com/CarlosG18/sys_barbershop/blob/diagram_us_casos/topicos/engenharia_requisitos/imagens/diagrama_casos_de_uso.jpeg)

## Casos de Uso

**Ator: Cliente**

> **AUTENTICAÇÂO**:

  *fluxo normal*
  1. O usuário acessa a página de login do sistema.
  2. O sistema exibe os campos de entrada para o nome de usuário e senha.
  3. O usuário insere suas credenciais (nome de usuário e senha) nos campos correspondentes.
  4. O usuário clica no botão de "Login" para submeter as informações.
  5. O sistema verifica as credenciais fornecidas pelo usuário.
  6. Se as credenciais são válidas, o sistema autentica o usuário e redireciona para a página inicial personalizada.
  7. Se as credenciais são inválidas, o sistema exibe uma mensagem de erro indicando que a autenticação falhou.

> **CRIAR CONTA**:

  *fluxo normal*
  1. cliente acessa a página de criação de conta para clientes.
  2. cliente informa username;
  3. cliente informa email;
  4. cliente informa cpf;
  5. cliente informa senha;

  *extensões*:
  - 3a. se o cpf for invalido, informar um novo;
  - 2a. informar se o username colocado já está em uso;
  - 5a. se a senha informada não estiver no formato correto (conter um caractere, uma letra em maiusculo e um número), informar novamente a senha.
  
> **AGENDAR**:

  *fluxo normal*
  1. Cliente clica na função de agendar;
  2. Cliente escolhe os tipos de serviços;
  3. Cliente escolhe o barbeiro de sua preferência.
  3. Cliente visualiza o preço total e o tempo estimado para os serviços selecionados;
  4. Cliente escolhe seu horário e confirma;

> **EXCLUIR AGENDAMENTO**

  *fluxo normal*
  1. Cliente poderá ver seus agendamentos ativos;
  2. Cliente poderá excluir agendamentos;

---

**Ator: gerente**

> **AUTENTICAÇÂO**:

  *fluxo normal*
  1. O usuário acessa a página de login do sistema.
  2. O sistema exibe os campos de entrada para o nome de usuário e senha.
  3. O usuário insere suas credenciais (nome de usuário e senha) nos campos correspondentes.
  4. O usuário clica no botão de "Login" para submeter as informações.
  5. O sistema verifica as credenciais fornecidas pelo usuário.
  6. Se as credenciais são válidas, o sistema autentica o usuário e redireciona para a página inicial personalizada.
  7. Se as credenciais são inválidas, o sistema exibe uma mensagem de erro indicando que a autenticação falhou.

>**CADASTRAR bARBEIRO**

  *fluxo normal*
  1. O gerente acessa o painel de administração do sistema.
  2. O gerente acessa a seção de barbeiros;
  3. O gerente clica na funcionalidade de adicionar um novo barbeiro;
  4. gerente informa nome do barbeiro;
  5. O gerente informa o cpf do barbeiro;
  6. O gerente informa os horarios do barbeiro;
  7. O gerente informa a clasificação do barbeiro;
  8. O gerente informa os tipos de serviços que o barbeiro possui incluindo as estimativas de tempo;
  9. O gerente confirma cadastramento do barbeiro.
  10. __ENVIAR CREDÊNCIAIS__

>**GERENCIAR BARBEARIA/SALÃO**

  *fluxo normal*
  1. O gerente acessa o painel de administração do sistema.
  2. O gerente realiza as alterações desejadas, como atualização de horários de funcionamento, preços de serviços ou informações de contato.
  3. O sistema solicita confirmação antes de efetuar a edição dos dados.

>**GERENCIAR BARBEIRO**

  *fluxo normal*
  1. O gerente acessa o painel de administração do sistema.
  2. O gerente acessa a seção de barbeiro;
  3. O gerente poderá <u>__Cadastrar barbeiro__</u>
  4. O gerente seleciona o barbeiro.
  5. O gerente modifica dados do barbeiro.
  6. O gerente poderá excluir barbeiro.
  7. O sistema solicita confirmação antes de efetuar a edição dos dados.

>**OBTER RELATÓRIOS**

  *fluxo normal*
  1. O gerente acessa o painel de administração do sistema.
  2. O gerente seleciona a seção de relatórios.
  3. O gerente poderá obter relatório de receita e taxa de comparecimento.

---

**Ator: barbeiro**

> **AUTENTICAÇÂO**:

  *fluxo normal*
  1. O usuário acessa a página de login do sistema.
  2. O sistema exibe os campos de entrada para o nome de usuário e senha.
  3. O usuário insere suas credenciais (nome de usuário e senha) nos campos correspondentes.
  4. O usuário clica no botão de "Login" para submeter as informações.
  5. O sistema verifica as credenciais fornecidas pelo usuário.
  6. Se as credenciais são válidas, o sistema autentica o usuário e redireciona para a página inicial personalizada.
  7. Se as credenciais são inválidas, o sistema exibe uma mensagem de erro indicando que a autenticação falhou.

  *extensões*:
  6. caso o cpf do barbeiro não estiver cadastrado no sistema ele não conseguirá realizar o login.

>**CONFIRMAR PRESENÇA**

  *fluxo normal*
  1. barbeiro visualiza seu dashboard com a lista de clientes e horarios que foram agendados;
  2. confirmar se o cliente compareceu;
  
  *extensões*:
  - 2.a caso o cliente não comparecer, o barbeiro deve registrar no sistema;

---

**Ator: Sistema**

>**NOTIFICAR CLIENTE**

  *fluxo normal*
  1. O sistema verifica periodicamente os agendamentos ativos.
  2. O sistema calcula o tempo restante até o horário agendado para cada cliente.
  3. Caso o tempo restante for igual a 30 minutos o sistema envia uma notificação push para o dispositivo do cliente através de um email ou mensagem no whatsapp.

>**ENVIAR CREDÊNCIAIS**

  *fluxo normal*
  1. O sistema gerará um username com base no nome do barbeiro.
  2. O sistema gerará uma senha aleatória.
  3. a tupla de username e senha será enviado para o email do barbeiro.
  

## Histórias de Usuário (US)

> cliente
```txt

- AGENDAR HORÁRIO:
  "Como cliente, gostaria de fazer um agendamento, escolhendo a data, horário, serviço e o barbeiro"
- Critério de aceitação: 
1. O cliente deve ter a opção de escolher a data em que deseja agendar o horário.
2. Deve ser possível selecionar um horário disponível no dia escolhido pelo cliente.
3. O cliente deve poder escolher o serviço que deseja agendar, com uma lista clara e descritiva.
4. O cliente deve ter a opção de selecionar o barbeiro de sua preferência.
5. Após a seleção da data, horário, serviço e barbeiro, o sistema deve confirmar o agendamento e exibir uma confirmação clara para o cliente.
6. Caso o horário escolhido não esteja disponível, o sistema deve informar ao cliente e oferecer opções alternativas.


- VISUALIZAR AGENDAMENTOS
"Como cliente, gostaria de visualizar meus agendamentos ativos e passados"
- Critério de aceitação: 
1. O cliente deve ter a opção de acessar uma seção específica para visualizar seus agendamentos.
2. A lista de agendamentos deve exibir os agendamentos ativos e passados separadamente, com indicações claras sobre o status de cada um.
3. Para cada agendamento ativo, o cliente deve poder ver a data, horário, serviço, cabeleireiro e qualquer outra informação relevante.
4. Para cada agendamento passado, o cliente deve poder visualizar o histórico completo do serviço prestado, incluindo data, horário, serviço e barbeiro.


- EXCLUIR AGENDAMENTO
"Como cliente, gostaria de poder excluir a qualquer momento meus agendamentos"
- Critério de aceitação: 
1. O cliente deve ter a opção de acessar uma seção específica para gerenciar seus agendamentos.
2. Para cada agendamento listado, deve haver uma opção clara e visível para excluí-lo.
3. Ao selecionar a opção de exclusão, o sistema deve solicitar uma confirmação do cliente antes de efetuar a exclusão.
4. Após a confirmação, o agendamento selecionado deve ser removido da lista de agendamentos do cliente.
5. O sistema deve fornecer um feedback claro para o cliente indicando que o agendamento foi excluído com sucesso.

```

> Gerente
```txt  
  - OBTER RELATÓRIOS
  "Como gerente, gostaria de poder obter um relatório de dados com vendas e servicos ofertados em periodos específicos de funcionamento de cada barbearia/salão"
  - Critério de aceitação: 
  1. O gerente deve ter a opção de selecionar um período específico (como uma data de início e uma data de fim) para o relatório.
  2. O sistema deve gerar um relatório que inclua informações sobre as vendas realizadas durante o período selecionado, com detalhes como valor total, número de transações e serviços mais populares.
  3. O relatório deve incluir uma lista dos serviços oferecidos em cada barbearia/salão durante o período selecionado, juntamente com a quantidade de vezes que cada serviço foi solicitado.
  4. O relatório deve exibir as informações de forma clara e organizada, facilitando a análise por parte do gerente.
  5. O sistema deve fornecer a opção de exportar o relatório em formatos comuns, como PDF ou planilha Excel, para que o gerente possa compartilhar ou arquivar os dados.
  6. Caso o período selecionado não tenha dados disponíveis, o sistema deve informar ao gerente de forma clara.

  
  - EDITAR DADOS DA BARBEARIA/SALÃO
  "Como Gerente, gostaria de editar os preços dos serviços ofertados pela mimha/meu barbearia/salão, além de excluir barbeiro existentes e adicionar novos"
  - Critério de aceitação: 
  1. O sistema deve fornecer uma funcionalidade para o gerente editar ou atualizar as informações da barbearia/salão.

  - EDITAR DADOS DOS CABELEREIROS(AS)
  "Como gerente, gostaria de atualizar dados dos barbeiros da minha barbearia/salão"
  - Critérios de aceitação:
  1. O gerente deve ter acesso ao painel de administração do sistema.
  2. O sistema deve exibir uma lista dos barbeiro associados à barbearia/salão.
  3. O gerente deve ser capaz de selecionar um barbeiro da lista para editar.
  4. O sistema deve apresentar os dados do barbeiro selecionado em um formulário editável.
  5. O gerente pode realizar as alterações desejadas nos dados do barbeiro.
  6. O sistema deve fornecer uma opção para salvar as alterações feitas nos dados do barbeiro.
  7. Após salvar as alterações, o sistema deve exibir uma confirmação de que os dados foram atualizados com sucesso.
  
```

> Barbeiro
```txt

  - VISUALIZAR LISTA DE CLIENTES
  "Como barbeiro, gostaria de ver a lista de horários dos clientes do dia atual, bem como os serviços que o cliente irá realizar";
  - Critério de aceitação: 
  1. Ao abrir a aplicação, o barbeiro deve ter a opção clara e visível para visualizar a lista de clientes do dia atual.
  2. A lista de clientes deve exibir o nome de cada cliente agendado para o dia, juntamente com o horário do agendamento.
  3. Ao selecionar um cliente na lista, o aplicativo deve exibir os detalhes do serviço(s) que o cliente irá realizar, como por exemplo, o tipo de corte ou tratamento.
  4. A lista e os detalhes do serviço devem ser atualizados em tempo real, refletindo quaisquer alterações feitas pelo cliente ou pela equipe.
  
```

