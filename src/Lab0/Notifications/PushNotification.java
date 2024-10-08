package Lab0.Notifications;

import Lab0.User;

public class PushNotification implements Notification {

    @Override
    public void send(User user) {
        System.out.println("Sending Push Notification to " + user.getUsername() + ": Welcome to the app!");
    }
}
