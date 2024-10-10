\* Books to boxes Test *\
\* Run using: glpsol --lp booksToBoxesTest.lp -o booksToBoxes.txt *\
\* Answer report will be in booksToBoxes.txt *\


Maximize
profit: 1 SmallB1 + 1 SmallMidB1 + 1 MediumB1 + 1 MidLargeB1 + 1 LargeB1

subject to
WeightB1: .5 SmallB1 + 1 SmallMidB1 + 1.5 MediumB1 + 2 MidLargeB1 + 2.5 LargeB1 <= 400
VolumeB1: 100 SmallB1 + 200 SmallMidB1 + 300 MediumB1 + 400 MidLargeB1 + 500 LargeB1 <= 1875
SmallBooks: 1 SmallB1 + 0 SmallMidB1 + 0 MediumB1 + 0 MidLargeB1 + 0 LargeB1 = 1
SmallMidBooks: 0 SmallB1 + 1 SmallMidB1 + 0 MediumB1 + 0 MidLargeB1 + 0 LargeB1 = 1
MediumBooks: 0 SmallB1 + 0 SmallMidB1 + 1 MediumB1 + 0 MidLargeB1 + 0 LargeB1 = 1
MidLargeBooks: 0 SmallB1 + 0 SmallMidB1 + 0 MediumB1 + 1 MidLargeB1 + 0 LargeB1 = 1
LargeBooks: 0 SmallB1 + 0 SmallMidB1 + 0 MediumB1 + 0 MidLargeB1 + 1 LargeB1 = 1

Integer
SmallB1
SmallMidB1
MediumB1
MidLargeB1
LargeB1

End
