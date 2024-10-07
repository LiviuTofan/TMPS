package Lab0.Notifications;

import Lab0.User;

public class EmailNotification implements Notification {

    @Override
    public void send(User user) {
        System.out.println("Sending Email to " + user.getEmail() + ": Welcome " + user.getUsername() + "!");
    }
}
