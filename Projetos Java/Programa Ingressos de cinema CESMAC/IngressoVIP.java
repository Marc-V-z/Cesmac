public class IngressoVIP extends Ingresso { 
    public IngressoVIP(Filme filme, String tipo, String horario) { 
        super(filme, tipo, horario); 
    } 

    @Override 
    public double getPreco() { 
        return tipo.equals("inteiro") ? 48.0 : 24.0; } 
    
    @Override 
    public void acessoLanchonete() { 
        System.out.println("Lanchonete do cinema liberada"); } 

    @Override
    public Boolean PasseVIP() { 
        return true;
    }
        
    @Override 
    public void setFilme(Filme filme) { 
        this.filme = filme; 
    }

    @Override
    public String toString() {
        return tipo + TipoIngressoEspaco() + filme.getNome() + " - " + horario + "  | VIP |";
    }
}