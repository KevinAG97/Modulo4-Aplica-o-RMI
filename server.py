import Pyro5.api
import Pyro5.server
import threading

CONTA_URI = "conta.bancaria"

@Pyro5.api.expose
@Pyro5.api.behavior(instance_mode="single")
class ContaBancaria:
    """Objeto remoto que representa uma conta bancária compartilhada."""

    def __init__(self):
        self._saldo = 0.0
        self._lock = threading.Lock()

    def depositar(self, valor: float) -> str:
        if valor <= 0:
            return f"Erro: valor de depósito deve ser positivo (recebido: {valor})"
        with self._lock:
            self._saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self._saldo:.2f}"

    def retirar(self, valor: float) -> str:
        if valor <= 0:
            return f"Erro: valor de retirada deve ser positivo (recebido: {valor})"
        with self._lock:
            if valor > self._saldo:
                return f"Erro: saldo insuficiente. Saldo atual: R$ {self._saldo:.2f}, tentativa de retirada: R$ {valor:.2f}"
            self._saldo -= valor
            return f"Retirada de R$ {valor:.2f} realizada. Saldo atual: R$ {self._saldo:.2f}"

    def saldo(self) -> str:
        with self._lock:
            return f"Saldo atual: R$ {self._saldo:.2f}"


def main():
    # Inicia o servidor de nomes do Pyro5 embutido (equivalente ao rmiregistry do Java)
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.api.locate_ns()

    uri = daemon.register(ContaBancaria)
    ns.register(CONTA_URI, uri)

    print(f"Servidor RMI iniciado.")
    print(f"Objeto remoto registrado como '{CONTA_URI}' -> {uri}")
    print("Aguardando conexões de clientes... (Ctrl+C para encerrar)\n")
    daemon.requestLoop()


if __name__ == "__main__":
    main()
