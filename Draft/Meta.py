class Position:
    _roles = {1: 'Carry',
              2: 'Mid',
              3: 'Offlane',
              4: 'Flex',
              5: 'Support'}

    def __init__(self, ident):
        self.ident = ident
        self.role = self._roles[self.ident]