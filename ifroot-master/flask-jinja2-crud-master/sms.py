from twilio.rest import Client
import chaves

def mensagem_sms(texto, num_para_envio="+5511944227457"):
    client = Client(chaves.account_sid, chaves.auth_token)

    message = client.messages.create(
        body = texto,
        from_=chaves.twilio_number,
        to=num_para_envio
    )

    print(message.body)