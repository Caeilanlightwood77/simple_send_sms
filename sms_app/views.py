from django.shortcuts import render, redirect
from django.contrib import messages  # For success and error messages
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.conf import settings

def send_sms(request):
    if request.method == "GET":
        # Render the form for GET requests
        return render(request, 'send_sms.html')

    if request.method == "POST":
        # Handle form submission
        to_number = request.POST.get('to')
        message_body = request.POST.get('message')

        if not to_number or not message_body:
            messages.error(request, "Both 'to' and 'message' fields are required.")
            return redirect('send_sms')  # Replace 'send_sms' with the appropriate URL name

        try:
            # Initialize Twilio client
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            # Send SMS
            message = client.messages.create(
                body=message_body,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=to_number
            )

            # Success message
            messages.success(request, "SMS sent successfully!")
            return redirect('send_sms')  # Replace 'send_sms' with the appropriate URL name

        except TwilioRestException as e:
            # Handle Twilio-specific errors
            messages.error(request, f"Failed to send SMS: {e.msg}.")
            return redirect('send_sms')
        except Exception as e:
            # Handle any other exceptions
            messages.error(request, f"An unexpected error occurred: {str(e)}")
            return redirect('send_sms')
