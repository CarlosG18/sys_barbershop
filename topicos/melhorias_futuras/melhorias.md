# Próximas melhorias do sistema

vou descrever aqui algumas features que o sistema poderá receber futuramente.

## Segurança:
- tela de cadastro:
    - aplicar um regex para o email.
    - aplicar um regex para a senha possuir um nível bom de segurança;

- tela de agendamento:
    - aplicar restrições de horario para o agendamento de acordo com o funcionamento do estabelecimento;
    - aplicar logicas de preço;
    - aplicar logicas de verificação do tempo de servço;
    - aplicar verificação na consistência dos dados inseridos pelo usuario, como hora e data.

## Interatividade:

- tela de login:
    - Na tela de login, ao informar a senha ou o username incorreto aparecer um box avisando que os dados foram incorretos;

- tela de cadastro (cliente/gerente):
    - Quando o usuário inserir o username, o sistema verifica se o username colocado já está em uso e deverá mostrar isso ao usuário e sugerir outros usernames.
    - mostrar como deveriam ser os inputs que o usuário deverá colocar.
    - No cpf, o usuário deverá colocar apenas o número, e o sistema adequar automaticamente ao formato padrão do cpf.
    - Na senha, a página deverá informar claramente o que a senha deve conter e além disso criar uma barra que informa o quanto a senha é segura.

- tela de agendamento (cliente):
    - melhorar a forma como o cliente preenche os inputs de agendamento, principalmente o de escolher o horario;
    - aplicar a seleção de o cliente pode escolher varios serviços;
    - mostrar ao cliente o preço total dos serviços escolhidos no agendamento;
    - ao clicar no botão de agendar, aparecer uma tela de confirmação.

## Visual:

- Criar uma página principal, que contém os aspectos centrais da aplicação, juntamente com um link para a área de login;
- alterar a identidade visual do site: pesquisar algumas fontes específicas de salão, e cores que remetem.
- melhorar como os serviçovenvs são apresentados para o cliente/gerente;
- melhorar a view principal do cliente;
- melhorar a view de agendamentos do cliente;
- melhorar a forma de mostrar os horarios já agendados.

## sistema:

- Implementar a view de detalhes do cabelereiro para o cliente e para o gerente;
- Implementar (gerente) a função de deletar barbeiros;
- Implementar (gerente) a função de editar barbeiros;
- Implementar (gerente) a função de deletar serviços;
- Implementar (gerente) a função de editar serviços;
- Implementar a tela de relatorios;
- Implementar a view de perfil do cliente, com a função de adicionar a foto de perfil e editar dados;
- Implementar a questão do tempo de serviço;