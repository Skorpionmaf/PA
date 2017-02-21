import playingarroundwithalgebra2 as p, iteratorRational as r

if __name__ == '__main__':
    prod = lambda x, y: r.Rational((x.getNum() * y.getNum()),
                                 (x.getDen() * y.getDen()))

    mset = { r.Rational(i, 1) for i in range(1, 10) }

    p.Monoid.checkClosure(mset, prod) #dovrebbe sollevare un eccezione ma non lo fa perchè il check e' sul tipo e non sull'appartenenza all'insieme