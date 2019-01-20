from django import template
register = template.Library()

@register.filter
def gt(first_entity,second_entity ):
    return first_entity > second_entity 
