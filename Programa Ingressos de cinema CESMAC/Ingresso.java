

public class Ingresso {
    protected  Filme filme;
    protected String tipo; // "inteiro" ou "meia"
    protected String horario;

    public Ingresso(Filme filme, String tipo, String horario) {
        this.filme = filme;
        this.tipo = tipo;
        this.horario = horario;
    }

    public double getPreco() {
        return tipo.equals("inteiro") ? 24.0 : 12.0;
    }

    public void acessoLanchonete() { 
        System.out.println("Compre um ingresso VIP");
    }

    public Boolean PasseVIP() {  
        return false;
    }

    public void setFilme(Filme filme) { 
        if (filme == null) { 
            throw new IllegalArgumentException("Filme não pode ser nulo."); } 
        if (!filme.isFilme3D()) { 
            this.filme = filme; } 
        else { 
            System.out.println("Filmes 3D são permitidos apenas para ingressos VIP."); }
    }

    public String TipoIngressoEspaco() {
        String espacamento;
        if (tipo.equals("meia")) {
            espacamento = "    - ";
        }
        else {
            espacamento = " - ";
        }
        return espacamento;
    }

    @Override
    public String toString() {
        return tipo + TipoIngressoEspaco() + filme.getNome() + " - " + horario;
    }
}


