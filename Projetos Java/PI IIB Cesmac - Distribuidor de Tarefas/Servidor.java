import java.io.*;
import java.net.*;
import java.util.*;
import java.time.LocalDate;

public class Servidor {
    private static final int PORT = 12345;
    private static List<Usuario> usuarios = new ArrayList<>();
    private static List<Projeto> projetos = new ArrayList<>();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Servidor iniciado na porta " + PORT);

            while (true) {
                Socket socket = serverSocket.accept();
                new ServidorHandler(socket).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static class ServidorHandler extends Thread {
        private Socket socket;

        public ServidorHandler(Socket socket) {
            this.socket = socket;
        }

        public void run() {
            try (ObjectInputStream input = new ObjectInputStream(socket.getInputStream());
                 ObjectOutputStream output = new ObjectOutputStream(socket.getOutputStream())) {
                
                String comando = (String) input.readObject();
                
                switch (comando) {
                    case "ADICIONAR_USUARIO":
                        Usuario usuario = (Usuario) input.readObject();
                        usuarios.add(usuario);
                        output.writeObject("USUARIO_ADICIONADO");
                        break;
                    case "LISTAR_USUARIOS":
                        output.writeObject(usuarios);
                        break;
                    case "CRIAR_PROJETO":
                        Projeto projeto = (Projeto) input.readObject();
                        projetos.add(projeto);
                        output.writeObject("PROJETO_CRIADO");
                        break;
                }
            }
        }
    }

    private  static int usuariosID() {
        LocalDate dataAtual = LocalDate.now();
        int ano = dataAtual.getYear(); 
        int mes = dataAtual.getMonthValue(); 
        int dia = dataAtual.getDayOfMonth();
        
        int dataID = ano + mes + dia + 0;
        while (true) { 
            int contador = 0;
            for (Usuario usuario :usuarios) {
                if (usuario.getID() == dataID) {
                    contador += 1;
                    dataID += 1;
                    break;
                }
            }
            if (contador == 0) {
                return dataID;
            }
        }
    }

    public static void UserRegister(String nome, String senha) {
        int id = usuariosID();
        Usuario novoUsuario = new Usuario(nome, id, senha);
        usuarios.add(novoUsuario);
    }
}