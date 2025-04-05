# Output Expirements

## 3.1 Data Types
While going through 3.1 Data Types I noticed that some of the output syntax seemed to be a bit off :)

### Example of incorrect output
1. The `String` data type says `Output: Welcome To Python`.
    ``` python
    # copy of code from 3.1 DataTypes String
    String
    Example:
    String1 = "Welcome"
    String2 ="To Python"
    print(String1+String2)
    Output: Welcome To Python
    ```
    Based on `String1` and `String2` value and because the above print statement has `+` instead of `,` the output for the above should be: **`WelcomeTo Pyton`**.

    If want the output to match expected here `Welcome To Python` we could do one of the following:
        
    1. Update print statement to `print(String1, String2)`
    2. Update print statement to `print(String1 + ' ' + String2)`

2. The `Tuple` data type says `Output: Tuple[1] = 15`
    ``` python
    # copy of code from 3.1 DataTypes Tuple
    Example:
    Tuple = (50,15,25.6,"Python")
    print("Tuple[1] = ", Tuple[1])
    Output: Tuple[1] = 15
    ```

    Based on `print` statement having a `space` before the comma the output for the above should be: **`Tuple[1] =  15'** with 2 spaces

    HA! Looking at the render for the above statement **`Tuple[1] =  15'** there is only 1 space :). I think that means the output is probably correct but html (and markdown here is not preserving the whitespace).

    We'd need need to use `&nbsp;`. So output for example code above would actually be Tuple[1] =&nbsp;&nbsp;15. <-- I'm not able to wrap this in backticks and display correctly.

    I think we can put it in a codeblock though to format better and show
    ```
    Output: Tuple[1] =  15
    ```

    That was a fun one!!

    If we want the output to match expected here `Tuple[1] = 15` we could do the following:

    1. Update print statement to `print("Tuple[1] =", Tuple[1])`

3. The `Set` example sent me down a rabbit hole a bit. At first when I saw this I was confused by the output order of the set. I understand that a `Set` is an unordered list however no matter how many times I run this example it always prints in the same order :)
    
    3.3: Set Basics does make a specific call out that because sets are unordered the order output could differ. However even running 3.3.1 over and over the output was always in the same sequence.

    After reviewing the reading a bit more and doing some independent research I believe the reason printing of the set is always in the same order is due to the hash that is used. I started to try and see if I could "alter" the hash to force the sequence to change but ended up abandoning this. For now I just have faith that the sequence of the output is random. I will at some point in the future when I have more time figure out a good way to prove this though :)