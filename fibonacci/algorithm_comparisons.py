from dynamic_prog import fib_string as dyn_fib
from formula import fib_string as form_fib
from recursion import fib_string as rec_fib
from timeit import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compare_algorithms(n_values, use_methods, fname: str = None):

    m_values = np.array([rec_fib, dyn_fib, form_fib])[use_methods]
    methods = np.array(['Recursive Programming', 'Dynamic Programming', 'Formulaic Approximation'])[use_methods]

    t_values = []
    for n in n_values:
        for m in m_values:
            t = timeit(stmt=f'fib({n})', setup=m, number=1)
            t_values.append(t)

    results = pd.DataFrame(
        data=np.array(t_values).reshape((-1, len(methods))),
        index=n_values,
        columns=methods
    )

    plt.clf()
    ax = sns.lineplot(
        data=results.reset_index().rename(mapper={'index': 'n'}, axis=1).melt(
            id_vars='n',
            var_name='Method',
            value_name='Time Taken'
        ),
        x='n',
        y='Time Taken',
        hue='Method'
    )
    ax.set_xticks(ticks=[i for i in ax.get_xticks() if i == int(i) and i > 0])
    plt.tight_layout()
    if fname is not None:
        plt.savefig(fname=fname)

# compare_algorithms(n_values=[n for n in range(1, 21)], use_methods=[True, True, True], fname='./fibonacci/assets/rec-dyn-form.png')

# compare_algorithms(n_values=[n for n in range(1, 1001)], use_methods=[False, True, True], fname='./fibonacci/assets/dyn-form.png')

# compare_algorithms(n_values=[n for n in range(1, 1001)], use_methods=[False, False, True], fname='./fibonacci/assets/form.png')