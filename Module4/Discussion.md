## Module 4 - Discussion

What are the key constructs required to create a loop? Identify two scenarios that may require two different types of loops. Be sure to provide specific details for each scenario that illustrate why the different types of loops are required. Include a brief pseudocode example to share that includes at least one loop. Actively participate in this discussion by providing constructive feedback on the scenarios and details posted by your peers.


## Answer

The key constructs requried to create a loop are:

1. Defining the control variable(s) used to create entry/exit condition which is checked/updated each time the loop executes
2. Defining the specific actions that execute each time a loop repeats
3. Defining an appropriate Boolean expression that determines if the loop will be entered
4. Defining an appropriate Boolean expression that determines when the loop will stop


I'm currently working on a project that is ingesting massive amounts of documents. A while loop is used for a couple of our chunking strategies (for example simple chunking and simple chunking with overlap).

For my simple chunking strategy a while loop is used because we do not know the number of repetitions needed to chunk the document when starting the loop. The entry point and exit point for the loop is determined by the current start position and whether or not are end position is > doc.length. 

```
int start = 0;
int end = 0;
```

