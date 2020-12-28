import base64


def base64ToString(message_id, stringToBeDecoded):
    xml_content = base64.urlsafe_b64decode(stringToBeDecoded).decode('utf-8')
    with open(message_id + '.xml', 'w') as writer:
        writer.write(xml_content)
