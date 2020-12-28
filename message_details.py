from attachment import get_attachment


def get_message(service, message_id):
    try:
        message_content = service.users().messages().get(
            userId='me', id=message_id).execute()
        if(message_content['labelIds'][1] == 'INBOX' or message_content['labelIds'][1] == 'UNREAD' or message_content['labelIds'][2] == 'INBOX'):
            texto = message_content['snippet']
            if(texto.find('NF-e') > 0):
                get_attachment_id = message_content['payload']['parts'][1]['body']['attachmentId']
                get_attachment(service=service, message_id=message_id,
                               attachment_id=get_attachment_id)
    except:
        pass
