import java.io.IOException;
import java.util.Scanner;

public class MenuController {
    private Scanner scanner = new Scanner(System.in);
    private CinemaSystem cinemaSystem = new CinemaSystem();

    public void iniciarMenu() {
        while (true) {
            //cinemaSystem.exibirselecionado();
            exibirMenu();
            int escolha = scanner.nextInt();
            scanner.nextLine(); // pular linha
            Limpar(); // Limpar tela
            switch (escolha) {
                case 1:
                    selecionarFilme();
                    break;
                case 2:
                    comprarIngresso();
                    break;
                case 3:
                    exibirResultadoFinal();
                    break;
                case 4:
                    acessarLanchonete();
                    break;
                case 5:
                    if (cinemaSystem.getFilmeSelecionado() != null) {
                    exibirdetalhes();
                    }
                    break;
                case 0:
                    System.out.println("Saindo...");
                    return;
                default:
                    System.out.println("Escolha inválida. Tente novamente.");
            }
        }
    }

    private void exibirMenu() {
        System.out.println("");
        System.out.println("1. Selecionar Filme");
        System.out.println("2. Comprar Ingresso");
        System.out.println("3. Exibir Resultado Final");
        System.out.println("4. Acessar lanchonete");
        if (cinemaSystem.getFilmeSelecionado() != null) {
            System.out.println("5. Exibir Detalhes do Filme");}
        System.out.println("0. Sair");
        System.out.println("");
        System.out.print("Escolha uma opção: ");
    }

    private void selecionarFilme() {
        cinemaSystem.listarFilmes();
        System.out.print("Selecione o filme pelo número: ");
        int numeroFilme = scanner.nextInt();
        System.out.println(); //pular linha
        cinemaSystem.selecionarFilme(numeroFilme);
    }

    private void comprarIngresso() {
        cinemaSystem.exibirselecionado();
        System.out.println();
        System.out.print("Ingressos VIP? (1. Sim | 2. Não): "); 

        boolean vip = false;
        String escolha = scanner.next();
        if (escolha.equalsIgnoreCase("sim") || escolha.equalsIgnoreCase("yes") ||
        escolha.equalsIgnoreCase("S") || escolha.equalsIgnoreCase("Y") || escolha.equalsIgnoreCase("1")) {
            vip = true;}
        
        System.out.print("Digite a quantidade de ingressos inteiros: ");
        int inteiros = scanner.nextInt();
        System.out.print("Digite a quantidade de ingressos meia: ");
        int meia = scanner.nextInt();
        System.out.println(); //pular linha
        cinemaSystem.comprarIngresso(inteiros, meia, vip);
    }

    private void exibirResultadoFinal() {
        cinemaSystem.exibirTotal();
    }

    private void acessarLanchonete() {
        cinemaSystem.acessoLanchonete();
    }

    private void exibirdetalhes() {
        Filme selecionado = cinemaSystem.getFilmeSelecionado();
        String nomeFilme = selecionado.getNome();
        String diretorFilme = selecionado.getDiretor();
        String descricaoFilme = selecionado.getDescrição();
        String generoFilme = selecionado.getGenero();
        String tempo = selecionado.CalcularDuracao();

        System.out.print(nomeFilme);
        System.out.println("     | Diretor: " + diretorFilme + " |");
        System.out.print("("+generoFilme+")");
        System.out.println("         ["+ tempo +"]");
        System.out.print("\n" + descricaoFilme);
        System.out.println();
    }

    public void Limpar() {
        String sistemaOperacional = System.getProperty("os.name").toLowerCase(); 
        try { 
            if (sistemaOperacional.contains("win")) {  // Comando para Windows 
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor(); } 
            else { // Comando para outros sistemas operacionais (Unix/Linux/MacOS) 
                new ProcessBuilder("clear").inheritIO().start().waitFor(); } 
        } 
        catch (IOException | InterruptedException e) { e.printStackTrace(); } 
    }
}

