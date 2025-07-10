we need it to work when the LLM gives paths that are starting with root above CWD...

or do we.... no that's stupid cos it would lead to creating extra bad stuff.... 

ignore this.  and maybe enshrine somewhere why its important to actually not allow this.

and honestly why its important to make sure that the root of all file paths is precisely correct...  no smart looking around....


UPDATE:

this fails when replace block is empty.  i tried updating the code and it kept breaking.  real fix is probably a state machine.  or starting over from scratch.  and including tests along the way.  but for now we just need to tell the LLM that when it wants to have an empty replace block, to replace it with a blank line and a space.

https://claude.ai/chat/f107ee9a-ecbb-4338-811c-6ff07bace457
examples of how fixing failed 

state machine conversion chat:
https://claude.ai/chat/e12f85b3-b42a-4b29-b183-fd2a0b77f965