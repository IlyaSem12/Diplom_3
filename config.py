#================CONSTANT URLS GUI================
BASE_URL = 'https://stellarburgers.education-services.ru/'
LOGIN_URL = f'{BASE_URL}login'
FEED_URL = f'{BASE_URL}feed'
PASSWORD_RECOVERY_URL = f'{BASE_URL}forgot-password'
PROFILE_URL = f'{BASE_URL}account/profile'
ORDER_HISTORY_URL = f'{BASE_URL}account/order-history'
#================CONSTANT URLS API================
REGISTRATION_API_URL = f'api/auth/register'
LOGIN_API_URL = f'api/auth/login'
USER_API_URL = f'/api/auth/user'
ALL_API_ORDERS_URL = f'/api/orders/all'
#================CONSTANT DATA================
PASSWORD_FIELD_BORDERS = "rgb(76, 76, 255)"
PLACEHOLDER_NUMBER =  "9999"
MESSAGE_IN_PROGGERSS_ORDERS = "Все текущие заказы готовы!"
SCRIPT_DARG_AND_DROP = """
        const source = arguments[0];
        const target = arguments[1];

        const dataTransfer = new DataTransfer();

        source.dispatchEvent(new DragEvent('dragstart', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        }));

        target.dispatchEvent(new DragEvent('dragenter', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        }));

        target.dispatchEvent(new DragEvent('dragover', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        }));

        target.dispatchEvent(new DragEvent('drop', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        }));

        source.dispatchEvent(new DragEvent('dragend', {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        }));
    """