import markdown

file_path = '/Users/minah.kim/Desktop/Python/'
file_name = 'pyenv.md'
target_file = file_path + file_name

# with open(target_file, 'r', encoding='UTF-8') as file:
#     text = file.read()

text = '''
20211128

```bash
brew install pyenv
pyenv install 3.10.0
pyenv global 3.10.0
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
cat .zshrc
# # python
# if command -v pyenv 1>/dev/null 2>&1; then
#   eval "$(pyenv init -)"
# fi
```

20211129

```bash
# seleniumを使うためにchromedriverをmacにインストール
brew install chromedriver
```
'''
extensions = ["nl2br", "fenced_code"]
html = markdown.markdown(text, extensions=extensions)
print(html)
body = '{}'.format(html)
