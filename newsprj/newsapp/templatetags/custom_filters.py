from django import template

register = template.Library()



BAD_WORDS = ['Жопа',
             'вонючка',
             ]

@register.filter()
def censor(text: str):
    text_list = text.split()
    for i in range(len(text_list)):
        for c in BAD_WORDS:
            if text_list[i].find(c) >= 0:
                repl_word = c[0] + (len(c) - 1) * '*'
                text_list[i] = text_list[i].replace(c, repl_word)
    return ' '.join(text_list)
