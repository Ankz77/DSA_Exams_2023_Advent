class Browserstack:
    def __init__(self):
        self.forward_stack = []
        self.backward_stack = []

    def navigation(self, url):
        self.backward_stack.append(url)
        self.forward_stack = []

    def backward(self):
        if not self.backward_stack:
            return 'No backward history'
        url = self.backward_stack.pop()
        self.forward_stack.append(url)
        return url

    def forward(self):
        if not self.forward_stack:
            return 'No forward history'
        url = self.forward_stack.pop()
        self.backward_stack.append(url)
        return url

pages = [
    'www.google.com',
    'www.github.com',
    'www.yahoo.com',
    'www.ucu.com',
    'www.microsoft.com',
    'www.skype.com'
]

browser = Browserstack()

for page in pages:
    browser.navigation(page)
    print(f'Navigated to {page}')
    print(f'Back: {browser.backward()}')
    print(f'Forward: {browser.forward()}')