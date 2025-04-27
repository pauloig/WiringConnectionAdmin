from django import template
import base64
from django.core.files.storage import default_storage

register = template.Library()

@register.filter
def get_signature_base64(signature_field):
    try:
        if signature_field and hasattr(signature_field, 'path'):
            with default_storage.open(signature_field.path, 'rb') as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                return encoded_string
    except Exception:
        return ''
    return ''