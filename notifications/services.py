# from .models import Notification
# from .firebase import send_push_notification
# import time
# from django.contrib.auth.models import User



# def create_notification(
#     user,
#     notification_type,
#     title,
#     message,
# ):

#     notification = Notification.objects.create(

#         user=user,

#         notification_type=notification_type,

#         title=title,

#         message=message
#     )


#     send_push_notification(

#         user=user,

#         title=title,

#         body=message

#     )


#     return notification



# def send_welcome_notification(user):

#     return create_notification(

#         user,

#         "welcome",

#         "🎉 Welcome to Mass Data",

#         """
# Thank you for choosing Mass Data.

# We are delighted to have you as part of our community.

# Enjoy fast and reliable Data, Airtime, Cable TV, Electricity and Wallet services.

# Thank you for trusting Mass Data.
# """

#     )



# def send_login_notification(
#     user,
#     device,
#     ip,
#     login_time
# ):

#     return create_notification(

#         user,

#         "login",

#         "🔐 New Login Detected",

#         f"""
# A new login was detected on your account.

# 📱 Device:
# {device}

# 🌍 IP Address:
# {ip}

# 🕒 Login Time:
# {login_time}

# If this wasn't you, please change your password immediately.
# """

#     )



# def send_airtime_notification(
#     user,
#     network,
#     phone,
#     amount,
#     transaction_id
# ):

#     return create_notification(

#         user,

#         "airtime",

#         "📱 Airtime Purchase Successful",

#         f"""
# Your airtime purchase was completed successfully.

# 📡 Network:
# {network}

# 📞 Phone Number:
# {phone}

# 💵 Amount:
# ₦{amount}

# 🆔 Transaction ID:
# {transaction_id}

# Thank you for choosing Mass Data.
# """

#     )



# def send_data_notification(
#     user,
#     network,
#     plan,
#     phone,
#     amount,
#     transaction_id
# ):

#     return create_notification(

#         user,

#         "data",

#         "📶 Data Purchase Successful",

#         f"""
# Congratulations!

# Your data plan has been delivered successfully.

# 📡 Network:
# {network}

# 📦 Plan:
# {plan}

# 📞 Phone Number:
# {phone}

# 💵 Amount:
# ₦{amount}

# 🆔 Transaction ID:
# {transaction_id}

# Enjoy your browsing.
# """

#     )





# def send_notification_every_5_seconds():

#     while True:

#         users = User.objects.all()

#         for user in users:

#             create_notification(
#                 user=user,
#                 notification_type="welcome",
#                 title="🎉 Mass Data Update",
#                 message=f"""
# Hello {user.username},

# Thank you for using Mass Data.

# Enjoy fast Airtime, Data, Cable TV,
# Electricity and Wallet services.
# """
#             )

#             print(
#                 f"Notification sent to {user.username}"
#             )
#             time.sleep(300)
#         # time.sleep(5)


from .models import Notification, DeviceToken
from .firebase import send_push_notification
def create_notification(
    user,
    notification_type,
    title,
    message,
    html_message=None,
):

    notification = Notification.objects.create(
        user=user,
        notification_type=notification_type,
        title=title,
        message=message,
        html_message=html_message,
    )

    # Get the user's device
    device = DeviceToken.objects.filter(user=user).first()

    if device:
        try:
            send_push_notification(
                token=device.token,
                title=title,
                body=message,
            )
            print("✅ Push notification sent")
        except Exception as e:
            print("❌ Push notification error:", e)
    else:
        print("❌ No device token found for user:", user.username)

    return notification

def send_welcome_notification(user):

    return create_notification(

        user=user,

        notification_type="welcome",

        title="🎉 Welcome to Mass Data",

        message=f"""
Hello {user.username},

Welcome to Mass Data.

Enjoy Data, Airtime, Cable TV and Wallet services.
""",


        html_message=f"""

<div style="
background:#0f172a;
padding:20px;
border-radius:15px;
font-family:Arial;
color:white;
">


<h2 style="
color:#22c55e;
">
🎉 Welcome to Mass Data
</h2>


<p>
Hello <b>{user.username}</b> 👋
</p>


<p>
Thank you for joining our platform.
</p>


<div style="
background:#1e293b;
padding:15px;
border-radius:10px;
">

<h3>
Available Services
</h3>


<p>📶 Fast Data Bundles</p>

<p>📱 Airtime Recharge</p>

<p>📺 Cable TV</p>

<p>⚡ Electricity Payment</p>

<p>💰 Wallet Services</p>


</div>


<p style="
color:#94a3b8;
">

Thank you for trusting Mass Data ❤️

</p>


</div>

"""

    )


def send_login_notification(
    user,
    device,
    ip,
    login_time
):

    return create_notification(

        user=user,

        notification_type="login",

        title="🔐 New Login Detected",

        message=f"""

Hello {user.username} 👋


A new login was detected on your Mass Data account.


📱 Device:
{device}


🌍 IP Address:
{ip}


🕒 Login Time:
{login_time}


If this was not you, please change your password immediately.


Thank you for using Mass Data ❤️

"""

    )