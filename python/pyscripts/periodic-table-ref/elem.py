import pandas as pd

elements = pd.read_excel('/Users/ethanwater/Documents/Projects/elements/ptelemdata.xlsx')
hd = list(elements.columns)
elements = elements.set_index('Symbol').T.to_dict('list')
symbols = list(elements.keys())

def syminfo():
    sym = input('Input Element Symbol: ')
    if sym in symbols:
        print(hd[1:])
        print(elements.get(sym))
    else:
        print('invalid input')
        syminfo()

syminfo()
