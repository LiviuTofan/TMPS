package Lab0.Notifications;

import Lab0.User;

public class SMSNotification implements Notification {

    @Override
    public void send(User user) {
        System.out.println("Sending SMS to " + user.getPhoneNumber() + ": Welcome " + user.getUsername() + "!");
    }
}
