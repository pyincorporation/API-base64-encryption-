import requests


def get_user_creadentions(username, password):
    connection_fail = False
    username_auth = 'bcsClass'
    password_auth = 'jaribuKuingia@bcs$$+++!XZty'
    payload = {
        'username':username_auth,
        'password':password_auth
    }
    response = requests.post('https://isms.iaa.ac.tz/ismsapi/hakiki.php', verify=False, json = payload)
    if response.status_code == 200:
        auth_token = response.json().get('token')
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            'username':username,
            'password':password
        }
    else:
        connection_fail = True
    url_2 = 'https://isms.iaa.ac.tz/ismsapi/students.php'
    ren = requests.post(url_2, headers=headers, verify=False, json = payload)
    content = ren.json()
    return content, connection_fail