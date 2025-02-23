class HtmlElement:
    indent_size = 2
    def __init__(self,name='',text=''):
        self.text = text
        self.name = name
        self.elements = []
        
    def __str__(self,indent=0):
        lines = []
        i = ' ' * (indent*self.indent_size)
        lines.append(f'{i}<{self.name}>')
        
        if self.text:
            i1 = ' ' * ((indent+1)*self.indent_size)
            lines.append(f'{i1}{self.text}')
        
        for e in self.elements:
            lines.append(e.__str__(indent+1))
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)
    
    @staticmethod
    def create(name):
        return HtmlBuilder(name)

class HtmlBuilder:
    def __init__(self,root_name):
        self.root_name = root_name
        self._root = HtmlElement(name=root_name)
        
    def add_child(self,child_name, child_text):
        self._root.elements.append(
            HtmlElement(child_name, child_text)
        )
        
    def add_child_fluent(self,child_name,child_text):
        self._root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self
        
    def __str__(self):
        return str(self._root)
    
builder = HtmlElement.create('ul')
# builder = HtmlBuilder('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', "adult")
builder.add_child_fluent('li', 'hello').add_child_fluent('li', "adult")
print("Ordinary Builder")
print(builder)