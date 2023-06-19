# bc_simple_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def treatment_manage_fever(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'HighFever39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.treatment_manage_fever: got unexpected plan from when clause 1"
            with engine.prove('facts', 'DuarationMoreThanThreeDays', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.treatment_manage_fever: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_treatment_manage_fever(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'HighFever_less39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.no_treatment_manage_fever: got unexpected plan from when clause 1"
            with engine.prove('facts', 'DuarationMoreThanThreeDays', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.no_treatment_manage_fever: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_to_manage_fever(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'fever_protection', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_do_to_manage_fever: got unexpected plan from when clause 1"
            with engine.prove('facts', 'Cough', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_do_to_manage_fever: got unexpected plan from when clause 2"
                with engine.prove('facts', 'Dyspnea', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_do_to_manage_fever: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_do_to_manage_fever_no(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'no_fever_protection', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules.what_to_do_to_manage_fever_no: got unexpected plan from when clause 1"
            with engine.prove('facts', 'Cough', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules.what_to_do_to_manage_fever_no: got unexpected plan from when clause 2"
                with engine.prove('facts', 'Dyspnea', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules.what_to_do_to_manage_fever_no: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules')
  
  bc_rule.bc_rule('treatment_manage_fever', This_rule_base, 'fever_protection',
                  treatment_manage_fever, None,
                  (pattern.pattern_literal(True),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('no_treatment_manage_fever', This_rule_base, 'no_fever_protection',
                  no_treatment_manage_fever, None,
                  (pattern.pattern_literal(True),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_to_manage_fever', This_rule_base, 'what_to_bring',
                  what_to_do_to_manage_fever, None,
                  (pattern.pattern_literal('you_have_a_Pneumonai_and_must_take_an_ibobrofen_and_a_paracetamol_and_drink_plenty_of_fluid'),),
                  (),
                  (contexts.variable('protection'),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_do_to_manage_fever_no', This_rule_base, 'what_to_bring',
                  what_to_do_to_manage_fever_no, None,
                  (pattern.pattern_literal('you_have_a_Pneumonai_and_drink_plenty_of_fluid_and_make_fomentation'),),
                  (),
                  (contexts.variable('protection'),
                   pattern.pattern_literal(True),))


Krb_filename = '..\\bc_simple_rules.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((26, 31), (7, 7)),
    ((44, 48), (10, 10)),
    ((50, 55), (12, 12)),
    ((56, 61), (13, 13)),
    ((74, 78), (18, 18)),
    ((80, 85), (20, 20)),
    ((86, 91), (21, 21)),
    ((92, 97), (22, 22)),
    ((110, 114), (25, 25)),
    ((116, 121), (27, 27)),
    ((122, 127), (28, 28)),
    ((128, 133), (29, 29)),
)
