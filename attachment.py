from convert import base64ToString


def get_attachment(service, message_id, attachment_id):
    try:
        attachment_base64 = service.users().messages().attachments().get(userId='me', messageId=message_id,
                                                                         id=attachment_id).execute()
        attachment_base64 = attachment_base64['data']
        #converted = base64ToString(message_id, attachment_base64)
        base64ToString(message_id, attachment_base64)
    except Exception as e:
        print(e)
    finally:
        pass
