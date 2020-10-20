#!/usr/bin/env python3

#The following is a fun excercise in designing a simple madlibs program in python.  Albeit longer than a short phrase.  I chose a longer shakespearian madlib as a challenge.  Feel free to copy the code into an interpreter.  It's somewhat fun.

adjective = input("Please name an adjective: ")
celebrity = input("Please name a celebrity: ")
Noun_1 = input("Please enter a noun: ")
Noun_2 = input("Please enter a different noun: ")
Noun_3 = input("Please enter a different noun: ")
Noun_4 = input("Please enter a different noun: ")
Plural_noun_1 = input("Please enter a plural Noun: ")
Plural_noun_2 = input("Please enter a different plural noun: ")
Plural_noun_3 = input("Please enter a different plural noun: ")
Plural_noun_4 = input("Please enter a different plural noun: ")
Type_of_liquid = input("Please enter a type of liquid: ")
Verb_1 = input("Please enter a verb: ")
Verb_2 = input("Please enter a different verb: ")
Verb_3 = input("Please enter a different verb: ")

print("This is a soliloquoy from the play 'Hamlet,' written by " + celebrity + ". In the third act of this " + adjective + " play, Hamlet, who is sometimes called 'the melancholy " + Noun_1 + ",' is suspicious of his stepfather and hires some actors to act out a scene in which a king is killed when someone pours " + Type_of_liquid + " into his " + Noun_2 + ". First, however he declaims: To be or not to be: that is the " + Noun_3 + ": Whether 'tis nobler in the mind to suffer the " + Plural_noun_1 + " and " + Plural_noun_2 + " of outrageous fortune, or to take arms against a sea of " + Plural_noun_3 + ", and by opposing end them. To die: to sleep; no more; and by a sleep to say we end the heartache and the thousand natural " + Plural_noun_4 + " that flesh is heir to, 'tis a consumation devoutly to be wish'd. To die, to " + Verb_1 + "; to " + Verb_2 + ": perchance to " + Verb_3 + ": ay, there's the " + Noun_4 + ".") 
