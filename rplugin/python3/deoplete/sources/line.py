from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'line'
        self.mark = '[line]'
        self.rank = 2

    def gather_candidates(self, context):
        filetype = context.get('filetype', '')
        files = self.vim.eval('g:deoplete#files')
        canidates = []
        for filename, filetypes in files:
            if filetype in filetypes or len(filetypes) == 0:
                with open(filename) as f:
                    for line in f:
                        canidates.append({'word': line[:-1]})
        return canidates
