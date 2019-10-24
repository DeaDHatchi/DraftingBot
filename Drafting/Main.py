from Drafting.Drafting import Drafting


class Main:
    def __init__(self):
        self.state = True

    def exit(self):
        self.state = False

    def run(self):
        while self.state:
            self.lets_draft()

    def lets_draft(self):
        draft = Drafting()
        draft.lets_draft()
        choice = input('Do you want to draft again? (Y/N): ')
        if choice.upper() == 'Y':
            self.lets_draft()
        else:
            self.exit()


class Position:
    _roles = {1: 'Carry',
              2: 'Mid',
              3: 'Offlane',
              4: 'Flex',
              5: 'Support'}

    def __init__(self, ident):
        self.ident = ident
        self.role = self._roles[self.ident]


if __name__ == '__main__':
    main = Main()
    main.run()
    print('debugline')
