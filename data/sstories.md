## happy path for the four questions
* greet
  - utter_greet
  - utter_get_informed_consent
  <!-- ask if they've been here before -->
  - first_time_form
  - form{"name": "first_time_form"}
  - form{"name": null}
  - utter_set_expectations
  <!-- some kind of conversation happen here -->
* ask_four_language_questions
  - utter_introduce_survey
  - language_questions_form
  - form{"name": "language_questions_form"}
  - form{"name": null}
  <!-- more conversation -->
  - utter_anything_else_question
* goodbye
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - utter_goodbye

## unhappy path for the four questions
* greet
  - utter_greet
  - utter_get_informed_consent
  <!-- ask if they've been here before -->
  - first_time_form
  - form{"name": "first_time_form"}
  - slot{"requested_slot": "given_name"}
* deny
  - utter_greet
  - first_time_form
  - slot{"given_name": null}
  - form{"name": null}
  - utter_set_expectations
* ask_four_language_questions
  - utter_introduce_survey
  - language_questions_form
  - form{"name": "language_questions_form"}
  - form{"name": null}
  <!-- more conversation -->
  - utter_anything_else_question
* goodbye
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - utter_goodbye

## happy path for statistics
* ask_for_stats
  - action_get_infection_stats
  -utter_anything_else_question

## unhappy path for out of scope
  - utter_out_of_scope
  - utter_get_back_on_topic

## answercovid_myth_cure
* covid_myth_cure
 - utter_answer_covid_myth_cure

## answercovid_myth_antibiotics
* covid_myth_antibiotics
 - utter_answer_covid_myth_antibiotics

## answercovid_myth_garlic
* covid_myth_garlic
 - utter_answer_covid_myth_garlic
 - myth_source_form
 - form{"name": "myth_source_form"}
 - form{"name": null}
 - utter_anything_else_question
* goodbye
   - feedback_form
   - form{"name": "feedback_form"}
   - form{"name": null}
   - utter_goodbye

## answercovid_explain_pandemic
* covid_explain_pandemic
 - utter_explain_pandemic3
 - action_link_to_pandemic_video

## answercovid_myth_saline_rinse
* covid_myth_saline_rinse
 - utter_answer_covid_myth_saline_rinse

## answercovid_myth_other_vaccines
* covid_myth_other_vaccines
 - utter_answer_covid_myth_other_vaccines

## answercovid_myth_alcohol_chlorine
* covid_myth_alcohol_chlorine
 - utter_answer_covid_myth_alcohol_chlorine

## answercovid_myth_thermal_scanners
* covid_myth_thermal_scanners
 - utter_answer_covid_myth_thermal_scanners

## answercovid_myth_UV
* covid_myth_UV
 - utter_answer_covid_myth_UV

## answercovid_myth_hand_dryers
* covid_myth_hand_dryers
 - utter_answer_covid_myth_hand_dryers

## answercovid_myth_hot_bath
* covid_myth_hot_bath
 - utter_answer_covid_myth_hot_bath

## answercovid_myth_pets
* covid_myth_pets
 - utter_answer_covid_myth_pets

## answercovid_myth_mosquitos
* covid_myth_mosquitos
 - utter_answer_covid_myth_mosquitos

## answercovid_myth_heat_kills
* covid_myth_heat_kills
 - utter_answer_covid_myth_heat_kills

## answercovid_myth_cold_kills
* covid_myth_cold_kills
 - utter_answer_covid_myth_cold_kills

## answercovid_myth_only_old
* covid_myth_only_old
 - utter_answer_covid_myth_only_old

## answercovid_children_stress
* covid_children_stress
 - utter_answer_covid_children_stress

## answercovid_stress
* covid_stress
 - utter_answer_covid_stress

## answercovid_donate
* covid_donate
 - utter_answer_covid_donate

## answercovid_travel_advice
* covid_travel_advice
 - utter_answer_covid_travel_advice

## answercovid_myths_summary
* covid_myths_summary
 - utter_answer_covid_myths_summary

## answercovid_donts
* covid_donts
 - utter_answer_covid_donts

## answercovid_on_surfaces
* covid_on_surfaces
 - utter_answer_covid_on_surfaces

## answercovid_infection_sources
* covid_infection_sources
 - utter_answer_covid_infection_sources

## answercovid_incubation
* covid_incubation
 - utter_answer_covid_incubation

## answercovid_masks
* covid_masks
 - utter_answer_covid_masks

## answercovid_SARS
* covid_SARS
 - utter_answer_covid_SARS

## answercovid_treatments
* covid_treatments
 - utter_answer_covid_treatments

## answercovid_most_at_risk
* covid_most_at_risk
 - utter_answer_covid_most_at_risk

## answercovid_anxiety
* covid_anxiety
 - utter_answer_covid_anxiety

## answercovid_infection_likelihood
* covid_infection_likelihood
 - utter_answer_covid_infection_likelihood

## answercovid_protection
* covid_protection
 - utter_answer_covid_protection

## answercovid_how_spread
* covid_how_spread
 - utter_answer_covid_how_spread

## answercovid_what_is_corona_covid-19
* covid_what_is_corona_covid-19
 - utter_answer_covid_what_is_corona_covid-19

## answercovid_symptoms
* covid_symptoms
 - utter_answer_covid_symptoms

## answerwash_hands_how
* wash_hands_how
 - utter_answer_wash_hands_how

## answerwash_hands_frequency
* wash_hands_frequency
 - utter_answer_wash_hands_frequency

## answer_out_of_scope
* out_of_scope
 - utter_out_of_scope

## answerfallback
* fallback
 - utter_answer_fallback

<!-- ## answergoodbye
* goodbye
 - utter_answer_goodbye -->

## answergreeting
* greet
 - utter_answer_greeting
 - utter_get_informed_consent
 - utter_set_expectations
