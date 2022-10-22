Doc:
Project Stracture:
there is account app :
    represnt user
    user can be courier ()
    user can be seller () = > sender
    user can be byer ()= > receiver
    user can be admin ()
the main app is base (we can split it into many small apps):

    in base we have mapping models:
        -mapping models have an idea : that we can map dynamically between fields in our app and remote couriers names .
        - we map models in courier  to our and fields in this models too .
        -we will use this mapping to understand the result from couriers and send to them excpeted format and data names .
        -there are values mapping too it will represnt fiexed  data and it's name in  couriers =
        like city , country , and services ,and others  we can use this data to not call couriers every time we need this data becouse they are almost fixed (not changing alot ).
        we must populate this data and get them from courier sites in first time only and use it after that. 
        -we can update this data with two ways :
            1-if  there is an error from courier about one of this fields that's mean there is an update and we must take it .
            2-hooks in this sites if available  , listeners  or (task run every specific time   ->this will not delete our need to first solution)




        
        - our app should have to contaian all data any courier can need (as much as possible )=> and give every courier what he need only .



get status:

    -get status have two solutions:
    -1)get status from courier when requested from user .
    -2)make hooks in courier sites like shipbox , or listen to changes in courier . 
    full solution :
    to check if there is listener of hooks in this courier 
    else get data from courier and save it  and return it to user
    in this task we will implement first solution only .
