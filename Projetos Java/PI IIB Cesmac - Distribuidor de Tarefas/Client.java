import java.util.Scanner;

public class Client {
    
    public static void RegistrarUser() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Registre um nome de Usuario: ");
        String nome = scanner.next();
        System.out.println("Registre uma senha: ");
        String senha = scanner.next();
        Servidor.UserRegister(nome, senha);
    }
}
