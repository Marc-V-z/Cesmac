public class Filme {
    private String nome;
    private String diretor;
    private String descricao;
    private String genero;
    private int duracao; // em minutos
    private boolean filme3D;

    public Filme(String nome, String diretor, String descricao, String genero, int duracao, boolean filme3D) {
        this.nome = nome;
        this.diretor = diretor;
        this.descricao = descricao;
        this.genero = genero;
        this.duracao = duracao;
        this.filme3D = filme3D;
    }

    public String getNome() {
        return nome;
    }

    public String getDiretor() {
        return diretor;
    }

    public String getDescrição() {
        return descricao;
    }

    public String getGenero() {
        return genero;
    }

    public int getDuração() {
        return duracao;
    }

    public boolean isFilme3D() { 
        return filme3D;
    }

    public String CalcularDuracao() {
        int horas = getDuração() / 60;
        int minutos = getDuração() % 60;
        String tempo = horas + ":" + minutos;

        return tempo;
    }

    @Override
    public String toString() {
        return nome + " (" + genero + ") [" + CalcularDuracao() + "] - Dirigido por: " + diretor;
    }
}
