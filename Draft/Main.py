from Draft.Drafting import Drafting


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
        if choice.upper().strip() == 'Y' or choice.upper().strip() == 'YES':
            self.lets_draft()
        else:
            self.exit()


if __name__ == '__main__':
    main = Main()
    main.run()
