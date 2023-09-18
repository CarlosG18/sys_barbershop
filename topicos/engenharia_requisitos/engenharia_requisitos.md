# Engenharia de Requisitos

Neste arquivo será apresentado os `casos de uso`, `diagrama de casos de uso` e as `histórias de usuários` do sistema de agendamentos dos salões.

## Casos de Uso

**Ator: Cliente**

> **CRIAR CONTA**:

  *fluxo normal*
  1. cliente informa username;
  2. cliente informa email;
  3. cliente informa cpf;
  4. cliente informa senha;

  *extensões*:
  - 3a. se o cpf for invalido, informar um novo;
  
> **AGENDAR**:

  *fluxo normal*
  1. Cliente escolhe uma barbearia/salão;
  2. Cliente clica na função de agendar;
  3. Cliente escolhe os tipos de serviços (tipo do corte, qual cabelereiro(a), etc);
  4. Cliente visualiza o preço total e o tempo estimado para os serviços selecionados;
  5. Cliente escolhe seu horário e confirma;

> **EXCLUIR AGENDAMENTO**

  *fluxo normal*
  1. Cliente poderá ver seus agendamentos ativos;
  2. Cliente poderá excluir agendamentos;

---

**Ator: gerente**

>**ADICIONAR BARBEARIA/SALÂO**

  *fluxo normal*
  1. o gerente informa o cnpj da barbearia/salão;
  2. o gerente informa o nome da barbearia/salão;
  3. o gerente informa o endereço da barbearia/salão;
  4. o gerente informa o horário de funcionamento da barbearia/salão;
  5. <u>__cadastrar barbeiro(a)__</u>

>**CADASTRAR BARBEIRO(A)**

  *fluxo normal*
  1. gerente informa nome do Cabelereiro(a);
  2. gerente informa os horarios do Cabelereiro(a);
  3. gerente informa a clasificação do Cabelereiro(a);
  4. gerente informa os tipos de serviços que o Cabelereiro(a) possui incluindo as estimativas de tempo;

>**ATUALIZAR DADOS**

  *fluxo normal*
  1. gerente atualiza os preços dos serviços;
  2. gerente deleta barbearias/salões;
  3. gerente __adiciona barbearia/salão__;
  4. gerente atualiza informações dos Cabelereiro(a); 

>**OBTER RELATÓRIOS**

  *fluxo normal*
  1. gerente obtem relatório de receita;
  2. estimativa de comparecimento;

---

**Ator: Cabelereiro(a)**

>**CONFIRMAR AGENDAMENTO**

  *fluxo normal*
  1. barbeiro visualiza seu dashboard com a lista de clientes e horarios que foram agendados;
  2. confirmar se o cliente compareceu;
  
  *extensões*:
  - 2.a caso o cliente não comparecer, o Cabelereiro(a) deve registrar no sistema;


## Diagrama de Casos de Uso

## Histórias de Usuário (US)
