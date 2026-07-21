from .models import Notification, DeviceToken
from .firebase import send_push_notification


def get_user_name(user):
    
    print("NOTIFICATION USER:")
    print("ID:", user.id)
    print("FIRST NAME:", user.first_name)
    print("LAST NAME:", user.last_name)
    print("USERNAME:", user.username)


    # Same format used during registration
    first_name = (user.first_name or "").strip()
    last_name = (user.last_name or "").strip()


    fullname = f"{first_name} {last_name}".strip()


    if fullname:
        return fullname.title()


    return "User"



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


    devices = DeviceToken.objects.filter(
        user=user
    )


    for device in devices:

        try:

            send_push_notification(
                token=device.token,
                title=title,
                body=message,
            )

            print("✅ Push sent")

        except Exception as e:

            print("Push error:", e)


    return notification



# ==============================
# WELCOME
# ==============================

def send_welcome_notification(user):

    name = get_user_name(user)

    return create_notification(
        user=user,
        notification_type="welcome",
        title="🎉 Welcome to Mass Data",
        message=f"""
Hello {name} 👋


Welcome to Mass Data.


You can now enjoy:

📶 Data

📱 Airtime

📺 Cable TV

⚡ Electricity

💰 Wallet Services
"""
    )



# ==============================
# LOGIN
# ==============================

def send_login_notification(
    user,
    device,
    ip,
    login_time
):

    name = get_user_name(user)

    return create_notification(
        user=user,
        notification_type="login",
        title="🔐 New Login Detected",
        message=f"""
Hello {name} 👋


A new login was detected.


📱 Device:
{device}


🌍 IP:
{ip}


🕒 Time:
{login_time}
"""
    )



# ==============================
# WALLET
# ==============================

def send_wallet_notification(
    user,
    amount
):

    name = get_user_name(user)

    return create_notification(
        user=user,
        notification_type="wallet",
        title="💰 Wallet Funded",
        message=f"""
Hello {name} 👋


Your wallet has been credited.


Amount:

₦{amount}


Thank you for using Mass Data ❤️
"""
    )



# ==============================
# AIRTIME
# ==============================

def send_airtime_notification(
    user,
    network,
    phone,
    amount
):

    name = get_user_name(user)

    return create_notification(
        user=user,
        notification_type="airtime",
        title="📱 Airtime Purchase Successful",
        message=f"""
Hello {name} 👋


Your airtime purchase was successful.


Network:
{network}


Phone:
{phone}


Amount:
₦{amount}
"""
    )



# ==============================
# DATA
# ==============================

def send_data_notification(
    user,
    network,
    plan,
    phone
):

    name = get_user_name(user)

    return create_notification(
        user=user,
        notification_type="data",
        title="📶 Data Purchase Successful",
        message=f"""
Hello {name} 👋


Your data bundle was activated.


Network:
{network}


Plan:
{plan}


Phone:
{phone}
"""
    )



# ==============================
# CABLE TV
# ==============================

def send_cable_notification(
    user,
    provider,
    smartcard
):

    name = get_user_name(user)

    return create_notification(
        user=user,
        notification_type="cable",
        title="📺 Cable Subscription Successful",
        message=f"""
Hello {name} 👋


Your cable subscription is successful.


Provider:
{provider}


Smart Card:
{smartcard}
"""
    )



# ==============================
# ELECTRICITY
# ==============================

def send_electricity_notification(
    user,
    meter,
    amount
):

    name = get_user_name(user)

    return create_notification(
        user=user,
        notification_type="electricity",
        title="⚡ Electricity Payment Successful",
        message=f"""
Hello {name} 👋


Your electricity payment was successful.


Meter:
{meter}


Amount:
₦{amount}
"""
    )