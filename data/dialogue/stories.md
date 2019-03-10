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
* custom_answer_1
	- utter_custom_answer_1
