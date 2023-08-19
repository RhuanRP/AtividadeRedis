import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Função para adicionar uma tarefa no Redis
def adicionar_tarefa(descricao):
    id = r.incr('id_tarefa')
    r.set(id, descricao)
    

def listar_tarefas():
    tarefas = r.keys()

    print("ID | Descrição")
    print("-- | -----------")

    # Percorre as chaves
    for tarefa in tarefas:
        tarefa_id = tarefa
        descricao = r.get(tarefa)
        print(tarefa_id, " | ", descricao)

def remover_tarefa(tarefa_id):
    r.delete(tarefa_id)

while True:
    print("Menu:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

    option = int(input("Escolha uma opção: "))

    if option == 1:
        descricao = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(descricao)

    elif option == 2:
        listar_tarefas()

    elif option == 3:
        tarefa_id = input("Digite o ID da tarefa que deseja remover: ")
        remover_tarefa(tarefa_id)

    elif option == 4:
        break
