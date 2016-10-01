from prettytable import PLAIN_COLUMNS, PrettyTable


def to_table(resolvelist):
    tablelist = []
    for item in resolvelist:
        if 'Answer' in item:
            table = PrettyTable(['NAME', 'DATA', 'TTL'])
            for a in item['Answer']:
                table.add_row([a['name'], a['data'], a['TTL']])
        table.set_style(PLAIN_COLUMNS)
        table.align = 'l'
        tablelist.append(table)
    return tablelist
