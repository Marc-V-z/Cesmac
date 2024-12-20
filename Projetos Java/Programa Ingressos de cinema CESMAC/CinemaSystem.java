import java.util.ArrayList;
import java.util.List;

public class CinemaSystem {
    private List<Filme> filmes = new ArrayList<>();
    private List<Ingresso> ingressos = new ArrayList<>();
    private Filme filmeSelecionado;

    public CinemaSystem() {
        filmes.add(new Filme("O Poderoso Chefão", "Francis Ford Coppola", "A história da família Corleone, liderada por Don Vito Corleone (Marlon Brando), e a ascensão de seu filho Michael (Al Pacino) ao poder da máfia.", "Crime e Drama", 175, false));
        filmes.add(new Filme("O Senhor dos Anéis", "Peter Jackson", "A jornada do hobbit Frodo Bolseiro para destruir o Um Anel, que é a chave para o poder do Senhor Sauron.", "Fantasia", 178, false));
        filmes.add(new Filme("A Família Addams", "Barry Sonnenfeld", "A família Addams, uma família excêntrica e gótica, enfrenta desafios enquanto tenta se integrar à sociedade.", "Comédia", 114, false));
        filmes.add(new Filme("Edward Mãos de Tesoura", "Tim Burton", "Edward, um jovem com mãos de tesoura, se apaixona por uma mulher chamada Kim e tenta encontrar seu lugar no mundo.", "Romance", 114, false));
        filmes.add(new Filme("O Menino e o Mundo", "Alê Abreu", "A história de um menino que sonha em ser um músico e sua jornada através de um mundo cheio de desafios e descobertas.", "Animação", 80, false));
        filmes.add(new Filme("Avatar (3D)", "James Cameron", "No exuberante mundo alienígena de Pandora vivem os Na'vi, seres que parecem ser primitivos, mas são altamente evoluídos. Como o ambiente do planeta é tóxico, foram criados os avatares, corpos biológicos controlados pela mente humana que se movimentam livremente em Pandora. Jake Sully, um ex-fuzileiro naval paralítico, volta a andar através de um avatar e se apaixona por uma Na'vi. Esta paixão leva Jake a lutar pela sobrevivência de Pandora.", "Ficção científica", 162, true));
        filmes.add(new Filme("Jurassic Park: O Parque dos Dinossauros (3D)", "Steven Spielberg", "Os paleontólogos Alan Grant, Ellie Sattler e o matemático Ian Malcolm fazem parte de um seleto grupo escolhido para visitar uma ilha habitada por dinossauros criados a partir de DNA pré-histórico. O idealizador do projeto e bilionário John Hammond garante a todos que a instalação é completamente segura. Mas após uma queda de energia, os visitantes descobrem, aos poucos, que vários predadores ferozes estão soltos e à caça.", "Ficção científica", 127, true));
        filmes.add(new Filme("Toy Story 3 (3D)", "Lee Unkrich", "Com seu amado Andy se preparando para ir para a universidade, Woody, Buzz Lightyear e o restante dos brinquedos enfrentam o seu maior medo: serem esquecidos quando são colocados no sótão. Mas, por engano, acabam no meio-fio. Woody, o único escolhido para acompanhar Andy, percebe o erro e salva a gangue, mas os brinquedos acabam em uma creche. Lá, todos percebem que existe um lugar com brincadeiras infinitas, mas os pequenos são incontroláveis e Woody e sua turma decidem planejar uma grande fuga.", "Animação", 103, true));
        // filmes.add(new Filme("Nome do filme", "Diretor", "Descrição", "Genero", Duração));
    }

    public void listarFilmes() {
        for (int i = 0; i < filmes.size(); i++) {
            System.out.println((i + 1) + ". " + filmes.get(i));
        }
    }

    public void selecionarFilme(int indice) {
        if (indice > 0 && indice <= filmes.size()) {
            filmeSelecionado = filmes.get(indice - 1);
            System.out.println("Filme selecionado: " + filmeSelecionado.getNome());
        } else {
            System.out.println("Filme inválido.");
        }
    }

    public void comprarIngresso(int inteiros, int meias, boolean vip) {
        if (filmeSelecionado == null) {
            System.out.println("[ Selecione um filme primeiro. ]");
            return;
        }
        /*  (Codigo antigo)
        for (int i = 0; i < inteiros; i++) {
            ingressos.add vip ? (new Ingresso(filmeSelecionado, "inteiro", "14:00"));
        }
        for (int i = 0; i < meias; i++) {
            ingressos.add(new Ingresso(filmeSelecionado, "meia", "14:00"));
        }
        */
        for (int i = 0; i < inteiros; i++) { 
            if (vip || !filmeSelecionado.isFilme3D()) {  // se for vip então não importa, se não for vip ent so não sendo 3d também
                Ingresso ingresso = vip ? new IngressoVIP(filmeSelecionado, "inteiro", "14:00") : new Ingresso(filmeSelecionado, "inteiro", "14:00"); 
                ingressos.add(ingresso); }
            else {
                System.out.println("Filmes 3D só podem ser comprados com ingressos VIP.");
                return;  // ideia: usar sistema parecido porém usando break; para filmes com idade indicativa, assim alguns filmes não poderiam comprar meia, mas inteiras sim
            }
        } 
        for (int i = 0; i < meias; i++) { 
            if (vip || !filmeSelecionado.isFilme3D()) {
                Ingresso ingresso = vip ? new IngressoVIP(filmeSelecionado, "meia", "14:00") : new Ingresso(filmeSelecionado, "meia", "14:00"); 
                ingressos.add(ingresso); }
            else {
                System.out.println("Filmes 3D só podem ser comprados com ingressos VIP.");
                return;
            }
        }
        
    }

    public void exibirTotal() {
        double total = 0;
        for (Ingresso ingresso : ingressos) {
            total += ingresso.getPreco();

            System.out.println(ingresso);
        }
        System.out.println("------------------------------------");
        System.out.println("Total a pagar: R$ " + total);
    }

    public void acessoLanchonete(){               // existiam metodos melhores... mas tentei seguir mais as instruções da EA
        for (Ingresso ingresso : ingressos) {
            if (ingresso.PasseVIP() == true) {
                ingresso.acessoLanchonete(); 
                return;
            }
        }
        System.out.println("Compre um ingresso VIP");
    }

    public Filme getFilmeSelecionado() {
        return filmeSelecionado;
    }

    public void exibirselecionado() {
        if (filmeSelecionado != null) {
            System.out.println("Filme Selecionado: " + filmeSelecionado.getNome());
        }
    }
}
