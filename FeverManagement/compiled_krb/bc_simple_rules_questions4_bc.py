# bc_simple_rules_questions4_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def Do_you_have_a_meningitis(rule, arg_patterns, arg_context):
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
        with engine.prove('questions4', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions4.Do_you_have_a_meningitis: got unexpected plan from when clause 1"
            with engine.prove('questions4', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions4.Do_you_have_a_meningitis: got unexpected plan from when clause 2"
                with engine.prove('questions4', 'Do_you_have_a_pain_in_the_neck', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions4.Do_you_have_a_meningitis: got unexpected plan from when clause 3"
                    with engine.prove('questions4', 'Is_your_neck_tight', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions4.Do_you_have_a_meningitis: got unexpected plan from when clause 4"
                        with engine.prove('questions4', 'Do_you_suffer_from_vomitting', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions4.Do_you_have_a_meningitis: got unexpected plan from when clause 5"
                            with engine.prove('questions4', 'Do_you_suffer_from_severe_headaches', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules_questions4.Do_you_have_a_meningitis: got unexpected plan from when clause 6"
                                with engine.prove('questions4', 'Do_you_suffer_from_High_fever', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "bc_simple_rules_questions4.Do_you_have_a_meningitis: got unexpected plan from when clause 7"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Do_you_have_a_hepatisis(rule, arg_patterns, arg_context):
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
        with engine.prove('questions4', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions4.Do_you_have_a_hepatisis: got unexpected plan from when clause 1"
            with engine.prove('questions4', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions4.Do_you_have_a_hepatisis: got unexpected plan from when clause 2"
                with engine.prove('questions4', 'Do_you_suffer_from_jaundice', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions4.Do_you_have_a_hepatisis: got unexpected plan from when clause 3"
                    with engine.prove('questions4', 'Do_you_suffer_from_naseua', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions4.Do_you_have_a_hepatisis: got unexpected plan from when clause 4"
                        with engine.prove('questions4', 'Do_you_suffer_from_Pain_in_the_right_part_of_the_abdomen', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions4.Do_you_have_a_hepatisis: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Do_you_have_a_malignancy(rule, arg_patterns, arg_context):
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
        with engine.prove('questions4', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions4.Do_you_have_a_malignancy: got unexpected plan from when clause 1"
            with engine.prove('questions4', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions4.Do_you_have_a_malignancy: got unexpected plan from when clause 2"
                with engine.prove('questions4', 'Do_you_lose_weight', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions4.Do_you_have_a_malignancy: got unexpected plan from when clause 3"
                    with engine.prove('questions4', 'Are_you_tired', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions4.Do_you_have_a_malignancy: got unexpected plan from when clause 4"
                        with engine.prove('questions4', 'Do_you_have_a_night_sweat', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions4.Do_you_have_a_malignancy: got unexpected plan from when clause 5"
                            with engine.prove('questions4', 'Do_you_suffer_from_lymph_denopathy', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc_simple_rules_questions4.Do_you_have_a_malignancy: got unexpected plan from when clause 6"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Do_you_have_a_ear_pain(rule, arg_patterns, arg_context):
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
        with engine.prove('questions4', 'Is_your_temperature_higher_than_39', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_simple_rules_questions4.Do_you_have_a_ear_pain: got unexpected plan from when clause 1"
            with engine.prove('questions4', 'Is_the_duration_of_the_fever_more_than_3_days', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_simple_rules_questions4.Do_you_have_a_ear_pain: got unexpected plan from when clause 2"
                with engine.prove('questions4', 'Do_you_have_discharge_from_ear', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc_simple_rules_questions4.Do_you_have_a_ear_pain: got unexpected plan from when clause 3"
                    with engine.prove('questions4', 'Do_you_have_ear_swelling', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc_simple_rules_questions4.Do_you_have_a_ear_pain: got unexpected plan from when clause 4"
                        with engine.prove('questions4', 'Is_your_hearing_decreased', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc_simple_rules_questions4.Do_you_have_a_ear_pain: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_simple_rules_questions4')
  
  bc_rule.bc_rule('Do_you_have_a_meningitis', This_rule_base, 'what_to_bring',
                  Do_you_have_a_meningitis, None,
                  (pattern.pattern_literal('you_have_a_meningitisn'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('Do_you_have_a_hepatisis', This_rule_base, 'what_to_bring',
                  Do_you_have_a_hepatisis, None,
                  (pattern.pattern_literal('you_have_a_hepatisis'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('Do_you_have_a_malignancy', This_rule_base, 'what_to_bring',
                  Do_you_have_a_malignancy, None,
                  (pattern.pattern_literal('you_have_a_malignancy'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('Do_you_have_a_ear_pain', This_rule_base, 'what_to_bring',
                  Do_you_have_a_ear_pain, None,
                  (pattern.pattern_literal('you_have_a_otitis'),),
                  (),
                  (pattern.pattern_literal(True),))


Krb_filename = '..\\bc_simple_rules_questions4.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((26, 31), (7, 7)),
    ((32, 37), (8, 8)),
    ((38, 43), (9, 9)),
    ((44, 49), (10, 10)),
    ((50, 55), (11, 11)),
    ((56, 61), (12, 12)),
    ((74, 78), (19, 19)),
    ((80, 85), (21, 21)),
    ((86, 91), (22, 22)),
    ((92, 97), (23, 23)),
    ((98, 103), (24, 24)),
    ((104, 109), (25, 25)),
    ((122, 126), (30, 30)),
    ((128, 133), (32, 32)),
    ((134, 139), (33, 33)),
    ((140, 145), (34, 34)),
    ((146, 151), (35, 35)),
    ((152, 157), (36, 36)),
    ((158, 163), (37, 37)),
    ((176, 180), (40, 40)),
    ((182, 187), (42, 42)),
    ((188, 193), (43, 43)),
    ((194, 199), (44, 44)),
    ((200, 205), (45, 45)),
    ((206, 211), (46, 46)),
)
