# Module 7: Discussion Forum

Working with Python, you could either use a predefined function/method or write a user-defined function/method. What are three criteria that you would use to determine whether to use predefined or user-defined functions/methods? Discuss your rationale in your post. Lastly, provide an example of your method declaration and return type. Actively participate in this discussion by providing constructive feedback and/or justifications on the criteria, rationales, and examples posted by your peers.

*Be sure to post an initial, substantive response by Thursday at 11:59 p.m. MT, and respond to two or more classmates or the instructor with substantive responses by Sunday at 11:59 p.m. MT.*

***A substantive initial post** answers the question presented completely and/or asks a thoughtful question pertaining to the topic. Be sure your post is unique. Do not repeat what other students have said.*

***Substantive peer responses** ask thoughtful questions pertaining to the topic, and/or answer a question (in detail) posted by another student or the instructor. Note: The following are not examples of substantive contributions:*

- *Thanking, agreeing with, or complimenting a classmate.*
- *Providing irrelevant commentary.*

## Answer
3 citeria I would use to determine wheter to use predefined or user-defined functions/methods are
1. If a predefined function already completes the task I'm trying to accomplish then I'd use it instead of writing my own. The predefined code here is proven and quick to understand.
2. If I have logic that will be repeated and there is no predefined function then I'd create my own function. My own function keeps the code clean by cutting out copy/pasta and helps keep the code easy to maintain.
3. If a predefined function already completes the task but I need to extend it with logging and/or exception handling then I'd create my own function with addtional logic around the predefined function. This allows me to use predefined functions (reasons in #1) and enhance the functionality.

Example of extending sum with logging
def sum_and_log(values) -> float:
    total = sum(values)
    print(f"Sum = {total}")
    return total