import java.io.Serializable;
import java.util.ArrayList; 
import java.util.List;

public class Usuario implements Serializable{
    private static final long serialVersionUID = 1L;

    private String nome;
    private int id;
    private String senha;
    private List<Notificacao> notificacoes;
    private List<String> tagsDefault;

    public int getID() {
        return id;
    }

    public Usuario(String nome, int id, String senha) { 
        this.nome = nome; 
        this.id = id; 
        this.senha = senha;
        this.notificacoes = new ArrayList<>(); 
        this.tagsDefault = new ArrayList<>(); } 
        public void criarProjeto() { 
            // Implementar a lógica para criar um projeto 
    } 

    public void alterarNome(String novoNome) { 
        this.nome = novoNome; 
    }  
    public void verNotificacoes() { 
        for (Notificacao notificacao : notificacoes) { 
            System.out.println(notificacao.getTexto()); 
            notificacao.setLido(true); } 
    }
    
    // Classe interna para Notificação     
    private static class Notificacao { 
        private String texto; 
        private boolean lido; 
        private String nomeProjeto; 
        private String nomeTarefa; 
        public Notificacao(String texto, String nomeProjeto, String nomeTarefa) { 
            this.texto = texto; 
            this.lido = false; 
            this.nomeProjeto = nomeProjeto; 
            this.nomeTarefa = nomeTarefa; }
        public String getTexto() { 
            return texto; } 
        public boolean isLido() { 
            return lido; } 
    public void setLido(boolean lido) { 
        this.lido = lido; } 
    } 
}