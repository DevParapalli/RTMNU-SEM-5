# P7_ProductionSystem Notes

- <https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/resources/lab1/>

## Family Relations

```text
This problem seems easy enough on the top of my head, dont know how it will work out.
```

You will be given data that includes three kinds of statements:

- `male x`: x is male
- `female x`: x is female
- `x parent y`: x is a parent of y

Every person in the data set will be defined to be either male or female. Your task is to deduce, wherever you can, the following relations:

- `x brother y`: x is the brother of y (sharing at least one parent)
- `x sister y`: x is the sister of y (sharing at least one parent)
- `x mother y`: x is the mother of y
- `x father y`: x is the father of y
- `x son y`: x is the son of y
- `x daughter y`: x is the daughter of y
- `can we ignore the following?`
- `x cousin y`: x and y are cousins (a parent of x and a parent of y are siblings)
- `x grandparent y`: x is the grandparent of y
- `x grandchild y`: x is the grandchild of y

You will probably run into the problem that the system wants to conclude that everyone is his or her own sibling. To avoid this, you will probably want to write a rule that adds `same-identity (?x) (?x)` for every person, and make sure that potential siblings don't have the same-identity. (Hint: You can assume that every person will be mentioned in a clause stating his gender (either male or female)). The order of the rules will matter, of course. Note that it's fine to include statements that are not any of the specified relations (such as `same-identity` or `sibling`).

Some relationships are symmetrical, and you need to include them both ways. For example, if a is a cousin of b, then b is a cousin of a.
