========================================================
  Desafio M3 - Sistemas Distribuídos
  Aplicação RMI com Conta Bancária em Python (Pyro5)
========================================================

DESCRIÇÃO
---------
Esta aplicação implementa o padrão RMI (Remote Method Invocation) utilizando
a biblioteca Pyro5 para Python. Um objeto remoto representa uma Conta Bancária
compartilhada, e múltiplos clientes podem acessá-lo simultaneamente.

O objeto remoto implementa os métodos:
  - depositar(valor)  : adiciona valor ao saldo da conta
  - retirar(valor)    : subtrai valor do saldo (verifica saldo suficiente)
  - saldo()           : retorna o saldo atual da conta

O acesso concorrente é protegido por lock (threading.Lock), garantindo
consistência mesmo com vários clientes operando ao mesmo tempo.

ARQUIVOS
--------
  server.py  - Servidor RMI com o objeto remoto ContaBancaria
  client.py  - Cliente interativo que acessa a conta remotamente
  readme.txt - Este arquivo

REQUISITOS
----------
  - Python 3.8 ou superior
  - Biblioteca Pyro5

INSTALAÇÃO DAS DEPENDÊNCIAS
----------------------------
Execute o comando abaixo para instalar a biblioteca Pyro5:

    pip install Pyro5

COMO EXECUTAR
-------------
Abra TRÊS terminais separados e execute na ordem abaixo:

  TERMINAL 1 - Servidor de Nomes (equivalente ao rmiregistry do Java):
    python -m Pyro5.nameserver

  TERMINAL 2 - Servidor com o objeto remoto:
    python server.py

  TERMINAL 3 (ou mais) - Um ou mais clientes:
    python client.py Cliente1
    python client.py Cliente2   (em outro terminal, simultaneamente)

  O argumento após client.py é opcional e serve como identificador do cliente.
  Se omitido, usará "Cliente" como padrão.

EXEMPLO DE SESSÃO DO CLIENTE
------------------------------
  ===== Banco RMI =====
  1. Depositar
  2. Retirar
  3. Consultar saldo
  4. Sair
  =====================
  Escolha uma opção: 1
  Valor para depositar: R$ 500
  [Cliente1] Depósito de R$ 500.00 realizado. Saldo atual: R$ 500.00

OBSERVAÇÕES
-----------
  - O servidor de nomes deve ser iniciado ANTES do server.py.
  - O server.py deve ser iniciado ANTES dos clientes.
  - Todos os clientes compartilham a mesma instância do objeto remoto
    (instance_mode="single"), simulando uma conta bancária compartilhada.
  - Para testar concorrência, abra múltiplos terminais com client.py rodando
    ao mesmo tempo e observe que o saldo é consistente entre eles.
