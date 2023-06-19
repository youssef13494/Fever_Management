# bc_simple_rules_questions3_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def Do_you_have_an_Urinary_tract_infection(rule, arg_patterns, arg_context):
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
        with engine.prove('questions3', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions3.Do_you_have_an_Urinary_tract_infection: got unexpected plan from when clause 1"
            with engine.prove('questions3', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions3.Do_you_have_an_Urinary_tract_infection: got unexpected plan from when clause 2"
                with engine.prove('questions3', 'Do_you_fear_the_bathroom_a_lot', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions3.Do_you_have_an_Urinary_tract_infection: got unexpected plan from when clause 3"
                    with engine.prove('questions3', 'Do_you_have_discharge_with_urine', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions3.Do_you_have_an_Urinary_tract_infection: got unexpected plan from when clause 4"
                        with engine.prove('questions3', 'Do_you_have_blood_in_your_urine', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions3.Do_you_have_an_Urinary_tract_infection: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules_questions3')
  
  bc_rule.bc_rule('Do_you_have_an_Urinary_tract_infection', This_rule_base, 'what_to_bring',
                  Do_you_have_an_Urinary_tract_infection, None,
                  (pattern.pattern_literal('you_have_an_Urinary_tract_infection'),),
                  (),
                  (pattern.pattern_literal(True),))


Krb_filename = '..\\bc_simple_rules_questions3.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((26, 31), (7, 7)),
    ((32, 37), (8, 8)),
    ((38, 43), (9, 9)),
    ((44, 49), (10, 10)),
)
