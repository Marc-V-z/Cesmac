import java.util.ArrayList;
import java.util.List;

public class Tarefas {
    private String nome;
    private String descricao;
    private boolean concluida;
    private String status; // Pendente, Atrasado, Fora do prazo
    private List<Integer> responsaveis; // IDs dos usuários responsáveis
    private Prazo prazoEstimado;
    private Prazo prazoFinal;
    private List<String> tags; // Tags do projeto

    public Tarefas(String nome, String descricao, String status, Prazo prazoFinal) {
        this.nome = nome;
        this.descricao = descricao;
        this.concluida = false;
        this.status = status;
        this.responsaveis = new ArrayList<>();
        this.tags = new ArrayList<>();
        this.prazoFinal = prazoFinal;
    }

    public void concluirTarefa() {
        this.concluida = true;
        this.status = "Concluída";
    }

    // Classe interna para Prazo
    public static class Prazo {
        private int dia;
        private String mes;
        private int ano;

        public Prazo(int dia, String mes, int ano) {
            this.dia = dia;
            this.mes = mes;
            this.ano = ano;
        }
    }
}
