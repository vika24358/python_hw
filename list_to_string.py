list_of_recipients = [
    'vika24358@ukr.net',
    'aaaaaa@ukr.net'
]

# result = ''
# for email in list_of_recipients:
#     result += f' {email},'
#
# result = result.strip(', ')
#
# print(result)

result = ', '.join(list_of_recipients)
print(result)