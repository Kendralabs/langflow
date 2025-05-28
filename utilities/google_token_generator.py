from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    '/Users/anshu/Downloads/client_secret_875904622593-7hk64ek4sgj9uqorhrui4hdu4mj795mb.apps.googleusercontent.com.json',
    scopes=['https://www.googleapis.com/auth/drive.readonly']
)

credentials = flow.run_local_server()
with open('/Users/anshu/Downloads/token.json', 'w') as token_file:
    token_file.write(credentials.to_json())
