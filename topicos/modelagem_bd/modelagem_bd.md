# Modelagem do Banco de Dados

## Modelo Entidade-Relacionamento(MER)

[imagem do modelo entidade relacionamento](https://github.com/CarlosG18/sys_barbershop/blob/modelagem_bd/topicos/modelagem_bd/imagens/modelagem_bd.md)

```mermaid
---
title: Modelagem Banco de Dados do sistema de agendamentos (barbearia)
---
flowchart LR
    Usuario
    email([email])
    cpf([_cpf_])
    username([username])
    senha([senha])
    overlap([o])

    Usuario --- email
    Usuario --- cpf
    Usuario --- username
    Usuario --- senha

    Barbeiro
    Cliente
    Gerente
    
    Agendamento
    id([_id_])
    servico([serviço])
    preco([preço])
    horario([horário])

    Agendamento ---id
    Agendamento --- servico
    Agendamento --- preco
    Agendamento --- horario

    style Usuario fill:#B0C4DE,stroke:#000,stroke-width:1px
    style Gerente fill:#ADD8E6,stroke:#000,stroke-width:1px
    style Barbeiro fill:#ADD8E6,stroke:#000,stroke-width:1px
    style Cliente fill:#ADD8E6,stroke:#000,stroke-width:1px
    style Gerente fill:#ADD8E6,stroke:#000,stroke-width:1px
    style Agendamento fill:#FFDEAD,stroke:#000,stroke-width:1px
    
    especializacao([d])
    Usuario --- especializacao
    especializacao --- Gerente

    especializacao --- overlap
    overlap --- Barbeiro
    overlap --- Cliente
    
    relacionamento1{participa}
    relacionamento2{gerencia}
    relacionamento3{gerencia}

    Cliente --- relacionamento1
    relacionamento1 --- Agendamento

    Barbeiro --- relacionamento1

    Gerente --- relacionamento2 
    relacionamento2 --- Barbeiro

    Gerente --- relacionamento3
    relacionamento3 --- Agendamento
```
### cardinalidade
- Cliente (N) --> PARTICIPA --> (N) Agendamento
- Barbeiro (1) --> PARTICIPA --> (N) Agendamento
- Gerente (1) -->  GERÊNCIA --> (N) Barbeiro
- Gerente (1) -->  GERÊNCIA --> (N) Agendamento

## Modelo Relacional
```mermaid
erDiagram
    
    Usuario {
        string email
        string __cpf__ PK
        string username
        string senha
    }
    
    Agendamento {
        int __id__ PK
        string servico
        float preco
        date horario
        string cpf_gerente__ FK
    }

    Barbeiro {
        string __cpf_b__ FK
        string cpf_gerente__ FK
    }

    Cliente {
        string __cpf_c__ FK
    }

    Gerente {
        string __cpf_g__ FK
    }

    Cliente_Agendamento{
        string cpf_barbeiro FK
        string __cpf_cliente__ FK 
        string __id_agendamento__ FK  
    }
```
### referências das chaves estrangeiras (FK):
- cpf_b(Barbeiro) referência cpf(Usuário);
- cpf_c(Cliente) referência cpf(Usuário);
- cpf_g(Gerente) referência cpf(Usuário);
- cpf_barbeiro(Cliente_Agendamento) referência cpf_b(Barbeiro);
- cpf_cliente(Cliente_Agendamento) referência cpf_c(Cliente);
- id_agendamento(Cliente_Agendamento) referência id(Agendamento);
- cpf_gerente(Agendamento) referência cpf_g(Gerente);
- cpf_gerente(Barbeiro) referência cpf_g(Gerente);
