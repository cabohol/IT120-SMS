from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client

def send_sms(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        message_body = request.POST.get("message_body")

        
        account_sid = 'twilio ssid'
        auth_token = 'twilio token'
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                body=message_body,
                from_='+17753733918',
                to=phone_number
            )
            return HttpResponse(f"SMS sent successfully! Message SID: {message.sid}")
        except Exception as e:
            return HttpResponse(f"Failed to send SMS. Error: {e}")

    return render(request, 'dashboard/sms.html')
