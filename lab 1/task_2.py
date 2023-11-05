# TODO Найдите количество книг, которое можно разместить на дискете

_buffer = 1.44
_bookPages = 100
_linesInPage = 50
_simbolsInLine = 25
_symbolWeight = 4


print("Количество книг, помещающихся на дискету:",
      int(
          (_buffer*1024*1024)/
          (_bookPages * _linesInPage * _simbolsInLine * _symbolWeight)
      )
  )
