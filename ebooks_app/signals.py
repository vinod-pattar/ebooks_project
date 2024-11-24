# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order

@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    if created:
        # Email subject and message
        subject = f"Order Confirmation - Order #{instance.id}"
        message = f"""
        Dear {instance.user.username},

        Thank you for your order! Here are the details of your order:

        Order ID: {instance.receipt_id}
        Total Price: ₹{instance.total_price}
        Payment Method: {instance.payment_method}
        Status: {instance.status}

        We will notify you once your order is shipped.

        Thank you for shopping with us!

        Best regards,
        Your Shop Team
        """

        # Send email
        send_mail(
            subject=subject,
            message=message,
            from_email='yourshop@example.com',  # Replace with your actual email
            recipient_list=[instance.user.email],  # Send to the user's email
            fail_silently=False,  # Raise an error if sending fails
        )
