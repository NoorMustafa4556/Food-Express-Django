import os, glob

base_dir = r"c:\Users\NoorMustafa\Desktop\Food Express\myproject\myapp\templates\food"
for filepath in glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Don't inject into messages.html itself
    if 'messages.html' in filepath: continue
    # Don't double inject
    if "{% include 'food/messages.html' %}" in content: continue
    if 'login.html' in filepath or 'signup.html' in filepath or 'change_password.html' in filepath: continue
    
    modified = False
    
    # Safest is right after </nav>
    if '</nav>' in content:
        content = content.replace('</nav>', '</nav>\n    <div class="container mt-3">\n        {% include \'food/messages.html\' %}\n    </div>', 1)
        modified = True
    elif '<div class="container' in content:
        content = content.replace('<div class="container', '<div class="container mt-3">\n    {% include \'food/messages.html\' %}\n</div>\n<div class="container', 1)
        modified = True
                
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Injected messages into {os.path.basename(filepath)}')
