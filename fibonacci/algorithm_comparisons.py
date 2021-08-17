from dynamic_prog import fib_string as dyn_fib
from formula import fib_string as form_fib
from formula import fib_less_string as form_less_fib
from recursion import fib_string as rec_fib
from timeit import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

n_values = [n for n in range(1, 1001)]
methods = ['Dynamic Programming', 'Formulaic Approximation', 'Formulaic Approximation (simple)']

t_values = []
for n in n_values:
    for m in [dyn_fib, form_fib, form_less_fib]:
        t = timeit(stmt=f'fib({n})', setup=m, number=1)
        t_values.append(t)

results = pd.DataFrame(
    data=np.array(t_values).reshape((-1, 3)),
    index=n_values,
    columns=methods
)

sns.lineplot(
    data=results.reset_index().rename(mapper={'index': 'n'}, axis=1).melt(
        id_vars='n',
        var_name='Method',
        value_name='Time Taken'
    ),
    x='n',
    y='Time Taken',
    hue='Method'
)
plt.show()