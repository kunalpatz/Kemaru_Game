from mako.template import Template

template = """
<table>
% for user in users:
     <tr>
        <td>${user['username']}</td>
        <td>${user['description']}</td>
     </tr>
% endfor
</table>
"""

users = [{'c1': 2, 'c7': 0, 'c13': 0, 'c19': 0, 'c25': 2, 'c31': 0},
    {'c2': 0, 'c8': 0, 'c14': 5, 'c20': 0, 'c26': 0, 'c32': 4},
    {'c3': 0, 'c9': 2, 'c15': 0, 'c21': 0, 'c27': 0, 'c33': 0},
    {'c4': 0, 'c10': 0, 'c16': 0, 'c22': 3, 'c28': 0, 'c34': 0},
    {'c5': 5, 'c11': 0, 'c17': 0, 'c23': 0, 'c29': 0, 'c35': 0},
    {'c6': 2, 'c12': 0, 'c18': 4, 'c24': 0, 'c30': 3, 'c36': 0}]
result = Template(template).render(users=users)
print(result)