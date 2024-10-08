package Lab0;

public class AuthService {
    public boolean login(User user, String password) {
        if ("password123".equals(password)) {
            System.out.println(user.getUsername() + " has logged in successfully!");
            return true;
        }
        System.out.println("Login failed for " + user.getUsername());
        return false;
    }
}
