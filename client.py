import Pyro5.api
import sys

CONTA_URI = "conta.bancaria"


def menu():
    print("\n===== Banco RMI =====")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Sair")
    print("=====================")
    return input("Escolha uma opção: ").strip()


def obter_valor(prompt: str) -> float:
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número.")


def main():
    cliente_id = sys.argv[1] if len(sys.argv) > 1 else "Cliente"

    print(f"\n[{cliente_id}] Conectando ao servidor RMI...")
    try:
        ns = Pyro5.api.locate_ns()
        uri = ns.lookup(CONTA_URI)
        conta = Pyro5.api.Proxy(uri)
        print(f"[{cliente_id}] Conectado com sucesso!\n")
    except Exception as e:
        print(f"[{cliente_id}] Erro ao conectar: {e}")
        print("Verifique se o servidor de nomes (nameserver) e o server.py estão rodando.")
        sys.exit(1)

    while True:
        opcao = menu()

        if opcao == "1":
            valor = obter_valor("Valor para depositar: R$ ")
            resposta = conta.depositar(valor)
            print(f"[{cliente_id}] {resposta}")

        elif opcao == "2":
            valor = obter_valor("Valor para retirar: R$ ")
            resposta = conta.retirar(valor)
            print(f"[{cliente_id}] {resposta}")

        elif opcao == "3":
            resposta = conta.saldo()
            print(f"[{cliente_id}] {resposta}")

        elif opcao == "4":
            print(f"[{cliente_id}] Encerrando conexão.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
