def adicionarTarefa(tarefas):
    tarefa = input('Tarefa: ')
    tarefas.append(tarefa)


def listarTarefas(tarefas):
    for tarefa in tarefas:
        print(tarefa)


def desfazer(tarefasFazer, tarefasRetiradas):
    if len(tarefasFazer) == 0:
        print('Nenhuma tarefa!')
        return

    tarefa = tarefasFazer.pop()
    tarefasRetiradas.append(tarefa)


def refazer(tarefasFazer, tarefasRetiradas):
    if len(tarefasRetiradas) == 0:
        print('Nenhuma tarefa desfeita!')
        return

    tarefa = tarefasRetiradas.pop()
    tarefasFazer.append(tarefa)


tarefasFazer = []
tarefasRetiradas = []

while True:
    opcao = input(
        'Comando > ')
    if opcao == 'add':
        adicionarTarefa(tarefasFazer)
        continue
    if opcao == 'ls':
        listarTarefas(tarefasFazer)
        continue

    if opcao == 'undo':
        desfazer(tarefasFazer, tarefasRetiradas)
        continue

    if opcao == 'redo':
        refazer(tarefasFazer, tarefasRetiradas)
        continue

    if opcao == 'sair':
        break
