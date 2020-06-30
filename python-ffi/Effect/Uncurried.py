
def mkEffectFn1(fn):
  def _mkEffectFn1 (_0):
    return fn(_0)()
  return _mkEffectFn1


def mkEffectFn2(fn):
  def _mkEffectFn2 (_0,_1):
    return fn(_0)(_1)()
  return _mkEffectFn2


def mkEffectFn3(fn):
  def _mkEffectFn3 (_0,_1,_2):
    return fn(_0)(_1)(_2)()
  return _mkEffectFn3


def mkEffectFn4(fn):
  def _mkEffectFn4 (_0,_1,_2,_3):
    return fn(_0)(_1)(_2)(_3)()
  return _mkEffectFn4


def mkEffectFn5(fn):
  def _mkEffectFn5 (_0,_1,_2,_3,_4):
    return fn(_0)(_1)(_2)(_3)(_4)()
  return _mkEffectFn5


def mkEffectFn6(fn):
  def _mkEffectFn6 (_0,_1,_2,_3,_4,_5):
    return fn(_0)(_1)(_2)(_3)(_4)(_5)()
  return _mkEffectFn6


def mkEffectFn7(fn):
  def _mkEffectFn7 (_0,_1,_2,_3,_4,_5,_6):
    return fn(_0)(_1)(_2)(_3)(_4)(_5)(_6)()
  return _mkEffectFn7


def mkEffectFn8(fn):
  def _mkEffectFn8 (_0,_1,_2,_3,_4,_5,_6,_7):
    return fn(_0)(_1)(_2)(_3)(_4)(_5)(_6)(_7)()
  return _mkEffectFn8


def mkEffectFn9(fn):
  def _mkEffectFn9 (_0,_1,_2,_3,_4,_5,_6,_7,_8):
    return fn(_0)(_1)(_2)(_3)(_4)(_5)(_6)(_7)(_8)()
  return _mkEffectFn9


def mkEffectFn10(fn):
  def _mkEffectFn10 (_0,_1,_2,_3,_4,_5,_6,_7,_8,_9):
    return fn(_0)(_1)(_2)(_3)(_4)(_5)(_6)(_7)(_8)(_9)()
  return _mkEffectFn10


def runEffectFn1(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2():
      return fn(_1)
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn2(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3():
        return fn(_1,_2)
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn3(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3(_3):
        def _runEffectFn4():
          return fn(_1,_2,_3)
        return _runEffectFn4
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn4(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3(_3):
        def _runEffectFn4(_4):
          def _runEffectFn5():
            return fn(_1,_2,_3,_4)
          return _runEffectFn5
        return _runEffectFn4
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn5(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3(_3):
        def _runEffectFn4(_4):
          def _runEffectFn5(_5):
            def _runEffectFn6():
              return fn(_1,_2,_3,_4,_5)
            return _runEffectFn6
          return _runEffectFn5
        return _runEffectFn4
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn6(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3(_3):
        def _runEffectFn4(_4):
          def _runEffectFn5(_5):
            def _runEffectFn6(_6):
              def _runEffectFn7():
                return fn(_1,_2,_3,_4,_5,_6)
              return _runEffectFn7
            return _runEffectFn6
          return _runEffectFn5
        return _runEffectFn4
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn7(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3(_3):
        def _runEffectFn4(_4):
          def _runEffectFn5(_5):
            def _runEffectFn6(_6):
              def _runEffectFn7(_7):
                def _runEffectFn8():
                  return fn(_1,_2,_3,_4,_5,_6,_7)
                return _runEffectFn8
              return _runEffectFn7
            return _runEffectFn6
          return _runEffectFn5
        return _runEffectFn4
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn8(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3(_3):
        def _runEffectFn4(_4):
          def _runEffectFn5(_5):
            def _runEffectFn6(_6):
              def _runEffectFn7(_7):
                def _runEffectFn8(_8):
                  def _runEffectFn9():
                    return fn(_1,_2,_3,_4,_5,_6,_7,_8)
                  return _runEffectFn9
                return _runEffectFn8
              return _runEffectFn7
            return _runEffectFn6
          return _runEffectFn5
        return _runEffectFn4
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn9(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3(_3):
        def _runEffectFn4(_4):
          def _runEffectFn5(_5):
            def _runEffectFn6(_6):
              def _runEffectFn7(_7):
                def _runEffectFn8(_8):
                  def _runEffectFn9(_9):
                    def _runEffectFn10():
                      return fn(_1,_2,_3,_4,_5,_6,_7,_8,_9)
                    return _runEffectFn10
                  return _runEffectFn9
                return _runEffectFn8
              return _runEffectFn7
            return _runEffectFn6
          return _runEffectFn5
        return _runEffectFn4
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1



def runEffectFn10(fn):
  def _runEffectFn1(_1):
    def _runEffectFn2(_2):
      def _runEffectFn3(_3):
        def _runEffectFn4(_4):
          def _runEffectFn5(_5):
            def _runEffectFn6(_6):
              def _runEffectFn7(_7):
                def _runEffectFn8(_8):
                  def _runEffectFn9(_9):
                    def _runEffectFn10(_10):
                      def _runEffectFn11():
                        return fn(_1,_2,_3,_4,_5,_6,_7,_8,_9,_10)
                      return _runEffectFn11
                    return _runEffectFn10
                  return _runEffectFn9
                return _runEffectFn8
              return _runEffectFn7
            return _runEffectFn6
          return _runEffectFn5
        return _runEffectFn4
      return _runEffectFn3
    return _runEffectFn2
  return _runEffectFn1


