##
* greet{"name": "Daniel"}
    - slot{"name": "Daniel"}
    - utter_greet
  
##
* greet{"name": "Miguel"}
    - slot{"name": "Miguel"}
    - utter_greet
* ask_definition
    - action_give_definition
* goodbye
    - utter_goodbye
    
##
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "Manuel"}
    - slot{"name": "Manuel"}
    - utter_nice_to_meet_you
* ask_definition
    - action_give_definition
* goodbye
    - utter_goodbye
    
##
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "João"}
    - slot{"name": "João"}
    - utter_nice_to_meet_you
* ask_law
    - action_give_law
* goodbye
    - utter_goodbye
    
##
* greet
    - utter_greet
    - utter_ask_name
* ask_law
    - utter_sad_because_you_did_not_provide_your_name
    - action_give_law
* goodbye
    - utter_goodbye
* ask_definition
    - utter_thought_you_were_gone
    - action_give_definition
* goodbye
    - utter_goodbye
    
##
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "Manuel"}
    - slot{"name": "Manuel"}
    - utter_nice_to_meet_you
* ask_definition
    - action_give_definition
* greet
    - utter_greet_again
* goodbye
    - utter_goodbye
    
##
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "Manuel"}
    - slot{"name": "Manuel"}
    - utter_nice_to_meet_you
* greet
    - utter_greet_again
* ask_definition
    - action_give_definition
* goodbye
    - utter_goodbye

##
* greet
    - utter_greet
    - utter_ask_name
* greet
    - utter_sad_because_you_did_not_provide_your_name
    - utter_happy

##
* greet
    - utter_greet
    - utter_ask_name
* affirm
    - utter_sad_because_you_did_not_provide_your_name
    - utter_happy

##
* greet
    - utter_greet
    - utter_ask_name
* deny
    - utter_sad_because_you_did_not_provide_your_name
    - utter_goodbye

##
* goodbye
    - utter_goodbye
  
##
* greet
    - utter_greet
    - utter_ask_name
* ask_definition
    - utter_sad_because_you_did_not_provide_your_name
    - action_give_definition

##
* greet
    - utter_greet
    - utter_ask_name
* ask_definition
    - utter_sad_because_you_did_not_provide_your_name
    - action_give_definition
* goodbye
    - utter_goodbye
    
##
* ask_definition
    - action_give_definition
* goodbye
    - utter_goodbye

##
* greet
    - utter_greet
    - utter_ask_name
* ask_law
    - utter_sad_because_you_did_not_provide_your_name
    - action_give_law
    
##
* ask_law
    - action_give_law
    
##
* ask_who_are_you
    - utter_who_i_am
  
##
* greet
    - utter_greet
    - utter_ask_name
* ask_who_are_you
    - utter_who_i_am
* goodbye
    - utter_goodbye
    
##
* greet{"name": "Miguel"}
    - slot{"name": "Miguel"}
    - utter_greet
* ask_definition
    - action_give_definition
* insult
    - utter_you_are_rude
    - utter_goodbye
    
##
* greet
    - utter_greet
    - utter_ask_name
* ask_who_are_you
    - utter_who_i_am
* insult
    - utter_you_are_rude
* goodbye
    - utter_goodbye
 
##
 * insult
    - utter_you_are_rude
    
##
 * insult
    - utter_you_are_rude
 * affirm
    - utter_apologize
    
##
 * insult
    - utter_you_are_rude
 * deny
    - utter_happy
    
##
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "Corceiro"}
    - slot{"name": "Corceiro"}
    - utter_nice_to_meet_you
* ask_who_are_you
    - utter_who_i_am
* insult
    - utter_you_are_rude
* affirm
    - utter_apologize
* goodbye
    - utter_goodbye
    
##
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "Narciso"}
    - slot{"name": "Narciso"}
    - utter_nice_to_meet_you
* ask_who_are_you
    - utter_who_i_am
* insult
    - utter_you_are_rude
* deny
    - utter_happy
* goodbye
    - utter_goodbye
    
##
* greet{"name": "Miguel"}
    - slot{"name": "Miguel"}
    - utter_greet
* ask_definition
    - action_give_definition
* insult
    - utter_you_are_rude
    - utter_goodbye
* ask_joke
    - utter_joke
    - utter_one_more
* affirm
    - utter_joke
    - utter_one_more
* deny


##
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "Sónia"}
    - slot{"name": "Sónia"}
    - utter_nice_to_meet_you
* ask_who_are_you
    - utter_who_i_am
* ask_joke
    - utter_joke
    - utter_one_more
* deny
* goodbye
    - utter_goodbye
    
##
* ask_joke
    - utter_greet
    - utter_joke
    - utter_one_more
* deny

##
* ask_joke
    - utter_greet
    - utter_joke
    - utter_one_more
* affirm
    - utter_joke
    - utter_ask_name
* tell_name{"name": "Teresa"}
    - slot{"name": "Teresa"}
    - utter_nice_to_meet_you
    
##
* greet
    - utter_greet
    - utter_ask_name
* ask_joke
    - utter_joke
    - utter_one_more
* deny
* goodbye
    - utter_goodbye
    
##
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "Cristina"}
    - slot{"name": "Cristina"}
    - utter_nice_to_meet_you
* ask_joke
    - utter_joke
    - utter_one_more
* deny
* insult
    - utter_you_are_rude
* ask_law
    - action_give_law
## Generated Story -1396719676658644124
* greet
    - utter_greet
    - utter_ask_name
* greet
    - utter_sad_because_you_did_not_provide_your_name
    - utter_greet
* greet
    - utter_greet_again
* ask_definition
    - action_give_definition
* ask_who_are_you
    - utter_who_i_am
* ask_law{"article": "34", "concept": "c\u00f3digo c\u00edvil"}
    - action_give_law
* ask_law{"number": "4", "article": "5", "concept": "c\u00f3digo civil"}
    - action_give_law
* ask_law{"article": "23", "concept": "constitui\u00e7\u00e3o da r\u00e9publica"}
    - action_give_law
* tell_name{"name": "Daniel"}
    - slot{"name": "Daniel"}
    - utter_nice_to_meet_you
* affirm
    - utter_not_understand
* ask_definition{"concept": "humano"}
    - utter_who_i_am
* ask_who_are_you{"concept": "cebola"}
    - action_give_definition
    - utter_who_i_am
* ask_who_are_you{"concept": "gato"}
    - action_give_definition
    - utter_who_i_am
* goodbye
    - utter_goodbye

## Generated Story -3916429016676665978
* greet
    - utter_greet
    - utter_ask_name
* deny
    - utter_sad_because_you_did_not_provide_your_name
* ask_who_are_you
    - utter_who_i_am
* ask_who_are_you
    - utter_who_i_am
* ask_who_are_you{"concept": "gato"}
    - action_give_definition
    - utter_who_i_am
* ask_law{"article": "87", "concept": "constitui\u00e7\u00e3o da r\u00e9publica"}
    - action_give_law
* ask_am_i_pretty
    - utter_you_are_beautiful
* ask_who_are_you{"concept": "cebola"}
    - action_give_definition
    - utter_who_i_am
* ask_who_are_you
    - utter_who_i_am
* ask_definition{"concept": "coisa"}
    - action_give_definition
* insult
    - utter_you_are_rude
* i_am_happy
    - utter_happy
* ask_who_are_you
    - utter_who_i_am
* ask_who_are_you{"concept": "humano"}
    - action_give_definition
    - utter_who_i_am
* ask_who_are_you
    - action_give_definition
    - utter_who_i_am
    
## Generated Story -4660963887069261977
* greet
    - utter_greet
    - utter_ask_name
* tell_name{"name": "Daniel"}
    - slot{"name": "Daniel"}
    - utter_nice_to_meet_you
* ask_who_are_you{"concept": "humano"}
    - action_give_definition
    - utter_who_i_am
* ask_who_are_you{"concept": "cebola"}
    - action_give_definition
    - utter_who_i_am
* ask_law{"article": "57", "concept": "consitui\u00e7\u00e3o portuguesa"}
    - action_give_law
* ask_am_i_pretty
    - utter_you_are_beautiful
* ask_joke
    - utter_joke
    - utter_one_more
* ask_joke
    - utter_joke
    - utter_one_more
* ask_age
    - utter_age
    
## Generated Story -179324983298317263
* greet
    - utter_greet
    - utter_ask_name
* ask_law{"name": "Daniel", "article": "46", "concept": "c\u00f3digo c\u00edvil"}
    - slot{"name": "Daniel"}
    - utter_nice_to_meet_you
    - action_give_law
* affirm
    - action_default_fallback
    - rewind
* ask_who_are_you
    - utter_who_i_am
* ask_who_are_you{"concept": "cebola"}
    - action_give_definition
    - utter_who_i_am
* ask_am_i_pretty
    - utter_you_are_beautiful
* ask_joke
    - utter_joke
    - utter_one_more
* deny
    - action_default_fallback
    - rewind
* ask_definition{"concept": "c\u00f3digo c\u00edvil"}
    - action_give_definition
* where_were_you_born
    - utter_i_was_not_born
    - utter_my_creators

## Generated Story -2608403271420667929
* greet
    - utter_greet
    - utter_ask_name
* ask_law{"concept": "c\u00f3digo c\u00edvil", "article": "45"}
    - action_give_law
* where_were_you_born
    - utter_i_was_not_born
    - utter_my_creators
* ask_who_created_you
    - utter_my_creators
* ask_who_are_you
    - utter_who_i_am
* ask_who_are_you{"concept": "humano"}
    - action_give_definition
    - utter_who_i_am
* i_am_happy
    - action_default_fallback
    - rewind
* ask_law{"article": "56", "concept": "c\u00f3digo c\u00edvil"}
    - action_give_law
* ask_law{"article": "87", "concept": "constitui\u00e7\u00e3o da r\u00e9publica"}
    - action_give_law
* ask_definition{"concept": "humano"}
    - action_give_definition
* thank_you
    - action_default_fallback
    - rewind
* goodbye
    - utter_goodbye
* greet
    - utter_thought_you_were_gone
    - utter_greet

