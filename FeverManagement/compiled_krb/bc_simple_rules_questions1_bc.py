# bc_simple_rules_questions1_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def Do_you_have_a_pneumonai(rule, arg_patterns, arg_context):
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
        with engine.prove('questions1', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions1.Do_you_have_a_pneumonai: got unexpected plan from when clause 1"
            with engine.prove('questions1', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions1.Do_you_have_a_pneumonai: got unexpected plan from when clause 2"
                with engine.prove('questions1', 'Do_you_have_a_cough', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions1.Do_you_have_a_pneumonai: got unexpected plan from when clause 3"
                    with engine.prove('questions1', 'Do_you_have_a_dyspnea', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions1.Do_you_have_a_pneumonai: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Do_you_have_a_viral(rule, arg_patterns, arg_context):
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
        with engine.prove('questions1', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions1.Do_you_have_a_viral: got unexpected plan from when clause 1"
            with engine.prove('questions1', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions1.Do_you_have_a_viral: got unexpected plan from when clause 2"
                with engine.prove('questions1', 'Do_you_have_a_common_cold', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions1.Do_you_have_a_viral: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Do_you_have_a_Tuberculosis(rule, arg_patterns, arg_context):
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
        with engine.prove('questions1', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions1.Do_you_have_a_Tuberculosis: got unexpected plan from when clause 1"
            with engine.prove('questions1', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions1.Do_you_have_a_Tuberculosis: got unexpected plan from when clause 2"
                with engine.prove('questions1', 'Do_you_have_a_haemoptysis', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions1.Do_you_have_a_Tuberculosis: got unexpected plan from when clause 3"
                    with engine.prove('questions1', 'Do_you_have_a_night_sweat', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions1.Do_you_have_a_Tuberculosis: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Do_you_have_a_tonsilitis(rule, arg_patterns, arg_context):
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
        with engine.prove('questions1', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions1.Do_you_have_a_tonsilitis: got unexpected plan from when clause 1"
            with engine.prove('questions1', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions1.Do_you_have_a_tonsilitis: got unexpected plan from when clause 2"
                with engine.prove('questions1', 'Do_you_have_a_sore_throat', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions1.Do_you_have_a_tonsilitis: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules_questions1')
  
  bc_rule.bc_rule('Do_you_have_a_pneumonai', This_rule_base, 'what_to_bring',
                  Do_you_have_a_pneumonai, None,
                  (pattern.pattern_literal('you_have_a_Pneumonai'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('Do_you_have_a_viral', This_rule_base, 'what_to_bring',
                  Do_you_have_a_viral, None,
                  (pattern.pattern_literal('you_have_a_viral'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('Do_you_have_a_Tuberculosis', This_rule_base, 'what_to_bring',
                  Do_you_have_a_Tuberculosis, None,
                  (pattern.pattern_literal('you_have_a_Tuberculosis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('Do_you_have_a_tonsilitis', This_rule_base, 'what_to_bring',
                  Do_you_have_a_tonsilitis, None,
                  (pattern.pattern_literal('you_have_a_tonsilitis'),),
                  (),
                  (pattern.pattern_literal(True),))


Krb_filename = '..\\bc_simple_rules_questions1.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((26, 31), (7, 7)),
    ((32, 37), (8, 8)),
    ((38, 43), (9, 9)),
    ((56, 60), (15, 15)),
    ((62, 67), (17, 17)),
    ((68, 73), (18, 18)),
    ((74, 79), (19, 19)),
    ((92, 96), (25, 25)),
    ((98, 103), (27, 27)),
    ((104, 109), (28, 28)),
    ((110, 115), (29, 29)),
    ((116, 121), (30, 30)),
    ((134, 138), (37, 37)),
    ((140, 145), (39, 39)),
    ((146, 151), (40, 40)),
    ((152, 157), (41, 41)),
)
