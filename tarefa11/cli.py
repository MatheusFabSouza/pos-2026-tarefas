import users_wrapper as usuario

opcao = True

while opcao:
    opcao = input("1 - Lista dos usuarios\n 2 - Ler usuario\n 3 - Editar usuario\n 4 - Excluir usuario\n 5 - Criar usuario\n 6 - Sair\n Digite a funcao desejada:")

    if opcao == "1":
        users = usuario.listar_usuarios()
        if users:
            print("\nLista de usuarios:")
            for user in users:
                print(f"ID: {user['id']} Nome: {user['name']}")
        else:
            print("Nenhum usuario encontrado.")

    if opcao == "2":
        user_id = input("Digite o ID do usuario:")
        user = usuario.read_usuario(user_id)
        if user:
            print(f"Nome:{user['name']}")
            print(f"Email:{user['email']}")
            print(f"Telefone:{user['phone']}")
        else:
            print("Usuario nao encontrado.")

    if opcao == "3":
        user_id = input("Digite o ID do usuario:")
        user = usuario.read_usuario(user_id)
        if user:
            user["name"] = input("Novo nome:")
            user["email"] = input("Novo email:")
            user["phone"] = input("Novo telefone:")

            novo_usuario = usuario.update_usuario(user_id, user)
            if novo_usuario:
                print(f"Usuario {novo_usuario['name']} atualizado.")
            else:
                print("Erro ao atualizar o usuario.")
        else:
            print("Usuario nao encontrado.")

    if opcao == "4":
        user_id = input("Digite o ID do usuario:")
        user = usuario.read_usuario(user_id)
        if user:
            confirmacao = input("Deseja excluir este usuario? s ou n pra confirmar:")
            if confirmacao == "s":
                if usuario.deletar_usuario(user_id):
                    print("Usuario deletado.")
                else:
                    print("Erro ao excluir usuario.")
            else:
                print("Exclusao cancelada.")
        else:
            print("Usuario não encontrado.")

    if opcao == "5":
        user = {}
        user["name"] = input("Nome:")
        user["email"] = input("Email:")
        user["phone"] = input("Telefone:")

        confirmacao = input("Deseja criar este usuario? s ou n pra confirmar:")
        if confirmacao == "s":
            novo_usuario = usuario.criar_usuario(user)
            if novo_usuario:
                print(f"Usuario {novo_usuario['name']} criado.")
            else:
                print("Erro ao criar usuario.")
        else:
            print("Operacao cancelada.")

    if opcao == "6":
        print("Valeu ata nunca mais")
        opcao = False

    else:
        print("Opcao invalida.")

    if opcao == "7":
         print("Removendo System32...")

    