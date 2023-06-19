# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_simple_rules.krb'):
           [1672171825.6339471, 'bc_simple_rules_bc.py'],
         ('', '', 'bc_simple_rules_questions1.krb'):
           [1672171825.6509025, 'bc_simple_rules_questions1_bc.py'],
         ('', '', 'bc_simple_rules_questions2.krb'):
           [1672171825.6588814, 'bc_simple_rules_questions2_bc.py'],
         ('', '', 'bc_simple_rules_questions3.krb'):
           [1672171825.66686, 'bc_simple_rules_questions3_bc.py'],
         ('', '', 'bc_simple_rules_questions4.krb'):
           [1672171825.7658706, 'bc_simple_rules_questions4_bc.py'],
         ('', '', 'facts.kfb'):
           [1672171825.8027723, 'facts.fbc'],
         ('', '', 'questions1.kqb'):
           [1672171826.0241816, 'questions1.qbc'],
         ('', '', 'questions2.kqb'):
           [1672171826.026176, 'questions2.qbc'],
         ('', '', 'questions3.kqb'):
           [1672171826.0281706, 'questions3.qbc'],
         ('', '', 'questions4.kqb'):
           [1672171826.03216, 'questions4.qbc'],
         ('', '', 'venv\\Lib\\site-packages\\pyke\\krb_compiler\\compiler.krb'):
           [1672171826.1937306, 'compiler_bc.py'],
        },
        compiler_version)

