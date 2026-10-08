```python
# ============================================================================
# TRABALHO: Criptografia e Comunicação Segura
# ALGORITMO: Cifra de César - Substituição por Deslocamento
#
# REFERÊNCIA:
# STALLINGS, William. Criptografia e segurança de redes:
# princípios e práticas. 6. ed. São Paulo: Pearson, 2015.
# Capítulo 2, Seções 2.1 e 2.2.
# ============================================================================

"""
DESCRIÇÃO

Este programa implementa a Cifra de César, um algoritmo clássico
de criptografia por substituição.

A técnica consiste em substituir cada letra da mensagem por outra
letra localizada a uma determinada quantidade de posições no alfabeto.

Exemplo com chave 3:

    A -> D
    B -> E
    C -> F
    ...
    X -> A
    Y -> B
    Z -> C

A implementação utiliza aritmética modular com módulo 26 para
permitir que o deslocamento continue corretamente após a letra Z.

Características:
- Criptografia;
- Descriptografia;
- Preservação de maiúsculas e minúsculas;
- Preservação de espaços e pontuação;
- Aceitação de chaves positivas, zero e negativas;
- Testes automatizados;
- Demonstração do funcionamento;
- Menu interativo;
- Tratamento de entradas inválidas.
"""


# ============================================================================
# CONSTANTES
# ============================================================================

ALFABETO_MAIUSCULO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFABETO_MINUSCULO = "abcdefghijklmnopqrstuvwxyz"
TAMANHO_ALFABETO = 26


# ============================================================================
# 1. FUNÇÃO DE CRIPTOGRAFIA
# ============================================================================

def cifrar(texto, chave):
    """
    Criptografa uma mensagem utilizando a Cifra de César.

    Parâmetros:
        texto (str): mensagem original.
        chave (int): quantidade de posições do deslocamento.

    Retorno:
        str: mensagem criptografada.
    """

    resultado = ""

    # Garante que a chave esteja entre 0 e 25
    chave = chave % TAMANHO_ALFABETO

    for caractere in texto:

        # ------------------------------------------------------------
        # Letras maiúsculas
        # ------------------------------------------------------------
        if caractere in ALFABETO_MAIUSCULO:

            posicao = ALFABETO_MAIUSCULO.index(caractere)

            nova_posicao = (
                posicao + chave
            ) % TAMANHO_ALFABETO

            resultado += ALFABETO_MAIUSCULO[nova_posicao]

        # ------------------------------------------------------------
        # Letras minúsculas
        # ------------------------------------------------------------
        elif caractere in ALFABETO_MINUSCULO:

            posicao = ALFABETO_MINUSCULO.index(caractere)

            nova_posicao = (
                posicao + chave
            ) % TAMANHO_ALFABETO

            resultado += ALFABETO_MINUSCULO[nova_posicao]

        # ------------------------------------------------------------
        # Espaços, números e símbolos
        # ------------------------------------------------------------
        else:
            resultado += caractere

    return resultado


# ============================================================================
# 2. FUNÇÃO DE DESCRIPTOGRAFIA
# ============================================================================

def decifrar(texto, chave):
    """
    Descriptografa uma mensagem utilizando a Cifra de César.

    A descriptografia utiliza o deslocamento inverso da criptografia.
    """

    return cifrar(texto, -chave)


# ============================================================================
# 3. FUNÇÃO DE DEMONSTRAÇÃO
# ============================================================================

def demonstrar_cifra(texto, chave):
    """
    Demonstra visualmente como cada letra é deslocada.
    """

    print("\n" + "=" * 70)
    print("DEMONSTRAÇÃO DA CIFRA DE CÉSAR")
    print("=" * 70)

    print(f"\nMensagem original: {texto}")
    print(f"Chave utilizada:   {chave}")

    print("\nProcessamento dos caracteres:")

    for caractere in texto:

        if caractere in ALFABETO_MAIUSCULO:

            posicao = ALFABETO_MAIUSCULO.index(caractere)
            nova_posicao = (
                posicao + chave
            ) % TAMANHO_ALFABETO

            novo_caractere = ALFABETO_MAIUSCULO[nova_posicao]

            print(
                f"  {caractere} -> {novo_caractere}"
            )

        elif caractere in ALFABETO_MINUSCULO:

            posicao = ALFABETO_MINUSCULO.index(caractere)
            nova_posicao = (
                posicao + chave
            ) % TAMANHO_ALFABETO

            novo_caractere = ALFABETO_MINUSCULO[nova_posicao]

            print(
                f"  {caractere} -> {novo_caractere}"
            )

        else:

            print(
                f"  {caractere} -> {caractere} "
                "(mantido)"
            )

    print("\nResultado:")
    print(cifrar(texto, chave))


# ============================================================================
# 4. TESTES AUTOMATIZADOS
# ============================================================================

def executar_testes():
    """
    Executa testes para verificar o funcionamento da criptografia
    e da descriptografia.
    """

    print("\n" + "=" * 70)
    print("TESTES AUTOMATIZADOS")
    print("=" * 70)

    testes = [
        ("ATACAR BASE SUL", 3),
        ("Criptografia e Seguranca", 5),
        ("Hello World 123!", 10),
        ("XYZ", 3),
        ("ABC", 26),
        ("Teste", 0),
        ("Mensagem secreta", -3),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 13),
        ("abcdefghijklmnopqrstuvwxyz", 7)
    ]

    total = len(testes)
    sucessos = 0

    for numero, (texto_original, chave) in enumerate(
        testes,
        start=1
    ):

        texto_cifrado = cifrar(
            texto_original,
            chave
        )

        texto_decifrado = decifrar(
            texto_cifrado,
            chave
        )

        resultado = (
            texto_original == texto_decifrado
        )

        print(f"\nTeste {numero}")
        print("-" * 40)
        print(f"Original:    {texto_original}")
        print(f"Chave:       {chave}")
        print(f"Cifrado:     {texto_cifrado}")
        print(f"Decifrado:   {texto_decifrado}")

        if resultado:

            print("Status:      APROVADO")
            sucessos += 1

        else:

            print("Status:      REPROVADO")

    print("\n" + "=" * 70)

    if sucessos == total:

        print(
            f"RESULTADO FINAL: {sucessos}/{total} TESTES APROVADOS"
        )

        print(
            "Todos os testes foram executados com sucesso."
        )

    else:

        print(
            f"RESULTADO FINAL: {sucessos}/{total} TESTES APROVADOS"
        )

        print(
            "Atenção: alguns testes apresentaram falha."
        )

    print("=" * 70)


# ============================================================================
# 5. FUNÇÃO PARA LEITURA DA CHAVE
# ============================================================================

def ler_chave():
    """
    Solicita ao usuário uma chave inteira.

    Continua solicitando até receber uma entrada válida.
    """

    while True:

        entrada = input(
            "Digite a chave de deslocamento: "
        ).strip()

        try:

            return int(entrada)

        except ValueError:

            print(
                "\nERRO: a chave deve ser um número inteiro."
            )

            print(
                "Exemplos válidos: 3, 5, 10, 26 ou -3.\n"
            )


# ============================================================================
# 6. FUNÇÃO PARA PAUSAR A EXECUÇÃO
# ============================================================================

def pausar():
    """
    Aguarda o usuário antes de retornar ao menu.
    """

    input(
        "\nPressione ENTER para continuar..."
    )


# ============================================================================
# 7. MENU PRINCIPAL
# ============================================================================

def menu_interativo():
    """
    Exibe o menu principal do programa.
    """

    while True:

        print("\n")
        print("=" * 70)
        print("                 CIFRA DE CÉSAR")
        print("          CRIPTOGRAFIA E COMUNICAÇÃO SEGURA")
        print("=" * 70)

        print("\n1 - Criptografar mensagem")
        print("2 - Descriptografar mensagem")
        print("3 - Demonstrar funcionamento da cifra")
        print("4 - Executar testes automatizados")
        print("5 - Exibir informações do algoritmo")
        print("6 - Sair")

        print("=" * 70)

        opcao = input(
            "Escolha uma opção (1-6): "
        ).strip()

        # ================================================================
        # OPÇÃO 1 - CRIPTOGRAFAR
        # ================================================================

        if opcao == "1":

            print("\n" + "-" * 70)
            print("CRIPTOGRAFAR MENSAGEM")
            print("-" * 70)

            mensagem = input(
                "Digite a mensagem: "
            )

            chave = ler_chave()

            resultado = cifrar(
                mensagem,
                chave
            )

            print("\nMensagem original:")
            print(mensagem)

            print("\nMensagem criptografada:")
            print(resultado)

            pausar()

        # ================================================================
        # OPÇÃO 2 - DESCRIPTOGRAFAR
        # ================================================================

        elif opcao == "2":

            print("\n" + "-" * 70)
            print("DESCRIPTOGRAFAR MENSAGEM")
            print("-" * 70)

            mensagem = input(
                "Digite a mensagem criptografada: "
            )

            chave = ler_chave()

            resultado = decifrar(
                mensagem,
                chave
            )

            print("\nMensagem criptografada:")
            print(mensagem)

            print("\nMensagem descriptografada:")
            print(resultado)

            pausar()

        # ================================================================
        # OPÇÃO 3 - DEMONSTRAÇÃO
        # ================================================================

        elif opcao == "3":

            print("\n" + "-" * 70)
            print("DEMONSTRAÇÃO DA CIFRA")
            print("-" * 70)

            mensagem = input(
                "Digite uma mensagem: "
            )

            chave = ler_chave()

            demonstrar_cifra(
                mensagem,
                chave
            )

            pausar()

        # ================================================================
        # OPÇÃO 4 - TESTES
        # ================================================================

        elif opcao == "4":

            executar_testes()

            pausar()

        # ================================================================
        # OPÇÃO 5 - INFORMAÇÕES
        # ================================================================

        elif opcao == "5":

            print("\n" + "=" * 70)
            print("INFORMAÇÕES SOBRE A CIFRA DE CÉSAR")
            print("=" * 70)

            print(
                "\nA Cifra de César é um método clássico de "
                "substituição."
            )

            print(
                "\nCada letra é deslocada uma quantidade fixa "
                "de posições no alfabeto."
            )

            print(
                "\nA implementação utiliza aritmética modular "
                "com módulo 26."
            )

            print(
                "\nExemplo com chave 3:"
            )

            print(
                "A -> D"
            )

            print(
                "B -> E"
            )

            print(
                "C -> F"
            )

            print(
                "X -> A"
            )

            print(
                "Y -> B"
            )

            print(
                "Z -> C"
            )

            print(
                "\nEspaços, números e sinais de pontuação "
                "não são modificados."
            )

            print(
                "\nReferência:"
            )

            print(
                "STALLINGS, William. Criptografia e segurança "
                "de redes: princípios e práticas. "
                "6. ed. São Paulo: Pearson, 2015."
            )

            pausar()

        # ================================================================
        # OPÇÃO 6 - SAIR
        # ================================================================

        elif opcao == "6":

            print("\n" + "=" * 70)
            print("PROGRAMA ENCERRADO")
            print("=" * 70)

            print(
                "Obrigado por utilizar o programa."
            )

            break

        # ================================================================
        # OPÇÃO INVÁLIDA
        # ================================================================

        else:

            print("\nERRO: opção inválida.")

            print(
                "Digite um número entre 1 e 6."
            )


# ============================================================================
# 8. EXECUÇÃO PRINCIPAL
# ============================================================================

if __name__ == "__main__":

    print("\n")
    print("=" * 70)
    print("       TRABALHO DE CRIPTOGRAFIA E COMUNICAÇÃO SEGURA")
    print("=" * 70)
    print("                    CIFRA DE CÉSAR")
    print("=" * 70)

    print(
        "\nIniciando testes automáticos..."
    )

    executar_testes()

    print(
        "\nOs testes foram concluídos."
    )

    print(
        "O sistema está pronto para utilização."
    )

    menu_interativo()
```