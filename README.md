# Grafana-skype-exporter
1) Deploy the app in a web server
2) Replace skype user/password with your robot user/pass
3) This app can send messages in groups so add the bot to your Skype group
4) Groups should have names since this is the way, we find you group id which is used to send notifications to
5) in your Grafana notification channel, add a new notification channel of type: Webhook
6) give this value to your channel:
  YourWebServerIP/SkypeNotifier/<your_group_name>
7) Done
8) If you want to include the image as well, you need to first config the external data storage in your Grafana config file and then add the image_url key from response to your message. Also, you need to check the 'include image' option in your Grafana alert channel
