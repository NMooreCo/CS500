# Module 5: Discussion Forum

Briefly describe how both the and & or operators work. Include a brief pseudocode example of both. In response to your peers, provide additional code examples and constructive feedback on the rationale posted by your peers.

Be sure to post an initial, substantive response by Thursday at 11:59 p.m. MT, and respond to two or more classmates or the instructor with substantive responses by Sunday at 11:59 p.m. MT.

**A substantive initial post** answers the question presented completely and/or asks a thoughtful question pertaining to the topic. Be sure your post is unique. Do not repeat what other students have said.

**Substantive peer responses** ask thoughtful questions pertaining to the topic, and/or answer a question (in detail) posted by another student or the instructor. Note: The following are not examples of substantive contributions:
- Thanking, agreeing with, or complimenting a classmate.
- Providing irrelevant commentary.

## Answer

The `and` operator is used to return true when both operands on either side are true (a and b will return true when both a AND b = true)

The `or` operator is used to return true when as least one operand on either side is true (a or b will return true when either a OR b = true)

### And Example:
I want to pickup the Switch 2. I can only pickup the Switch 2 if todays date is at least launch date AND I've preordered.

``` python
import datetime
def pickup_switch2(todays_date, preordered):
    switch_release_date = datetime.datetime(2025, 6, 2)
    return (todays_date >= switch_release_date) and preordered
```

### Or Example:
It is possible though that even if I didn't pre order the switch that I could get lucky and be able to get one. For instance if I didn't preorder but one happens to be in stock

``` python
import datetime
def pickup_switch2(todays_date, preordered):
    extra_in_stock = True # in this example we are always lucky and there is switch2 in stock
    switch_release_date = datetime.datetime(2025, 6, 2)
    return (todays_date >= switch_release_date) and (preordered or extra_in_stock)
```