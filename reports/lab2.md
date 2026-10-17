The expression grammar and design choices are all pretty similar to Lox except for a couple of things.
1) true and false are capitalized
2) I added postfix and logical expressions 
3) I added increment and decrement

All you need to do to replicate the printer tests is do "python3 test[num].py" and replace [num] with 1, 2, 3, or 4. I did include an ast printer and to run it you need to do "python3 generateAST" with an underline between generate and AST. To regenerate the expression classes you need to edit define ast in main and add a class.

Test case 1 is for all arithmic operations. 
Both expected and printer outputs match: (/ (group (- (+ 523.0 12.0) (* 53.0 2.0))) 2.0) 

Test case 2 is for most literals and all comparisons and logic
Both expected and printer outputs match: (|| (|| (&& (< 1.0 2.0) (<= 3.0 4.0)) (&& (> 5.0 6.0) (>= 7.0 8.0))) (&& (! (group (== True False))) (!= False True)))

Test case 3 is for null and strings
Both expected and printer outputs match: (!= guava null)

Test case 4 is for postfix as well as the ++ and -- operators
Both expected and printer outputs match: (* (group (+ (++ 1.0) (post++ 2.0))) (group (- (-- 3.0) (post-- 4.0))))

I don't believe there is any limitations or failed tests.
