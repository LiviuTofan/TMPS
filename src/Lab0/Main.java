package Lab0;

import Lab0.Notifications.EmailNotification;
import Lab0.Notifications.Notification;
import Lab0.Notifications.PushNotification;
import Lab0.Notifications.SMSNotification;

public class Main {
    public static void main(String[] args) {

        User user = new User("Liviu Tofan", "liviutofan@mail.com", "123-456-7890");
        AuthService authService = new AuthService();

        if (authService.login(user, "password123")) {
            Notification emailNotification = new EmailNotification();
            emailNotification.send(user);

            Notification smsNotification = new SMSNotification();
            smsNotification.send(user);

            Notification pushNotification = new PushNotification();
            pushNotification.send(user);
        }
    }
}
