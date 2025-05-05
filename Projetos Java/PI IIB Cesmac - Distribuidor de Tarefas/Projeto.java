import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Projeto {
    private String nome;
    private String descricao;
    private List<Tarefas> tarefas;
    private List<String> tags;
    private Map<Integer, Membro> membros; // ID do usuário, informações do membro

    public Projeto(String nome, String descricao) {
        this.nome = nome;
        this.descricao = descricao;
        this.tarefas = new ArrayList<>();
        this.tags = new ArrayList<>();
        this.membros = new HashMap<>();
    }

    public void criarTarefa(String nome, String descricao, String status, Tarefas.Prazo prazoFinal) {
        Tarefas tarefa = new Tarefas(nome, descricao, status, prazoFinal);
        tarefas.add(tarefa);
    }

    public void adicionarTag(String tag) {
        tags.add(tag);
    }

    public void removerTag(String tag) {
        tags.remove(tag);
    }

    public void adicionarMembro(int usuarioId, String perfil) {
        Membro membro = new Membro(usuarioId, perfil);
        membros.put(usuarioId, membro);
    }

    public void removerMembro(int usuarioId) {
        membros.remove(usuarioId);
    }

    public void promoverMembro(int usuarioId) {
        Membro membro = membros.get(usuarioId);
        if (membro != null) {
            membro.setPerfil("ADM");
        }
    }

    public void rebaixarMembro(int usuarioId) {
        Membro membro = membros.get(usuarioId);
        if (membro != null) {
            membro.setPerfil("Membro");
        }
    }

    public void distribuirTarefas() {
        boolean algumSelecionado = false;
        List<Tarefas> tarefasSemResponsavel = new ArrayList<>();

        for (Tarefas tarefa : tarefas) {
            if (tarefa.responsaveis.isEmpty()) {
                tarefasSemResponsavel.add(tarefa);
            }
        }

        for (Tarefas tarefa : tarefasSemResponsavel) {
            List<Integer> aptos = new ArrayList<>();

            for (Map.Entry<Integer, Membro> entrada : membros.entrySet()) {
                Membro membro = entrada.getValue();
                if (membro.tarefas.isEmpty() && membro.tags.stream().anyMatch(tarefa.tags::contains)) {
                    aptos.add(entrada.getKey());
                }
            }

            if (aptos.size() == 1) {
                tarefa.responsaveis.add(aptos.get(0));
                membros.get(aptos.get(0)).tarefas.add(tarefa.nome);
                algumSelecionado = true;
            }
        }

        for (Tarefas tarefa : tarefasSemResponsavel) {
            if (tarefa.responsaveis.isEmpty()) {
                if (algumSelecionado) {
                    distribuirTarefas();
                } else {
                    int menorQuantidadeTarefas = Integer.MAX_VALUE;
                    int membroSelecionado = -1;

                    for (Map.Entry<Integer, Membro> entrada : membros.entrySet()) {
                        Membro membro = entrada.getValue();
                        if (membro.tarefas.size() < menorQuantidadeTarefas) {
                            menorQuantidadeTarefas = membro.tarefas.size();
                            membroSelecionado = entrada.getKey();
                        }
                    }

                    if (membroSelecionado != -1) {
                        tarefa.responsaveis.add(membroSelecionado);
                        membros.get(membroSelecionado).tarefas.add(tarefa.nome);
                    }
                }
            }
        }
    }

    // Classe interna para Membro
    private static class Membro {
        private int usuarioId;
        private String perfil;
        private List<String> tags;
        private List<String> tarefas;

        public Membro(int usuarioId, String perfil) {
            this.usuarioId = usuarioId;
            this.perfil = perfil;
            this.tags = new ArrayList<>();
            this.tarefas = new ArrayList<>();
        }

        public void setPerfil(String perfil) {
            this.perfil = perfil;
        }
    }
}
